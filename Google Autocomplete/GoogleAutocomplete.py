import json
import requests

def get_search_suggestions(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15"
    }

    try:
        response = requests.get(f'http://google.com/complete/search?client=chrome&q={query}', headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Print the full response to see what we get
        #print("Full response:")
        #print(response.text)

        suggestions = json.loads(response.text)[1]
        if suggestions:
            for suggestion in suggestions:
                print(suggestion)
        else:
            print("No suggestions found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

while True:
    completion_query = input("Enter Search: ")
    get_search_suggestions(completion_query)
    
    continue_search = input("\nDo you want to search again? (yes/no): ").strip().lower()
    if continue_search != 'yes':
        print("Goodbye!")
        break
