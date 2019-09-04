# the geo json geometry object we got from geojson.io

# TO DO: This geojson will be to convert a in put param.
geo_json_geometry = {
    "type":"Polygon",
    "coordinates":[
     [
         [-72.991877930999976,1.9609552240000312],
		 [-72.991792826999983,2.088827664000064],
		 [-72.991702335999946,2.2166998910000757],
		 [-72.991648020999946,2.2900174120000543],
		 [-73.373025957999971,2.2902569450000669],
		 [-73.373061200999985,2.2169317480000359],
		 [-73.373119917999986,2.089046134000057],
		 [-73.500236779999966,2.0890982780000513],
		 [-73.563059456999952,2.0891202290000592],
		 [-73.563099789999967,1.9612298650000639],
		 [-73.500282037999966,1.9612092590000429],
		 [-73.500324430999967,1.8333200430000716],
		 [-73.500363962999984,1.7054306420000671],
		 [-73.246189733999984,1.7053370790000599],
		 [-73.246132795999984,1.8332194590000199],
		 [-73.246071736999966,1.9611016530000711],
		 [-73.118972456999984,1.9610332910000352],
		 [-72.991877930999976,1.9609552240000312]
		]
	]
}


# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2018-08-01T00:00:00.000Z",
    "lte": "2019-12-31T00:00:00.000Z"
  }
}

# filter any images which are more than 5% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.05
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
redding_reservoir = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}

very_large_search = {
  "name": "very_large_search",
  "item_types": ["PSScene4Band"],
  "filter": {
              "type": "AndFilter",
              "config": [geometry_filter, date_range_filter, cloud_cover_filter]
    }
}

FILE_IDS = r"./ids_list.txt"