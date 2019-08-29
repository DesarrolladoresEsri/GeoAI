from hard_downloader.config import IMAGE_LIST_FILE
from multiprocessing import Pool
from image_downloader_by_id.utils import download_by_id


def open_file():
    with open(IMAGE_LIST_FILE) as f:
        lines = f.read().splitlines()
        return lines


if __name__ == "__main__":
    ids = open_file()
# uncomment for multiproccessing
    with Pool(8) as p:
        print(p.map(download_by_id, ids))
# comment for multiprocesing
#    for image_id in ids:
#        download_by_id(image_id)
