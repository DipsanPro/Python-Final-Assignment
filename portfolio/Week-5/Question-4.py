#program that takes a URL as a command-line argument and reports
#whethe or not there is a working website at that address

#TO RUN THIS PROGRAMME: INSTALL requests PACKAGE

import sys
import requests

url = sys.argv[1] if len(sys.argv) > 1 else None
if url:
    try:
        response = requests.get(url)
        print("The website is working." if response.status_code == 200 else f"Status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print("The website is not working.")
else:
    print("Please provide a URL as a command-line argument.")