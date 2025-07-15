import requests 
from requests.exceptions import HTTPError

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as err:
        print(f"Other Exception occured: {err}")
    else:
        print("Success!")