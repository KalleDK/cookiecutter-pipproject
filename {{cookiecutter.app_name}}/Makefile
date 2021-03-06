VERSION=patch

.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist major minor patch upload

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 {{ cookiecutter.app_name }} test

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source {{ cookiecutter.app_name }} setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/{{ cookiecutter.app_name }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.app_name }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

upload: patch release
	twine upload dist/* -r testpypi

release: clean
	python setup.py sdist
	python setup.py bdist_wheel

sdist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

major: VERSION = major
major: bump

minor: VERSION = minor
minor: bump

patch: VERSION = patch
patch: bump

bump:
	@bumpversion --config-file setup.cfg ${VERSION}
