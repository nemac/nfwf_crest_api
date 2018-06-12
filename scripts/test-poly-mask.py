with fiona.open("./assets/charleston-poly.geojson", "r") as shapefile:
    features = [feature["geometry"] for feature in shapefile]

with rasterio.open("./assets/SA_ExposureIndex_Charleston.tif") as src:
  out_image, out_transform = rasterio.mask.mask(src, features, crop=True)
  out_meta = src.meta.copy()

out_meta.update({
  "driver": "GTiff",
  "height": out_image.shape[1],
  "width": out_image.shape[2],
  "transform": out_transform
})

with rasterio.open("./assets/charleston_exposure_index.byte.masked.tif", "w", **out_meta) as dest:
  dest.write(out_image)
