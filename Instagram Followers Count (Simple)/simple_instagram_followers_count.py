import requests
import time
import sys

# Function to fetch follower count from the third-party API


def fetch_follower_count(username):
    url = f"https://backend.mixerno.space/instagram/test/{username}"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "If-None-Match": 'W/"407-D+G+pbsC04ExhIFep0BY+psb5AY"',
        "Origin": "https://livecounts.nl",
        "Priority": "u=1, i",
        "Referer": "https://livecounts.nl/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

        # print(response.text, "\n")

        data = response.json()
        if 'user' in data and 'followerCount' in data['user']:
            follower_count = data['user']['followerCount']
            return follower_count
        else:
            print("Unexpected response format:", data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    return None

# Function to continuously update follower count in the terminal on the same line


def update_follower_count_to_terminal(username):
    while True:
        follower_count = fetch_follower_count(username)
        if follower_count is not None:
            sys.stdout.write(f"\rFollower Count: {follower_count}")
            sys.stdout.flush()
        else:
            sys.stdout.write("\rError fetching follower count")
            sys.stdout.flush()
        time.sleep(1)  # Update every 1 seconds


# Replace "pycode.hubb" with any other username
update_follower_count_to_terminal("pycode.hubb")
