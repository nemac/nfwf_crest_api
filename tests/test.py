import os.path, os, sys, json
import requests
import boto3
import hashlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util import get_config

config = get_config()
offline_api = 'http://localhost:3000/dev/'


def test_identify():
    identify_api = os.path.join(offline_api, 'identify')
    print('TEST: Identify')
    print(f'URL: {identify_api}')
    print()
    for region in config['test']['points']:
        print(f'Testing region: {region}... ', end='')
        params = config['test']['points'][region]
        params['region'] = region
        r = requests.get(identify_api, params=params)
        if r.status_code != 200:
          print()
          print(f'Error: non-200 status code reported: {r.status_code}')
          print(f'Result: {r.text}')
        print('Done')
    print()
    print('=' * 80)


def test_zonal_stats():
    zonal_stats_api = os.path.join(offline_api, 'zonal_stats')
    print('TEST: Zonal Stats')
    print(f'URL: {zonal_stats_api}')
    print()
    for region in config['test']['polygons']:
        print(f'Testing region: {region}... ', end='')
        data = config['test']['polygons'][region]
        params = {'region': region}
        r = requests.post(zonal_stats_api, data=data, params=params)
        if r.status_code != 200:
          print()
          print(f'Something went wrong. {r.status_code} status code reported.')
          print(f'Response: {r.text}')
        else:
          print('Done')
    print()
    print('=' * 80)


def test_upload_shape():
    upload_shape_api = os.path.join(offline_api, 'upload_shape')
    print('TEST: Upload Shape')
    print(f'URL: {upload_shape_api}')
    print()
    s3 = boto3.resource('s3')
    for region in config['test']['polygons']:
        print(f'Testing region: {region}')  
        config_geojson = config['test']['polygons'][region]
        geojson = "".join(config_geojson.split())
        params = { 'region': region }
        # Use dev stage explicitly for now
        r = requests.post(upload_shape_api, data=geojson, params=params)
        key = json.loads(r.text)['key']
        bucket = config['user_shapes_bucket']
        s3_path = os.path.join(bucket, key)
        obj = s3.Object(bucket, key)
        fetch_geojson = obj.get()['Body'].read().decode('utf-8')
        check_geojson = "".join(fetch_geojson.split())
        print('Verifying upload... ', end='')
        if check_geojson == geojson:
            print('Done')
        else:
            print('Geojson doesn\'t match!')
            print('Uploaded:')
            print(geojson)
            print('Fetched:')
            print(check_geojson)
        print('Deleting... ', end='')
        obj.delete()
        try:
            obj.get()
        except:
            # NoKey exception indicates successful delete
            print('Done')
        print()
            
    print('=' * 80)


def run_all():
    test_identify()
    test_zonal_stats()
    test_upload_shape()


if __name__ == '__main__':
    run_all()
