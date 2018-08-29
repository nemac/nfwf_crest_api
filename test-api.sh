#! /usr/bin/env sh

set -ev

case $1 in "dev")
  STACK_NAME='nfwf-tool-api-dev'
  ;;
"prod")
  STACK_NAME='nfwf-tool-api'
  ;;
*)
  echo "You must provide a stage to deploy to as an argument to this script (either 'dev' or 'prod')"
  exit 1
  ;;
esac

ZONAL_STATS_OUTPUT_VALUE='ZonalStatsApigwURL'
IDENTIFY_OUTPUT_VALUE='IdentifyApigwURL'

get_endpoint () {
	echo $(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --output text \
    --query "Stacks[].Outputs[?OutputKey==\`$1\`].{OutputValue:OutputValue}")
}

ZONAL_STATS_ENDPOINT=$(get_endpoint $ZONAL_STATS_OUTPUT_VALUE)
IDENTIFY_ENDPOINT=$(get_endpoint $IDENTIFY_OUTPUT_VALUE)
IDENTIFY_PARAMS="?lat=80&lng=33"
IDENTIFY_REQUEST="$IDENTIFY_ENDPOINT$IDENTIFY_PARAMS"

GEOJSON='{"type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]}'

ZONAL_STATS_STATUS_CODE=$(curl -s -X POST \
	$ZONAL_STATS_ENDPOINT \
	-H 'Content-Type: application/json' \
	-d "$GEOJSON" \
	-o /dev/null \
	-w "%{http_code}" \
)

IDENTIFY_STATUS_CODE=$(curl -s \
	"$IDENTIFY_REQUEST" \
	-H 'Content-Type: application/json' \
	-o /dev/null \
	-w "%{http_code}" \
)

if [ "$IDENTIFY_STATUS_CODE" -ne "200" ]
then
echo "Identify request failed with status code $IDENTIFY_STATUS_CODE"
exit 1
fi

if [ "$ZONAL_STATS_STATUS_CODE" -ne "200" ]
then
echo "Zonal stats request failed with status code $ZONAL_STATS_STATUS_CODE"
exit 1
fi

exit 0
