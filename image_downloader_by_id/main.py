# -*- coding: utf-8 -*-
import time
from utils import download_by_id

if __name__ == "__main__":
     start_time = time.time()
     download_by_id("20170102_143401_0e14")
     print("--- %s seconds ---" % (time.time() - start_time))
    
