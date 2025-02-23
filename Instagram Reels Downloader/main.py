import requests
from bs4 import BeautifulSoup
import os

# URL of the API to fetch Instagram media details
igdownloader_url = "https://igdownloader.app/api/ajaxSearch"

# Headers for the POST request
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://igdownloader.app',
    'Priority': 'u=1, i',
    'Referer': 'https://igdownloader.app/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

def get_vid(user_input_link, count):
    """Fetch and download the video from the provided Instagram URL."""
    data = {
        'q': user_input_link,  # Instagram post URL
        't': 'media',  # Type of content to fetch
        'lang': 'en'   # Language
    }

    try:
        # Sending POST request to the URL
        response = requests.post(igdownloader_url, data=data, headers=headers)
        response.raise_for_status() 

        # Load the HTML content of the response
        soup = BeautifulSoup(response.json()['data'], 'html.parser')

        # Find the download link for the media
        download_link = soup.select_one('.download-items .download-items__btn a')['href']

        # Download the video file
        video_response = requests.get(download_link)
        video_response.raise_for_status()

        # Save the video to a file with a unique name
        filename = os.path.join('downloaded_reels', f'reel_{count}.mp4')
        with open(filename, 'wb') as file:
            file.write(video_response.content)
        print(f"Video downloaded successfully: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while processing {user_input_link}: {e}")

def main():
    """Main function to handle user input and download videos."""
    # Create the 'downloaded_reels' directory if it does not exist
    os.makedirs('downloaded_reels', exist_ok=True)

    print("Welcome to the Instagram Video Downloader!")
    print("Enter Instagram post URLs to download videos.")
    print("Type 'exit' to quit.")

    count = 1
    while True:
        user_input_link = input("Enter Instagram URL: ").strip()
        if user_input_link.lower() == 'exit':
            break
        if user_input_link:
            get_vid(user_input_link, count)
            count += 1

if __name__ == "__main__":
    main()
