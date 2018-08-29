#! /usr/bin/env bash

funcs=( 'identify_function' 'zonal_stats_function' )

for i in "${funcs[@]}"
do
	pip install -U pip pipenv
	rm -rf $i/build/
	pipenv lock -r > requirements.txt
	pip install -Ur requirements.txt -t $i/build/
done
