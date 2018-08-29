#! /usr/bin/env bash

funcs=( 'identify_function' 'zonal_stats_function' )

VRT_DEV='ALL_DATASETS_CONUS_DEV.vrt'
VRT_PROD='ALL_DATASETS_CONUS_PROD.vrt'

CONFIG_DEV='config-dev.yml'
CONFIG_PROD='config-prod.yml'

for i in "${funcs[@]}"
do
	# Copy function code, utility code, and config files
	# to the lambda function's build folder
	cp $i/* $i/build/
	cp lib/lib.py $i/build/
	cp $CONFIG_DEV $CONFIG_PROD $VRT_DEV $VRT_PROD $i/build/
done

