import requests
import sys
import time

# API endpoint URL
url = "https://mixerno.space/api/youtube-channel-counter/user/UCX6OQ3DkcsbYNE6H8uQQuVA"

# Custom headers
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "If-None-Match": 'W/"407-D+G+pbsC04ExhIFep0BY+psb5AY"',
    "Origin": "https://livecounts.nl",
    "Referer": "https://livecounts.nl/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


def fetch_subscriber_count():
    try:
        # Send GET request with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # print(response.text)
        data = response.json()  # Parse JSON response
        # Extract subscriber count
        subscriber_count = None
        for item in data.get('counts', []):
            if item['value'] == 'subscribers':
                subscriber_count = item['count']
                break

        if subscriber_count is not None:
            return subscriber_count
        else:
            return "Subscriber count not found"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def main():
    try:
        # Initial fetch
        prev_count = fetch_subscriber_count()
        if prev_count is None:
            sys.exit(1)

        while True:
            # Fetch current count
            current_count = fetch_subscriber_count()

            if current_count is None:
                break

            # Display only when count changes
            if current_count != prev_count:
                # Print on the same line with carriage return
                sys.stdout.write(
                    f"\rCurrent subscriber count: {current_count}")
                sys.stdout.flush()
                prev_count = current_count

            time.sleep(2)  # Wait for 2 seconds before next request

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
