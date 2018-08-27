import json
import pytest
import boto3
from zonal_stats_function import app

session = boto3.Session()

apigw_event_template = {
        "body": "",
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": ""
            },
            "stage": "Dev"
        },
        "queryStringParameters": {
            "foo": "bar"
        },
        "headers": {
            "Via":
            "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language":
            "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer":
            "true",
            "CloudFront-Is-SmartTV-Viewer":
            "false",
            "CloudFront-Is-Mobile-Viewer":
            "false",
            "X-Forwarded-For":
            "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country":
            "US",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests":
            "1",
            "X-Forwarded-Port":
            "443",
            "Host":
            "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto":
            "https",
            "X-Amz-Cf-Id":
            "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer":
            "false",
            "Cache-Control":
            "max-age=0",
            "User-Agent":
            "Custom User Agent String",
            "CloudFront-Forwarded-Proto":
            "https",
            "Accept-Encoding":
            "gzip, deflate, sdch"
        },
        "httpMethod": "POST",
        "path": "/zonal_stats"
    }

polygon_event_body = '''
{
    "type": "FeatureCollection",
    "name": "charleston-poly",
    "features": [{
        "type": "Feature",
        "properties": {
            "id": null
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-79.662208557128906, 32.920664249232836],
                    [-79.685039520263672, 32.930174118010605],
                    [-79.717311859130845, 32.906541649538447],
                    [-79.691219329833984, 32.895299602872463],
                    [-79.676971435546875, 32.902362080894527],
                    [-79.675083160400391, 32.909568110575655],
                    [-79.662208557128906, 32.920664249232836]
                ]
            ]
        }
    }]
}
'''

multipolygon_event_body = '''
{
    "type": "FeatureCollection",
    "name": "charleston-multi-poly",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "features": [{
        "type": "Feature",
        "properties": {
            "id": null
        },
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [-79.744316416802718, 32.918307771183919],
                        [-79.758743269652271, 32.880394658156938],
                        [-79.827024159455647, 32.910824100458811],
                        [-79.793686860877372, 32.942719190317831],
                        [-79.744316416802718, 32.918307771183919]
                    ]
                ],
                [
                    [
                        [-79.662208557128906, 32.920664249232836],
                        [-79.685039520263672, 32.930174118010605],
                        [-79.717311859130845, 32.906541649538447],
                        [-79.691219329833984, 32.895299602872463],
                        [-79.676971435546875, 32.902362080894527],
                        [-79.675083160400391, 32.909568110575655],
                        [-79.662208557128906, 32.920664249232836]
                    ]
                ]
            ]
        }
    }]
}
'''

def test_polygon_event():
    event = apigw_event_template
    event['body'] = polygon_event_body
    ret = app.lambda_handler(event, "")

    assert ret['statusCode'] == 200
#    assert ret['body'] == json.dumps({'hello': 'world'})

def test_multipolygon_event():
    event = apigw_event_template
    event['body'] = multipolygon_event_body
    ret = app.lambda_handler(event, "")

    assert ret['statusCode'] == 200

