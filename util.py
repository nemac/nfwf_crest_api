'''
Utility functions used by many or all of the functions in the API.
'''
import os, os.path, yaml


def transform_polygon(coords, transformer):
  new_coords = []
  for coord in coords:
    x,y = transformer.transform(coord[0], coord[1])
    new_coords.append([x, y])
  return new_coords


def transform_geom(geom, transformer):
  if geom['type'] == 'Polygon':
    coords = geom['coordinates'][0]
    geom['coordinates'] = [ transform_polygon(coords, transformer) ]
  elif geom['type'] == 'MultiPolygon':
    new_polys = []
    for poly in geom['coordinates']:
      new_coords = []
      for coords in poly:
        new_coords.append(transform_polygon(coords, transformer))
      new_polys.append(new_coords)
    geom['coordinates'] = new_polys
  else:
    print("Geometry type must be MultiPolygon or Polygon")
    raise
  return geom


def get_dataset_names(config, region):
  names = list(map(lambda dataset: dataset['name'], config['datasets'][region]))
  return names


def get_config():
  with open('config.yml', 'r') as stream:
    config = yaml.safe_load(stream)
  return config
