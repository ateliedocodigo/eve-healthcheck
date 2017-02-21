#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from tests import TestBase


class TestEveHealthchek(TestBase):

    def test_api(self):
        self.app.debug = True
        r = self.test_client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_basic_check(self):

        self.app.debug = True

        r = self.test_client.get(self.healthcheck_uri)
        self.assertEqual(200, r.status_code)

    def test_failing_check(self):
        def fail_check():
            return False, "FAIL"

        self.hc.hc.add_check(fail_check)
        r = self.test_client.get(self.healthcheck_uri)
        self.assertEqual(500, r.status_code)

        jr = self.parse_response(r)
        self.assertEqual("failure", jr["status"])

    def test_database_success_check(self):
        # ckeck eatch domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri))
            self.assertEqual(200, r.status_code)

            jr = self.parse_response(r)
            self.assertEqual("success", jr["status"])

    def test_database_failure_check(self):
        # set an invalid database
        self.app.config['MONGO_URI'] = 'mongodb://invalid.db.net/db'
        # ckeck eatch domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri))

            self.assertEqual(500, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("failure", jr["status"])
