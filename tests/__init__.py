#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest

import eve
from pymongo import MongoClient

from eve_healthcheck import EveHealthCheck
from tests.test_settings import MONGO_DBNAME, MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USERNAME


def fail_check():
    return False, "FAIL"


class TestBase(unittest.TestCase):
    healthcheck_uri = '/h'

    def setUp(self, settings=None):
        self.this_directory = os.path.dirname(os.path.realpath(__file__))
        if settings is None:
            settings = os.path.join(self.this_directory, 'test_settings.py')

        self.setupDB()

        self.settings = settings
        self.app = eve.Eve(settings=self.settings)

        self.domain = self.app.config['DOMAIN']

        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

    def tearDown(self):
        del self.app
        del self.hc
        self.dropDB()

    def setupDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        if MONGO_USERNAME:
            self.connection[MONGO_DBNAME].add_user(MONGO_USERNAME,
                                                   MONGO_PASSWORD,
                                                   False)

    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()

    def parse_response(self, r):
        try:
            v = json.loads(r.get_data().decode('utf-8'))
        except ValueError:
            v = None
        return v

    def assertSuccessCheck(self, response):
        self.assertEqual(200, response.status_code)
        jr = self.parse_response(response)
        self.assertEqual("success", jr["status"])

    def assertFailureCheck(self, response):
        self.assertEqual(500, response.status_code)
        jr = self.parse_response(response)
        self.assertEqual("failure", jr["status"])

    @property
    def test_client(self):
        return self.app.test_client()
