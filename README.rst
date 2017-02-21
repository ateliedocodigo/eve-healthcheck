eve-healthcheck
===============

|Build Status| |Requirements Status| |Coverage Status|

`eve-healthcheck`_ is project that servers healthcheck urls used to
monitor your application `Eve`_ powered RESTful API.

Usage
-----

.. code:: python

    from eve_healthcheck import EveHealthCheck
    ...

    app = Eve()
    hc = EveHealthCheck(app, '/healthcheck')
    ...

This will add an url ``/healthckeck`` that will check database
connection like:

.. code:: json

    {'hostname': 'localhost',
     'results': [{'checker': 'database_check',
                  'expires': 1487655119.5796409,
                  'output': 'Database OK',
                  'passed': True,
                  'timestamp': 1487655092.5796409}],
     'status': 'success',
     'timestamp': 1487655092.5820687}

Running tests with ``tox``
--------------------------

Install ``tox``

::

    $ pip install tox

Run tests

::

    tox

.. _eve-healthcheck: https://pypi.python.org/pypi/eve-healthcheck
.. _Eve: http://python-eve.org/

.. |Build Status| image:: https://travis-ci.org/ateliedocodigo/eve-healthcheck.svg?branch=master
   :target: https://travis-ci.org/ateliedocodigo/eve-healthcheck
.. |Requirements Status| image:: https://requires.io/github/ateliedocodigo/eve-healthcheck/requirements.svg?branch=master
   :target: https://requires.io/github/ateliedocodigo/eve-healthcheck/requirements/?branch=master
.. |Coverage Status| image:: https://coveralls.io/repos/github/ateliedocodigo/eve-healthcheck/badge.svg?branch=master
   :target: https://coveralls.io/github/ateliedocodigo/eve-healthcheck?branch=master