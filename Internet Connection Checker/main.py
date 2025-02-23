import requests
from requests.exceptions import RequestException

def test_internet_connection():
    url = 'https://www.google.com/'
    print(f'Attempting to connect to {url} to determine internet connection status.\n')
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(f'Congratulations! You have active internet connection.')
        return True
    except RequestException:
        print(f'Your internet connection is not working!')
        return False

if __name__ == "__main__":
    test_internet_connection()
