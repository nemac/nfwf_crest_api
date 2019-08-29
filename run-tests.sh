#! /usr/bin/env bash

set -ev

# cd ..

pip install -U pip pipenv
pipenv install --dev

pipenv run python -m pytest tests/ -v -s -x
