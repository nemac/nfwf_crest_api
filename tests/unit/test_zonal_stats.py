import json
import pytest
import boto3
from zonal_stats_function import app
from lib import lib


def test_polygon_event(lambda_context, apigw_event_factory):
  event = apigw_event_factory('zonal_stats:polygon')
  ret = app.lambda_handler(event, lambda_context)
  assert ret['statusCode'] == 200


def test_multipolygon_event(lambda_context, apigw_event_factory):
  event = apigw_event_factory('zonal_stats:multipolygon')
  ret = app.lambda_handler(event, lambda_context)
  assert ret['statusCode'] == 200

