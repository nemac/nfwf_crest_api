import pytest


class LambdaContext:
  def __init__(self):
    self.invoked_function_arn = 'pytest'


@pytest.fixture(scope="module")
def lambda_context():
  context = LambdaContext()
  return context


@pytest.fixture(scope="module")
def apigw_event_factory():

  def _factory (event_type):
    body = ''
    queryStringParams = {}

    if event_type == 'identify':
      queryStringParams = {
        "lat": -80.01140194,
        "lng": 32.88178577
      }
    elif event_type == 'zonal_stats:polygon':
      body = '''
        {
          "type": "FeatureCollection",
          "name": "test-ar",
          "features": [{
            "type": "Feature",
            "properties": {
              "id": null
            },
            "geometry": {
              "type": "Polygon",
              "coordinates": [
                [
                  [-80.01149654388428, 32.887677980874706],
                  [-80.01911401748657, 32.88337138447869],
                  [-80.01553058624268, 32.87764094428261],
                  [-80.00417947769165, 32.882578515468],
                  [-80.01149654388428, 32.887677980874706]
                ]
              ]
            }
          }]
        }
      '''
    elif event_type == 'zonal_stats:multipolygon':
      body = '''
        {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "properties": {},
              "geometry": {
                "type": "MultiPolygon",
                "coordinates": [
                  [
                    [
                      [-80.01402318477629, 32.88335786972543],
                      [-80.01506388187408, 32.881371178577474],
                      [-80.01121759414673, 32.881407218722806],
                      [-80.01402318477629, 32.88335786972543]
                    ]
                  ],
                  [
                    [
                      [-80.01388370990753, 32.88338039431306],
                      [-80.00966727733612, 32.88092067552428],
                      [-80.00970482826233, 32.88469131544987],
                      [-80.01388370990753, 32.88338039431306
                      ]
                    ]
                  ]
                ]
              }
            }
          ]
        }
      '''

    return {
      "body": body,
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
      "queryStringParameters": queryStringParams,
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

  return _factory