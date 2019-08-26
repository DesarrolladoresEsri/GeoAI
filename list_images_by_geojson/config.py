# the geo json geometry object we got from geojson.io

# TO DO: This geojson will be to convert a in put param.
geo_json_geometry = {
    "type":"Polygon",
    "coordinates":[
     [
         [-73.927989509808015,3.1662026886988701],
		 [-73.950574996438888,3.1031349719991721],
		 [-73.955131914306378,3.3547536756311795],
		 [-74.002771858434471,3.2179731605269755],
		 [-74.079589844096006,3.2645263665910993],
		 [-74.183156210690527,3.1365468292694869],
		 [-74.082557734551756,3.0195411415110334],
		 [-74.129123847687367,2.8332623070165157],
		 [-74.049660688789743,2.6299748230929509],
		 [-73.916140743100755,2.5100344280637379],
		 [-73.94019898829265,2.3042344029194353],
		 [-73.835015703611816,2.3231739759217218],
		 [-73.845678293318542,2.2350301478494203],
		 [-73.79535814556192,2.218857135874992],
		 [-73.74650793879033,2.4508480027524127],
		 [-73.681418300614041,2.3687331496370954],
		 [-73.529634164684921,2.3882857616998749],
		 [-73.51216799775483,2.3330752427513572],
		 [-73.442125497193899,2.3865842470867116],
		 [-73.437122004776654,2.3271249117086268],
		 [-73.35527196512902,2.3248227282097469],
		 [-72.934012295830769,2.4650284165469767],
		 [-72.920515791270702,2.5621777210405643],
		 [-72.819026670644291,2.6135248612971917],
		 [-73.249605823649802,2.7341768125198271],
		 [-73.387111268770013,2.8558897128458924],
		 [-73.40830666342174,2.7688811547503169],
		 [-73.854253248088867,2.7014854614958432],
		 [-73.809743050801103,2.8107132339360343],
		 [-73.880120050599828,2.8488545664912319],
		 [-73.927989509808015,3.1662026886988701]
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
    "gte": "2017-01-01T00:00:00.000Z",
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