#! /usr/bin/env bash

set -ev

source '.env'

funcs=( 'identify_function' 'zonal_stats_function' 'upload_shape_function' )

for i in "${funcs[@]}"
do
	cp $CONFIG_FILE_DEV $CONFIG_FILE_PROD $i/
	cp $VRT_FILE_DEV $VRT_FILE_PROD $i/
	cp -R lib/ $i/
done

pip install -U pip pipenv
pipenv install --dev

pipenv run python -m pytest tests/ -v -s -x
