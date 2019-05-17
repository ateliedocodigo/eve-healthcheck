#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from functools import partial

from eve.render import send_response
from healthcheck import HealthCheck


def view_health_func(hc, resource=None):
    message, status, headers = hc.run()
    response = (
        json.loads(message),
        None,
        None,
        status,
        [(k, v) for k, v in headers.items()],
    )

    return send_response(resource, response)


def check_wrapper(app):
    def database_check():
        # perform a count
        for k, v in app.config.get('DOMAIN', {}).items():
            result = app.data.is_empty(k)
            assert type(result) == bool, "Database NOK"
        return True, "Database OK"

    return database_check


class EveHealthCheck(object):
    def __init__(self, app=None, healthcheck_uri='/healthcheck', *argv, **kw):
        self.logger = logging.getLogger(self.__module__)
        self.hc = HealthCheck(*argv, **kw)

        if app:
            self.init_app(app, healthcheck_uri)

    def init_app(self, app, healthcheck_uri='/healthcheck'):
        self.hc.add_check(check_wrapper(app))

        uri = "{}{}".format(app.api_prefix, healthcheck_uri)

        app.add_url_rule(uri, uri,
                         view_func=partial(view_health_func, self.hc),
                         methods=['GET', 'OPTIONS'])
        for resource, v in app.config.get('DOMAIN', {}).items():
            uri = "{}/{}{}".format(app.api_prefix, resource, healthcheck_uri)
            self.logger.debug("Adding uri {}".format(uri))
            app.add_url_rule(uri, uri,
                             view_func=partial(view_health_func, self.hc, resource),
                             methods=['GET', 'OPTIONS'])
