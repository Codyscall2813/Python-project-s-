import os
import requests
from bs4 import BeautifulSoup

# URL of the API
api_url = "https://savetik.co/api/ajaxSearch"

# Headers for the POST request
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://savetik.co',
    'Priority': 'u=1, i',
    'Referer': 'https://savetik.co/en2',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_video(user_input_link: str) -> str:
    """Fetch and return the 'Download MP4 HD' URL from the provided TikTok video URL."""
    data = {
        'q': user_input_link,
        'lang': 'en'
    }

    try:
        # Sending POST request to the URL
        response = requests.post(api_url, data=data, headers=headers)
        response.raise_for_status()

        # Parse HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags in the response
        all_links = soup.find_all('a')

        # Search for the download link containing 'Download MP4 HD' in the text or class
        download_link = None
        for link in all_links:
            if 'Download MP4 HD' in link.text or 'dl-success' in link.get('class', []):
                download_link = link.get('href')
                break

        if download_link:
            return download_link
        else:
            return None

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred while processing {user_input_link}: {http_err} - Status Code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as req_err:
        # Handle other request exceptions
        print(f"An error occurred while processing {user_input_link}: {req_err}")
        return None
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
        return None

def download_video(download_link: str, save_path: str):
    """Download the video from the given URL and save it to the specified path."""
    try:
        # Clean up download_link
        download_link = download_link.replace('\\"', '')

        # Download the video content
        response = requests.get(download_link)
        response.raise_for_status()

        # Save the video content to a file
        with open(save_path, 'wb') as f:
            f.write(response.content)

        print(f"Video downloaded successfully and saved at: {save_path}")

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred while downloading the video: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request exceptions
        print(f"An error occurred while downloading the video: {req_err}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred while downloading the video: {e}")

def main():
    """Main function to handle user input and download videos."""
    # Create the 'Tik_Saverrr' directory if it does not exist
    output_folder = "Tik_Saverrr"
    os.makedirs(output_folder, exist_ok=True)

    print("Welcome to the TikTok Video Downloader!")
    print("Enter TikTok video URLs to download videos.")
    print("Type 'exit' to quit.")

    count = 1
    while True:
        user_input_link = input("Enter TikTok URL: ").strip()
        if user_input_link.lower() == 'exit':
            break
        if user_input_link:
            download_link = get_video(user_input_link)
            if download_link:
                # Generate a filename based on the TikTok video ID or use a sequential number
                video_id = download_link.split('/')[-1].split('?')[0]  # Extract video ID from URL
                save_path = os.path.join(output_folder, f"{video_id}.mp4")
                download_video(download_link, save_path)
            else:
                print(f"Failed to fetch the download link for video: {user_input_link}")

if __name__ == "__main__":
    main()
