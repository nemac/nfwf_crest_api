#! /bin/bash

pip install -U pip pipenv

rm -rf identify_function/build/
rm -rf zonal_stats_function/build/

pipenv lock -r > requirements.txt

pip install -Ur requirements.txt -t identify_function/build/
pip install -Ur requirements.txt -t zonal_stats_function/build/

cp identify_function/app.py identify_function/build/
cp zonal_stats_function/app.py zonal_stats_function/build/
