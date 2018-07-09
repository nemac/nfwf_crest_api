'''
Convert a GeoTiff file to a Cloud-Optimized GeoTiff
of type Byte with a 255 nodata value.

Provide a file path as an argument.

Assumes gdal tools (gdal_translate, gdalbuildvrt) are in PATH.

'''

import sys, os, os.path

if not len(sys.argv) > 1:
  print("Please supply a path to a file to convert.")
  exit(0)

path = sys.argv[1]

if not os.path.isfile(path):
  print("Provided path to file does not exist!")
  exit(0)

path_pair = os.path.split(path)

file_dir = path_pair[0]

filename_with_ext = path_pair[1]

filename = ''.join(filename_with_ext.split('.')[:-1])

print('Converting file {0}...'.format(filename_with_ext))

gdalbuildvrt = 'gdalbuildvrt -vrtnodata 255 {0}.vrt {0}.tif'.format(filename)

print(gdalbuildvrt)

os.chdir(file_dir)

os.system(gdalbuildvrt)

gdal_translate = ('gdal_translate {0}.vrt {0}_NEW.tif'
  ' -ot Byte'
  ' -of GTiff'
  ' -co COMPRESS=LZW'
  ' -co TILED=YES'
  ' -co BLOCKXSIZE=128'
  ' -co BLOCKYSIZE=128'
  ' -co COPY_SRC_OVERVIEWS=YES'
  ' --config GDAL_TIFF_OVR_BLOCKSIZE 128'
  ).format(filename)

print(gdal_translate)

os.system(gdal_translate)

# Cleanup
os.remove('{0}.vrt'.format(filename))
os.remove('{0}.tif'.format(filename))

os.rename('{0}_NEW.tif'.format(filename), '{0}.tif'.format(filename))
