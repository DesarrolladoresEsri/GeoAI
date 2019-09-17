# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:14:04 2019

@author: wpineda
"""

#USE THIS: 
# python get_DOWNLOAD_API_PLANET_V2.py <<order_id>>

import os
import sys
import time
import json
from tqdm import tqdm

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
import requests

API_ENDPOINT = "https://api.planet.com/compute/ops/orders/v2/"
  
USER_NAME = "dfonseca@esri.co"
PASSWORD = "Nicolas2014"
try:
    order_id = sys.argv[1]
except: 
    print("You need put a valid order id")
r = requests.get(url = API_ENDPOINT + order_id, auth=(USER_NAME, PASSWORD)) 

path = order_id

access_rights = 0o755
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

results = r.json()['_links']['results']
start_time = time.time()
for r in tqdm(results):
    resp = requests.get(r['location'])
    with open(r'{}/{}'.format(path, os.path.basename(r['name'])), 'wb') as f:
        f.write(resp.content)
        f.close()
        
    print("Download {}".format(r['name']))
print("--- %s seconds ---" % (time.time() - start_time))