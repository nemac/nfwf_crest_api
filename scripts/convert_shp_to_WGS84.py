#! /usr/bin/env python

import fiona
import sys, os, os.path
import click
import pyproj
from fiona.crs import from_epsg

# Helper methods for transforming geometries

WGS84 = pyproj.Proj(init='epsg:4326')
AEA = pyproj.Proj(proj='aea', lat_1=29.5, lat_2=45.5, lat_0=37.5, lon_0=-96, x_0=0, y_0=0, datum='NAD83', units='m')

def transform_polygon(coords):
  new_coords = []
  for coord in coords:
    new_coord = list(pyproj.transform(AEA, WGS84, coord[0], coord[1]))
    new_coords.append(new_coord)
  return new_coords


def transform_geom(geom):
  if geom['type'] == 'Polygon':
    coords = geom['coordinates'][0]
    geom['coordinates'] = [ transform_polygon(coords) ]
  elif geom['type'] == 'MultiPolygon':
    new_polys = []
    for poly in geom['coordinates']:
      new_coords = []
      for coords in poly:
        new_coords.append(transform_polygon(coords))
      new_polys.append(new_coords)
    geom['coordinates'] = new_polys
  else:
    print("Geometry type must be MultiPolygon or Polygon")
    raise
  return geom



@click.command()
@click.argument('file_path',
  type=click.Path(exists=True, resolve_path=True)
)
def convert_shpfile_to_WGS84(file_path):
    shpfile = fiona.open(file_path)
    new_file_path = file_path + "_WGS84.shp"

    new_crs = from_epsg('4326')
    new_driver = shpfile.driver
    new_schema = shpfile.schema

    with fiona.open(
            new_file_path,
            'w',
            crs=new_crs,
            driver=new_driver,
            schema=new_schema) as shp:
        for f in shpfile:
            f['geometry'] = transform_geom(f['geometry'])
            shp.write(f)




if __name__ == '__main__':
    convert_shpfile_to_WGS84() 
