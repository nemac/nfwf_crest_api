echo "Polygon test:"
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"type": "FeatureCollection","name": "test-ar","features": [{"type": "Feature","properties": {"id": null},"geometry": {"type": "Polygon","coordinates": [[[-80.01149654388428, 32.887677980874706],[-80.01911401748657, 32.88337138447869],[-80.01553058624268, 32.87764094428261],[-80.00417947769165, 32.882578515468],[-80.01149654388428, 32.887677980874706]]]}}]}' \
  http://localhost:3000/dev/zonal_stats?region=conus

echo "Multipolygon test:"
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"type": "FeatureCollection","name": "test-ar","features": [{"type": "Feature","properties": {"id": null},"geometry": {"type": "Polygon","coordinates": [[[-80.01149654388428, 32.887677980874706],[-80.01911401748657, 32.88337138447869],[-80.01553058624268, 32.87764094428261],[-80.00417947769165, 32.882578515468],[-80.01149654388428, 32.887677980874706]]]}}]}' \
  http://localhost:3000/dev/zonal_stats?region=conus


