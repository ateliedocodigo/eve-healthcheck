#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eve_healthcheck import EveHealthCheck
from tests import fail_check, TestBase


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

        self.hc.hc.add_check(fail_check)
        r = self.test_client.get(self.healthcheck_uri)
        self.assertEqual(500, r.status_code)

        jr = self.parse_response(r)
        self.assertEqual("failure", jr["status"])

    def test_database_success_check(self):
        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri))
            self.assertEqual(200, r.status_code)

            jr = self.parse_response(r)
            self.assertEqual("success", jr["status"])

    def test_database_failure_check(self):
        # set an invalid database
        self.app.config['MONGO_URI'] = 'mongodb://invalid.db.net/db'
        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri))

            self.assertEqual(500, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("failure", jr["status"])

    def test_url_prefix_success_check(self):
        url_prefix = 'prefix'
        # set an invalid database
        self.app.config['URL_PREFIX'] = url_prefix

        # Recreate the healthcheck object in order to get utl prefix
        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}/{}{}".format(url_prefix, k, self.healthcheck_uri))

            self.assertEqual(200, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("success", jr["status"])

    def test_url_prefix_failure_check(self):
        url_prefix = 'prefix'
        # set an invalid database
        self.app.config['MONGO_URI'] = 'mongodb://invalid.db.net/db'
        self.app.config['URL_PREFIX'] = url_prefix

        # Recreate the healthcheck object in order to get utl prefix
        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}/{}{}".format(url_prefix, k, self.healthcheck_uri))

            self.assertEqual(500, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("failure", jr["status"])

    def test_url_api_version_success_check(self):
        api_version = '1.0.0'
        # set an invalid database
        self.app.config['API_VERSION'] = api_version

        # Recreate the healthcheck object in order to get utl prefix
        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}/{}{}".format(api_version, k, self.healthcheck_uri))

            self.assertEqual(200, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("success", jr["status"])

    def test_url_api_version_failure_check(self):
        api_version = '1.0.0'
        # set an invalid database
        self.app.config['MONGO_URI'] = 'mongodb://invalid.db.net/db'
        self.app.config['API_VERSION'] = api_version

        # Recreate the healthcheck object in order to get utl prefix
        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}/{}{}".format(api_version, k, self.healthcheck_uri))

            self.assertEqual(500, r.status_code)
            jr = self.parse_response(r)
            self.assertEqual("failure", jr["status"])
