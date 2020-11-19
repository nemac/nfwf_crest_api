#! /usr/bin/env python

import os.path, os, sys, json, argparse
import requests
import boto3
import hashlib
import rasterio as rio
from util import get_config

offline_api = 'http://localhost:3000/dev/'


def test_identify(config, verbose):
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
		if verbose:
			print(f'Result: {r.text}')
			print()
	print()
	print('=' * 80)


def test_zonal_stats(config, verbose):
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
			if verbose:
				print(f'Result: {r.text}')
				print()
	print()
	print('=' * 80)


def test_upload_shape(config, verbose):
	upload_shape_api = os.path.join(offline_api, 'upload_shape')
	print('TEST: Upload Shape')
	print(f'URL: {upload_shape_api}')
	print()
	s3 = boto3.resource('s3')
	for region in config['test']['polygons']:
		print(f'Testing region: {region}')	
		config_geojson = config['test']['polygons'][region]
		geojson = "".join(config_geojson.split())
		# Use dev stage explicitly for now
		r = requests.post(upload_shape_api, data=geojson)
		key = json.loads(r.text)['key']
		bucket = config['user_shapes_bucket']
		s3_path = os.path.join(bucket, key)
		obj = s3.Object(bucket, key)
		fetch_geojson = obj.get()['Body'].read().decode('utf-8')
		check_geojson = "".join(fetch_geojson.split())
		print('Verifying upload... ', end='')
		if check_geojson == geojson:
			print('Done')
			if verbose:
				print(f'Result: {fetch_geojson}')
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


def test_nodata(expected=255):
	print(f"TEST: NoData should be {expected} for all datasets.")
	config = get_config()
	regions = config['datasets']
	fail = False
	for region in regions:
		print(f"Testing region: {region}... ", end='')
		data_source = config['vrt'][region]
		for d in config['datasets'][region]:
			name = d['name']
			path = d['path']
			full_path = os.path.join('/vsis3/nfwf-tool/', path)
			with rio.open(full_path) as src:
				if int(expected) != int(src.nodata):
					print(f"{d['path']} has an unexpected NoData value {src.nodata}!")
					print()
					fail = True
					break
		print('Done.')

	if fail:
		print()
		print('TEST FAILED: Errors encountered. Make sure your datasets all use the same NoData value!!')
		print()

	print('=' * 80)


def setup_argparser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--verbose', '-v', action='store_true', help='Display the result of each test')
	parser.add_argument('--local', action='store_true', help='Use local VRTs')
	return parser


def run_all():
		parser = setup_argparser()
		args = parser.parse_args()
		verbose = args.verbose
		local = args.local
		# This doesn't actually cause the functions to use the local VRTs at the moment
		if local:
			config = get_config('config.local.yml')
		else:
			config = get_config()
		test_identify(config, verbose)
		test_zonal_stats(config, verbose)
		test_upload_shape(config, verbose)
		test_nodata()


if __name__ == '__main__':
		run_all()

