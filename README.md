eve-healthcheck
===========

[![Build Status](https://travis-ci.org/ateliedocodigo/eve-healthcheck.svg?branch=master)](https://travis-ci.org/ateliedocodigo/eve-healthcheck)
[![Requirements Status](https://requires.io/github/ateliedocodigo/eve-healthcheck/requirements.svg?branch=master)](https://requires.io/github/ateliedocodigo/eve-healthcheck/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/ateliedocodigo/eve-healthcheck/badge.svg?branch=master)](https://coveralls.io/github/ateliedocodigo/eve-healthcheck?branch=master)

[eve-healthcheck](https://pypi.python.org/pypi/eve-healthcheck) is project that servers healthcheck urls used to monitor your application  [Eve](http://python-eve.org/) powered RESTful API.

Usage
----

```python
from eve_healthcheck import EveHealthCheck
...

app = Eve()
hc = EveHealthCheck(app, '/healthcheck')
...
```

This will add an url `/healthckeck` that will check database connection like:

```json
{'hostname': 'localhost',
 'results': [{'checker': 'database_check',
              'expires': 1487655119.5796409,
              'output': 'Database OK',
              'passed': True,
              'timestamp': 1487655092.5796409}],
 'status': 'success',
 'timestamp': 1487655092.5820687}
```

Running tests with `tox`
----

Install `tox`
```
$ pip install tox
```

Run tests

```
tox
```
