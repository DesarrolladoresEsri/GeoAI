# -*- coding: utf-8 -*-

from planet import api
from .config import PRODUCTS, ITEM_TYPE, DOWNLOAD_LOCATION, LOG_IMAGES
import os
import requests
import sys
import time
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
client = api.ClientV1()
session = requests.Session()
session.auth = (os.environ['PL_API_KEY'], '')


def download_by_id(item_id):
    PATH_RESULT = os.path.join(DOWNLOAD_LOCATION, item_id)
    if not os.path.exists(PATH_RESULT):
        os.makedirs(PATH_RESULT)
    # activate assets
    print("Downloading product id {}".format(item_id))
    assets = client.get_assets_by_id(ITEM_TYPE, item_id).get()

    for product in PRODUCTS:
        try:
            client.activate(assets["{}".format(product)])
        except:
            print("The Product {} isn't avaible for id: {}".format(product, item_id))
            next

    # wait until activation completes
    while True:
        assets = client.get_assets_by_id(ITEM_TYPE, item_id).get()
        if all(['location' in assets["{}".format(product)] for product in PRODUCTS]):
            break
        print("Waiting for the order to be available...")
        time.sleep(10)
        print("Trying again...")

    # Download product.
    for product in PRODUCTS:
        cd = client.download(assets[product],
                             callback=api.write_to_file(PATH_RESULT))
        file_name = cd.get_body().name
        print("{}: {}".format(product, file_name))
        file = open(LOG_IMAGES, "a")
        file.write(file_name + "\n")
        file.close()
    print("Finish, all is ok!!!")
