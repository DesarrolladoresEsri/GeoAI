# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:43:39 2019

@author: wpineda
"""
import sys
import time
import json
import requests

#USE THIS: 
# python post_API_PLANET_V2.py id_list.txt

API_ENDPOINT = "https://api.planet.com/compute/ops/orders/v2"
  
USER_NAME = "dfonseca@esri.co"
PASSWORD = "Nicolas2014"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def make_ids_list(file):
    file = open(file, 'r')
    lines = file.readlines()
    return [','.join(lines[i:i + 3]) for i in range(0, len(lines), 3)]
    

def make_order(ids):
    
    data = {  
       "name":"New simple order",
       "subscription_id": 299492,
       "products":[
          {  
             "item_ids": ids.replace("\n",'').split(",")
             ,
             "item_type":"PSScene4Band",
             "product_bundle":"analytic_sr_udm2"
          }
       ],
       "notifications":{  
          "email": True
       }
    }
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data), auth=(USER_NAME, PASSWORD), headers=headers ) 
    if r.status_code == 202:
        print(json.dumps(data))
        order_id = r.json()['id']    
        print("Order id :{}".format(order_id))
        gen_ords = open('orders.log', 'a')
        gen_ords.write(order_id + '\n')
        time.sleep(60)
    else:
        print("Bad response, with status {}".format(r.status_code))
        print("Cause By: {}".format(r.json()['field']))

if __name__ == "__main__" and __package__ is None:
    start_time = time.time()
    file = sys.argv[1] 
    id_groups = make_ids_list(file)
    for ids in id_groups:
        make_order(ids)
    
    print("--- %s seconds ---" % (time.time() - start_time))