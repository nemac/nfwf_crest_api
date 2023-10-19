try:
  import unzip_requirements
except ImportError:
  pass
import os, json, numpy, numpy.ma
from pyproj import Transformer
from rasterio import Env, open
from rasterio.mask import mask
from numpy.ma import masked_outside
from numpy import isnan
from copy import deepcopy
import util

def handler(event, context):
  try:
    geojson = json.loads(event['body'])
  except:
    geojson = event['body']

  region = event['queryStringParameters']['region']
  response = get_response(geojson, region)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_zonal_stat(arr):
  result = arr.mean()
  if isnan([result]):
    result = "NaN"
  else:
    result = float(result)
  return result


def get_response(geojson, region, local=False):
  if local:
    config = util.get_config('config.local.yml') 
  else:   
    config = util.get_config()
  data_source = config['vrt'][region]
  dataset_names = util.get_dataset_names(config, region)
  if region == 'continental_us' or region == 'alaska' or region == 'great_lakes':
    landcover_to_use = config['NLCD_Landcover']
  else:
    landcover_to_use = config['CCAP_Landcover']

  with Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with open(data_source) as src:
      for feature in geojson['features']:
        geom_latlng = deepcopy(feature['geometry'])
        proj_string = src.profile['crs'].to_proj4()
        transformer = Transformer.from_crs('epsg:4326', proj_string, always_xy=True)
        geom_transformed = util.transform_geom(geom_latlng, transformer)
        geom = [ geom_transformed ]
        out_image, out_transform = mask(src, geom, pad=True, crop=True)
        # TODO this might need to be refactored
        arr = masked_outside(out_image, 0.0, 100.0)
        if 'properties' not in feature:
          feature['properties'] = {}
        feature['properties']['mean'] = {}
        for i in range(0, len(arr)):
          index_name = dataset_names[i]
          if (index_name == 'landcover'): # need to treat landcover differently due to it not being an average
            #hist, bins = numpy.histogram(arr[i].compressed(), bins=range(0, 101))
            hist, bins = numpy.histogram(arr[i], bins=range(0, 101))
            try:
              print(hist)
              landcover_percent = hist / arr[i].compressed().size * 100
            except: # catch divide by zero error?
              landcover_percent = 0
            for key, value in landcover_to_use.items():
              feature['properties']['mean'][key] = landcover_percent[value]
          else: # calculate mean
            mean = get_zonal_stat(arr[i])
            feature['properties']['mean'][index_name] = mean
  return geojson

