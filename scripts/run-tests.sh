#! /usr/bin/env sh

set -ev

pip install -U pip pipenv
pipenv install --dev

pipenv run python -m pytest tests/ -v
