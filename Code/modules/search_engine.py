# search_engine.py

import requests
from bs4 import BeautifulSoup

def search_external_sites(query):
    results = []

    # Define the websites to search
    sites = [
        {"name": "Stack Overflow", "url": "https://stackoverflow.com/search?q="},
        {"name": "W3Schools", "url": "https://www.w3schools.com/search/search.asp?q="},
        {"name": "Geeks for Geeks", "url": "https://www.geeksforgeeks.org/?s="},
        # Add more sites as needed
    ]

    # Iterate through each site and perform the search
    for site in sites:
        search_url = site["url"] + query
        response = requests.get(search_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information from the search results
            search_results = soup.find_all('div', {'class': 'question-summary'})

            for result in search_results:
                title = result.find('a', {'class': 'question-hyperlink'})
                link = title['href'] if title else None
                results.append({
                    "site": site["name"],
                    "title": title.text.strip() if title else None,
                    "link": link,
                })

    return results

# Example usage:
query = "Python exception handling"

search_results = search_external_sites(query)

for result in search_results:
    print(f"Site: {result['site']}")
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print("-" * 30)
