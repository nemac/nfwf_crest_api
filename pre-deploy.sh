#! /usr/bin/env bash

funcs=( 'identify_function' 'zonal_stats_function' 'upload_shape_function' )

source '.env'

for i in "${funcs[@]}"
do
	pip install -U pip pipenv
	rm -rf $i/build/
	pipenv lock -r > requirements.txt
	pip install -Ur requirements.txt -t $i/build/
	cp $CONFIG_FILE_DEV $CONFIG_FILE_PROD $i/
	cp $VRT_FILE_DEV $VRT_FILE_PROD $i/
	cp $i/* $i/build/
	cp -R lib/ $i/
	cp -R lib/ $i/build/
done

