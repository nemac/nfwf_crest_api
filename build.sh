#! /usr/bin/env bash

set -e

funcs=( 'identify_function' 'zonal_stats_function' 'upload_shape_function' )

source '.env'

DEPS_FLAG=$1

pip install -U pip pipenv

for i in "${funcs[@]}"
do
  if [ "$DEPS_FLAG" = "--deps" ]; then
    docker run --rm -v ${PWD}:/var/task -it lambci/lambda:build-python3.6 /bin/bash -c \
      "rm -rf $i/build/ && \
      rm -rf $i/\.tif && \
      pipenv lock -r > requirements.txt && \
      pip install -Ur requirements.txt -t $i/build/"
  fi
	cp $CONFIG_FILE_DEV $CONFIG_FILE_PROD $i/
	cp $VRT_FILE_DEV $VRT_FILE_PROD $i/
	cp $i/* $i/build/
	cp -r lib/ $i/
	cp -r lib/ $i/build/
done
