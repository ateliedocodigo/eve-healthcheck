include defines.mk

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

.PHONY: install
install: $(PYTHON_ACTIVATE)
	# $(PIP) install -r requirements-dev.txt
	$(PYTHON) setup.py install

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

ifndef VERBOSE
.SILENT:
endif
