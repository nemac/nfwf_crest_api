#!/usr/bin/env python

'''
Convert a GeoTiff file to a Cloud-Optimized GeoTiff.

https://trac.osgeo.org/gdal/wiki/CloudOptimizedGeoTIFF

Assumes gdal tools (gdal_translate, gdalbuildvrt) are in PATH.

Install the click library before use.

Use the --help option for more information:

python convert_to_cogeo.py --help

'''

import sys, os, os.path
import click

@click.command()
@click.option('-of', default='GTiff', show_default=True, type=click.STRING, help='Output format.')
@click.option('-ot', default='Byte', show_default=True, type=click.STRING, help='Data type of output bands.')
@click.option('-r', default='average', show_default=True, help=(
    'Resampling algorithm to use'),
    type=click.Choice(['nearest','bilinear','cubic','cubicspline','lanczos','average','mode']))
@click.option('-a_nodata', default=255, show_default=True, help=(
    'Optional nodata value to use instead of default nodata for src_dataset.'))
@click.option('-tmpdir', help=(
    'Optional directory to place temporary files. Defaults to directory of src_dataset'))
@click.option('-blocksize', show_default=True, default=128, type=click.INT, help=(
    'Blocksize to use when converting dataset.'))
@click.option('--convert_nodata', is_flag=True, help=(
    'Convert pixel values equal to the nodata value of src_dataset to -a_nodata.'))
@click.argument('src_dataset', required=True, type=click.Path(exists=True, resolve_path=True))
def convert_to_cogeotiff(of, ot, r, a_nodata, tmpdir, blocksize, convert_nodata, src_dataset):
  
  path_pair = os.path.split(src_dataset)
  filename_with_ext = path_pair[1]
  tmpdir = path_pair[0] if tmpdir is None else tmpdir

  gdal_translate = ['gdal_translate',
    '-stats',
    '-ot {0}'.format(ot),
    '-of {0}'.format(of),
    '-r  {0}'.format(r),
    '-co COMPRESS=LZW',
    '-co TILED=YES',
    '-co BLOCKXSIZE={0}'.format(str(blocksize)),
    '-co BLOCKYSIZE={0}'.format(str(blocksize)),
    '-co COPY_SRC_OVERVIEWS=YES',
    '--config GDAL_TIFF_OVR_BLOCKSIZE {0}'.format(str(blocksize))
  ]

  if a_nodata:
    gdal_translate.append('-a_nodata {0}'.format(a_nodata))

    # Use an intermediate vrt file to convert nodata pixel values
    if convert_nodata:
      vrtpath = os.path.join(tmpdir, filename_with_ext) + '.vrt'
      gdalbuildvrt = ['gdalbuildvrt']
      gdalbuildvrt.append('-vrtnodata {0}'.format(a_nodata))
      gdalbuildvrt.append('"{0}" "{1}"'.format(vrtpath, src_dataset))
      gdalbuildvrt_command = ' '.join(gdalbuildvrt)
      click.echo(gdalbuildvrt_command)
      try:
        os.system(gdalbuildvrt_command)
      except:
        click.echo("Something went wrong when building the intermediate vrt file!")
        sys.exit(1)
    else:
      vrtpath = ''

  dst_dataset = '{0}_NEW'.format(src_dataset)
  gdal_translate.append('"{0}"'.format(src_dataset if not vrtpath else vrtpath))
  gdal_translate.append('"{0}"'.format(dst_dataset))
  
  gdal_translate_command = ' '.join(gdal_translate)
  click.echo(gdal_translate_command)
  try:
    os.system(gdal_translate_command)
  except:
    click.echo("Something went wrong while trying to run gdal_translate!")
    sys.exit(1)

  # Cleanup
  try:
    os.remove(vrtpath)
  except:
    pass

  try:
    os.remove(src_dataset)
    os.rename(dst_dataset, src_dataset)
    click.echo('Done!')
  except:
    click.echo("Error while attempting to rename intermediate translated dataset!")
    sys.exit(1)

if __name__ == '__main__':
  convert_to_cogeotiff()