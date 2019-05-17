#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eve import Eve

from eve_healthcheck import EveHealthCheck
from tests import TestBase, fail_check


class TestCors(TestBase):
    origin_header = {'Origin': 'http://example.com'}

    def setUp(self, **kwargs):
        super(TestCors, self).setUp()

        self.app = Eve(settings=self.settings)
        # set cors origins
        self.app.config['X_DOMAINS'] = '*'

        # Recreate the healthcheck
        self.hc = EveHealthCheck(self.app, self.healthcheck_uri)

    def test_cors_when_success_check(self):
        r1 = self.test_client.get(self.healthcheck_uri, headers=self.origin_header)
        self.assertIn(('Access-Control-Allow-Origin', self.origin_header['Origin']), list(r1.headers))
        self.assertSuccessCheck(r1)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri), headers=self.origin_header)

            self.assertIn(('Access-Control-Allow-Origin', self.origin_header['Origin']), list(r.headers))
            self.assertSuccessCheck(r)

    def test_cors_when_failure_check(self):
        self.hc.hc.add_check(fail_check)

        r1 = self.test_client.get(self.healthcheck_uri, headers=self.origin_header)
        self.assertIn(('Access-Control-Allow-Origin', self.origin_header['Origin']), list(r1.headers))
        self.assertFailureCheck(r1)

        # check each domain
        for k, v in self.app.config.get('DOMAIN', {}).items():
            r = self.test_client.get("/{}{}".format(k, self.healthcheck_uri), headers=self.origin_header)

            self.assertIn(('Access-Control-Allow-Origin', self.origin_header['Origin']), list(r.headers))
            self.assertFailureCheck(r)
