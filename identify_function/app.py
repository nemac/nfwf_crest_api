import boto3
import json
import os
import rasterio as rio
import rasterio.warp as warp
from rasterio.crs import CRS

session = boto3.Session()

def runs_on_aws_lambda():
    """
        Returns True if this function is executed on AWS Lambda service.
    """
    return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ


def lambda_handler(event, context):
    """
        AWS Lambda handler

        This method is invoked by the API Gateway: /Prod/first/{proxy+} endpoint.
    """

    params = event['queryStringParameters']

    response = get_identify(params)

    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": {
            "Content-Type": 'application/json',
            "Access-Control-Allow-Origin": "*"
        }
    }


def get_identify(params):

    # Band 1 = Exposure Index
    # Band 2 = Asset Index
    # Band 3 = Threat Index
    # Band 4 = Aquatic Index
    # Band 5 = Terrestrial Index
    # Band 6 = Hubs (preliminary)
    
    bands = (1, 2, 3, 4, 5, 6)

    data_source = "ALL_INDICES_CONUS.vrt"

    with rio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
        with rio.open(data_source) as src:

            # Transform Coords
            if runs_on_aws_lambda():
                xs = [ float(params['lng']) ]
                ys = [ float(params['lat']) ]
            else:
                xs = [ float(params['lng'][0]) ]
                ys = [ float(params['lat'][0]) ]

            src_crs = CRS.from_epsg(4326)
            # deprecated, use src.crs
            dst_crs = src.get_crs()
            t_coords = warp.transform(src_crs, dst_crs, xs, ys)
            coords = [(t_coords[0][0], t_coords[1][0])]
            
            # Identify
            response = {}
            result_gen = src.sample(coords, bands)
            result = next(result_gen)
            response['asset'] = str(result[0])
            response['threat'] = str(result[1])
            response['exposure'] = str(result[2])
            response['aquatic'] = str(result[3])
            response['terrestrial'] = str(result[4])
            response['hubs'] = str(result[5])

    return response
