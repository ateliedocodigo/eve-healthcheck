PIP = pip3
PYTHON = python3
PIPY_REPOSITORY=pypi

ifdef PY_VENV_PATH
PYTHON_ACTIVATE = . $(PY_VENV_PATH)/bin/activate
PIP = $(PYTHON_ACTIVATE) && pip
PYTHON_BIN := $(PYTHON)
PYTHON := $(PYTHON_ACTIVATE) && $(PYTHON)
ifneq ("$(wildcard $(PY_VENV_PATH)/bin/activate)","")
$(PYTHON_ACTIVATE):
else
$(PYTHON_ACTIVATE):
	virtualenv -p$(PYTHON_BIN) $(PY_VENV_PATH)
endif
endif

.PHONY: clean
clean:
	rm -rf .cache dist/ docs/_build htmlcov *.egg-info

.PHONY: install
install: $(PYTHON_ACTIVATE)
	# $(PIP) install -r requirements-dev.txt
	$(PYTHON) setup.py install

.PHONY: install-dev
install-dev: $(PYTHON_ACTIVATE)
	$(PIP) install -r requirements-dev.txt
	# $(PYTHON) setup.py install

# make lint PY_VENV_PATH=env
.PHONY: lint
lint: $(PYTHON_ACTIVATE) install-dev
	echo "Start linting"
	$(PYTHON_ACTIVATE) && pep8 --exclude .tox,env,docs
	# $(PYTHON_ACTIVATE) && pep257 boilerplate tests

# make test PY_VENV_PATH=env
.PHONY: test
test: install-dev lint
	echo "Start testing"
	$(PYTHON_ACTIVATE) && nosetests -v --with-doctest

# make register PIPY_REPOSITORY=pypitest
.PHONY: register
register:
	$(PYTHON) setup.py register -r ${PIPY_REPOSITORY}

# make dist PIPY_REPOSITORY=pypitest
.PHONY: dist
dist: install
	$(PYTHON) setup.py sdist

# make upload PIPY_REPOSITORY=pypitest
.PHONY: upload
upload:
	$(PYTHON) setup.py sdist upload -r ${PIPY_REPOSITORY}

# make minor PY_VENV_PATH=env
.PHONY: minor
minor:
	$(PYTHON_ACTIVATE) && bumpversion --allow-dirty --verbose minor

# make patch PY_VENV_PATH=env
.PHONY: patch
patch:
	$(PYTHON_ACTIVATE) && bumpversion --allow-dirty --verbose patch

ifndef VERBOSE
.SILENT:
endif
