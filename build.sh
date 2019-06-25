#! /usr/bin/env bash

funcs=( 'identify_function' 'zonal_stats_function' 'upload_shape_function' )

source '.env'

pip install -U pip pipenv

DEPS_FLAG=$1

for i in "${funcs[@]}"
do
  if [ "$DEPS_FLAG" = "--deps" ]; then
    docker run --rm -v ${PWD}:/var/task -it lambci/lambda:build-python3.6 /bin/bash -c \
      "rm -rf $i/build/ && \
      rm -rf $i/\.tif && \
      pipenv lock -r > requirements.txt && \
      pip install -Ur requirements.txt -t $i/build/"
  fi
  sudo cp $CONFIG_FILE_DEV $CONFIG_FILE_PROD $CONFIG_FILE_LOCAL $i/
  sudo cp $VRT_FILE_DEV $VRT_FILE_PROD $i/
  sudo cp $i/* $i/build/
  sudo cp -R lib/ $i/
  sudo cp -R lib/ $i/build/
done
