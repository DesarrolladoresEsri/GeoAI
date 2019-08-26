# -*- coding: utf-8 -*-
import time
from planet import api
from config import PRODUCTS, ITEM_TYPE, DOWNLOAD_LOCATION
client = api.ClientV1()

def download_by_id(item_id):
    # activate assets
    assets = client.get_assets_by_id(ITEM_TYPE, item_id).get()
    
    for product in PRODUCTS:
        try:
            client.activate(assets["{}".format(product)])
        except:
            print("The Product {} isn't avaible for id: {}".format(product,item_id))
            next
    
    # wait until activation completes
    while True:
        assets = client.get_assets_by_id(ITEM_TYPE, item_id).get()
        for product in PRODUCTS:
            if 'location' in assets["{}".format(product)]:
                    break
            print("Waiting for the order to be available...")
            #time.sleep(10)
            print("Trying again...")
        
    for product in PRODUCTS:
        cd = client.download(assets[product], callback=api.write_to_file(DOWNLOAD_LOCATION))
        file = cd.get_body().name
        print("{}: {}".format(product, file))
