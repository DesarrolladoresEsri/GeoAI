import time
from hard_downloader.config import IMAGE_LIST_FILE
from multiprocessing import Pool
from image_downloader_by_id.utils import download_by_id


def open_file():
    with open(IMAGE_LIST_FILE) as f:
        lines = f.read().splitlines()
        return lines


if __name__ == "__main__":
    start_time = time.time() 
    ids = open_file()
# uncomment for multiproccessing
    with Pool(4) as p:
        print(p.map(download_by_id, ids))
# comment for multiprocesing
#    for image_id in ids:
#        download_by_id(image_id)
    log = open(r"run.log", "w")
    log.write("--- %s seconds ---" % (time.time() - start_time))
    log.close()
    print("--- %s seconds ---" % (time.time() - start_time))