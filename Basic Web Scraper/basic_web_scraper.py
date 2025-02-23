import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the web page. Status code: {
              response.status_code}")
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for item in soup.find_all('div', class_='row test-site'):
        title_element = item.find('h2', class_='site-heading')
        description_element = item.find('p', class_='lead')

        if title_element and description_element:
            title = title_element.text.strip()
            description = description_element.text.strip()
            data.append({'title': title, 'description': description})
    return data


def main():
    url = 'https://webscraper.io/test-sites'
    html = fetch_page(url)
    if html:
        data = parse_html(html)
        for entry in data:
            print(f"Title: {entry['title']}")
            print(f"Description: {entry['description']}")
            print('---')


if __name__ == '__main__':
    main()
