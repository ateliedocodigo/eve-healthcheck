#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest

import eve
from bson import ObjectId
from flask_pymongo import MongoClient

from tests.test_settings import \
    MONGO_HOST, MONGO_PORT, \
    MONGO_USERNAME, MONGO_PASSWORD, MONGO_DBNAME

from eve_healthcheck import EveHealthCheck


class TestBase(unittest.TestCase):

    healthcheck_uri = '/h'

    def setUp(self, settings=None):
        self.this_directory = os.path.dirname(os.path.realpath(__file__))
        if settings is None:
            settings = os.path.join(self.this_directory, 'test_settings.py')

        self.setupDB()

        self.settings = settings
        self.app = eve.Eve(settings=self.settings)

        self.test_client = self.app.test_client()
        self.domain = self.app.config['DOMAIN']

        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

    def tearDown(self):
        del self.app
        del self.test_client
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
