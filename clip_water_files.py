import geopandas as gpd
from shapely.geometry import box

# Define bounding box coordinates (minx, miny, maxx, maxy)
bbox_coords = (-47.0, -24.0, -46.0, -23.0)  # Example for São Paulo, Brazil

# Create the bounding box geometry
bbox = box(*bbox_coords)

# Load the waterways shapefile (modify the file path to your data)
waterways = gpd.read_file("data/sudeste-latest-free.shp/gis_osm_waterways_free_1.shp")
water = gpd.read_file("data/sudeste-latest-free.shp/gis_osm_water_a_free_1.shp")

# Clip the data using the bounding box
clipped_waterways = waterways.clip(bbox)
clipped_water = water.clip(bbox)

# Save the clipped data to a new shapefile
clipped_waterways.to_file("data/clipped_waterways.shp")
clipped_water.to_file("data/clipped_water.shp")

# Save to GeoJSON
clipped_waterways.to_file("data/clipped_waterways.geojson", driver="GeoJSON")
clipped_water.to_file("data/clipped_water.geojson", driver="GeoJSON")

print("Clipping completed successfully!")
