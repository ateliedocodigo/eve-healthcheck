#!/usr/bin/env python
# -*- coding: utf-8 -*-

from healthcheck import HealthCheck

import logging


class EveHealthCheck(object):

    def __init__(self, app=None, healthcheck_uri='/healthcheck', *argv, **kw):
        self.logger = logging.getLogger(self.__module__)
        self.hc = HealthCheck(*argv, **kw)

        if app:
            self.init_app(app, healthcheck_uri)

    def init_app(self, app, healthcheck_uri='/healthcheck'):

        def database_check():
            # perform a count
            for k, v in app.config.get('DOMAIN', {}).items():
                result = app.data.is_empty(k)
                assert type(result) == bool, "Database NOK"
            return True, "Database OK"

        self.hc.add_check(database_check)
        app.add_url_rule(healthcheck_uri, healthcheck_uri, view_func=lambda: self.hc.run())
        for k, v in app.config.get('DOMAIN', {}).items():
            self.logger.debug("Adding uri /{}{}".format(k, healthcheck_uri))
            app.add_url_rule("/{}{}".format(k, healthcheck_uri),
                             "/{}{}".format(k, healthcheck_uri),
                             view_func=lambda: self.hc.run())
