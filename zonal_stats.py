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
  data_source_landcover = config['vrt'][region + '_landcover']
  dataset_names = util.get_dataset_names(config, region)
  dataset_names_landcover = util.get_dataset_names(config, region + '_landcover')
  if region == 'continental_us' or region == 'alaska' or region == 'great_lakes':
    landcover_to_use = config['NLCD_Landcover']
  else:
    landcover_to_use = config['CCAP_Landcover']

  with Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    # The reason there are two data sources here is because we needed to
    # create an entirely separate VRT for landcover data. Trying to combine
    # landcover data with the rest of the zonal stats data was causing too many errors
    with open(data_source) as src, open(data_source_landcover) as src_landcover:
      for feature in geojson['features']:
        proj_string_src = src.profile['crs'].to_proj4()
        proj_string_src_landcover = src_landcover.profile['crs'].to_proj4()
        transformer_src = Transformer.from_crs('epsg:4326', proj_string_src, always_xy=True)
        transformer_landcover = Transformer.from_crs('epsg:4326', proj_string_src_landcover, always_xy=True)
        geom_latlng = deepcopy(feature['geometry'])
        geom_transformed_src = util.transform_geom(geom_latlng, transformer_src)
        geom_latlng = deepcopy(feature['geometry'])
        geom_transformed_landcover = util.transform_geom(geom_latlng, transformer_landcover)
        geom = [ geom_transformed_src ]
        geom_landcover = [ geom_transformed_landcover ]
        out_image, out_transform = mask(src, geom, pad=True, crop=True)
        out_image_landcover, out_transform_landcover = mask(src_landcover, geom_landcover, pad=True, crop=True)
        # TODO this might need to be refactored
        arr = masked_outside(out_image, 0.0, 100.0)
        arr_landcover = masked_outside(out_image_landcover, 0.0, 100.0)
        if 'properties' not in feature:
          feature['properties'] = {}
        feature['properties']['mean'] = {}
        for i in range(0, len(arr)):
          index_name = dataset_names[i]
          mean = get_zonal_stat(arr[i])
          feature['properties']['mean'][index_name] = mean
        # landcover stuff
        hist, bins = numpy.histogram(arr_landcover, bins=range(0, 101))
        if (arr_landcover.compressed().size != 0):
          landcover_percent = (hist / arr_landcover.compressed().size) * 100
          for key, value in landcover_to_use.items():
            val = "NaN" if isnan(landcover_percent[value]) else landcover_percent[value]
            feature['properties']['mean'][key] = val
  return geojson

