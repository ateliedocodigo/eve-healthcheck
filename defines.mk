PIP = pip3
PYTHON = python3
PIPY_REPOSITORY=pypi

BASE_PKG_NAME=boilerplate
PKG_NAME=boilerplate

script_env = \
	PIP="$(PIP)"                           \
	PYTHON="$(PYTHON)"                     \
	PIPY_REPOSITORY="$(PIPY_REPOSITORY)"   \
	BASE_PKG_NAME="$(BASE_PKG_NAME)"       \
	PKG_NAME="$(PKG_NAME)"                 \
	VERSION="$(VERSION)"


.PHONY: clean
clean:
	rm -rf .cache .tox/ .coverage build/ dist/ docs/_build htmlcov *.egg-info

.PHONY: rename
rename: $(script_env)
ifeq ($(BASE_PKG_NAME),$(PKG_NAME))
	echo "Set a different name to rename BASE_PKG_NAME or PKG_NAME ie.:";
	echo "\t$$ make rename PKG_NAME=my_pkg"
	exit 1
endif
	echo "Rename package from $(BASE_PKG_NAME) to $(PKG_NAME)"
	grep -rl $(BASE_PKG_NAME) . | grep -v .git/  | grep -v defines.mk | xargs sed -i 's/$(BASE_PKG_NAME)/$(PKG_NAME)/g'
	mv $(BASE_PKG_NAME) $(PKG_NAME)
