#!/usr/bin/env python
# -*- coding: utf-8 -*-

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'test_user'
MONGO_PASSWORD = 'test_pw'
MONGO_DBNAME = 'eve_healthcheck_test'

TRANSPARENT_SCHEMA_RULES = True
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'people': {
        'description': 'the people resource',
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
                'unique': True,
                'description': 'the last name of the person'
            },
            'skills': {
                'type': 'list',
                'schema': {
                    "type": "objectid",
                    "data_relation": {
                        "resource": "skills",
                        "embeddable": True
                    }
                }
            },
        }
    },
    'skills': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
                'unique': True,
            },
        },
    },
}
