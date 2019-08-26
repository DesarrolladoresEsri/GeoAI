import os
import requests
from config import very_large_search
from utils import handle_page
import time

if __name__ == "__main__":
    start_time = time.time()
    session = requests.Session()
    session.auth = (os.environ['PL_API_KEY'], '')
    
    # Create a Saved Search
    saved_search = \
        session.post(
            'https://api.planet.com/data/v1/searches/',
            json=very_large_search)
            
    # after you create a search, save the id. This is what is needed
    # to execute the search.
    saved_search_id = saved_search.json()["id"]
        
    # How to Paginate:
    # 1) Request a page of search results
    # 2) do sa+omething with the page of results
    # 3) if there is more data, recurse and call this method on the next page.
    def fetch_page(search_url):
        page = session.get(search_url).json()
        handle_page(page)
        next_url = page["_links"].get("_next")
        if next_url:
            fetch_page(next_url)
            
    first_page = \
        ("https://api.planet.com/data/v1/searches/{}" +
            "/results?_page_size={}").format(saved_search_id, 5)
        
    fetch_page(first_page)
    print("--- %s seconds ---" % (time.time() - start_time))