

import rasterio as rio

coords = [ (1745727, 451980) ]

bands = (1, 2)

with rio.open("s3://nfwf-tool/NA_AssetThreatIndexAsBands.tif") as src:

	for s in src.sample(coords, bands):
		print(s)

