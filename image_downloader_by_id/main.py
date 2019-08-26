# -*- coding: utf-8 -*-
import sys
import time
from utils import download_by_id

product_id = sys.argv[1]
#product_id = "20170102_143401_0e14" # in proccess order
#product_id = "20190821_145814_0f3f" # ok order

if __name__ == "__main__":
     start_time = time.time()
     try:
         if (product_id) is not None:
             download_by_id(product_id)
         else: 
             print("You need a valid id")
     except:
         print("You need pass a id parameter")        
     print("--- %s seconds ---" % (time.time() - start_time))
