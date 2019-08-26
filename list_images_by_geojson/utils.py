from config import FILE_IDS

# What we want to do with each page of search results
# in this case, just print out each id
def handle_page(page):
    for item in page["features"]:
        print (item["id"])
        add_id_file(item["id"])

def add_id_file(image_id):
    file = open(FILE_IDS, "a")
    file.write(image_id + "\n")
    file.close()
    