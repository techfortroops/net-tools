import logging, requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logging.basicConfig(level = logging.DEBUG)

session = requests.Session()

# retries on basic connectivity issues (including DNS lookup failures) and HTTP status codes of 502, 503 and 504
retries = Retry(total = 5, backoff_factor = 1, status_forcelist = [502, 503, 504])

responsive_addrs = []
non_responsive_addrs = []

test_addrs = ["http://stackoverflow.com", "http://www.google.com/nothere", "http://httpstat.us/503", "https://httpbin.org/status/404"]

for url in test_addrs:
    session.mount(url, HTTPAdapter(max_retries = retries))

    try:
        request = session.get(url, timeout = 3, stream = True)
        print(f"URL Redirected to: {request.url}")
        print(f"Response Status Code: {request.status_code}")
        print(f"Response Cookies: {request.cookies}")
        print(f"Response Encoding: {request.encoding}")
        print(f"Raw Response: {request.raw}")
        print(f"First 10 Bytes: {request.raw.read(10)}")
        print(f"\nResponse Headers: {request.headers}")
        # print(request.text)
        if (str(request.status_code) == "200"):
            responsive_addrs.append(url)
        else:
            non_responsive_addrs.append(url)
        request.raise_for_status()  

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh)
    
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    
    except requests.exceptions.TooManyRedirects:
        print("URL bad with too many redirects. Try a different one!")
    
    except requests.exceptions.RequestException as err:
        print ("Oops: Error is not clear!", err)

print(f"Responsive Addresses: {responsive_addrs}")
print(f"Non Responsive Addresses: {non_responsive_addrs}")