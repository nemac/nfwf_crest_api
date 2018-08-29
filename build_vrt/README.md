# NFWF Tool Datasets

Prepare datasets for use and generate the Virtual Raster Table used for NEMAC's NFWF Web Tool.

## Requirements

1. [Python 3](https://www.python.org/downloads/)
2. [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html) (see NEMAC AWS administrator)
3. [GDAL](http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries)
4. [Pipenv](https://docs.pipenv.org/)

## Quickstart

Setup development environment:

```bash
pipenv install --three
```

Build the combined VRT for all datasets using default arguments:

```bash
pipenv run ./build_vrt.py
```

Upload the resulting file to the nfwf-tool S3 bucket (requires awscli):

```bash
aws s3 cp ALL_DATASETS_CONUS.vrt s3://nfwf-tool/
```

## More Information

Each dataset has its own input file list which is used by [`gdalbuildvrt`](https://www.gdal.org/gdalbuildvrt.html).


## Preparing New Datasets

To prepare a new dataset, we can use the `convert_to_cogeo.py` script to convert it to a [Cloud-Optimized GeoTiff](https://trac.osgeo.org/gdal/wiki/CloudOptimizedGeoTIFF).

Note: all datasets **MUST** be in the same projection for the generated VRT to function correctly. 

For example, let's say the GIS team has updated the Aquatic Index dataset.

Convert it to a cloud-optimized GeoTIFF:

```bash
pipenv run ./convert_to_cogeo.py --convert_nodata PATH_TO_FILE
```

We use the `--convert_nodata` flag to change pixel values equal to the nodata value 


