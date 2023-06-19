import requests
import json

SHODAN_API_KEY = 'your_shodan_api_key'
ZOOMEYE_API_KEY = 'your_zoomeye_api_key'
CENSYS_API_ID = 'your_censys_api_id'
CENSYS_API_SECRET = 'your_censys_api_secret'

def search_shodan(query):
    shodan_url = f'https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}'
    response = requests.get(shodan_url)
    data = response.json()
    return data['matches']

def search_zoomeye(query):
    headers = {
        'API-KEY': ZOOMEYE_API_KEY,
    }
    zoomeye_url = f'https://api.zoomeye.org/host/search?query={query}'
    response = requests.get(zoomeye_url, headers=headers)
    data = response.json()
    return data['matches']

def search_censys(query):
    censys_url = 'https://censys.io/api/v1/search/ipv4'
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'query': query,
    }
    response = requests.post(censys_url, headers=headers, auth=(CENSYS_API_ID, CENSYS_API_SECRET), json=params)
    data = response.json()
    return data['results']

def main():
    query = input('[+] \033[34mEnter your query: \033[0m ')
    print('[~] \033[34mSearching Shodan... \033[0m ')
    shodan_results = search_shodan(query)
    print('[~] \033[34mSearching ZoomEye... \033[0m ')
    zoomeye_results = search_zoomeye(query)
    print('[~] \033[34mSearching Censys... \033[0m ')
    censys_results = search_censys(query)

    with open('results.txt', 'w') as f:
        f.write('Shodan Results:\n')
        f.write(json.dumps(shodan_results, indent=4))
        f.write('\nZoomEye Results:\n')
        f.write(json.dumps(zoomeye_results, indent=4))
        f.write('\nCensys Results:\n')
        f.write(json.dumps(censys_results, indent=4))
    print('[~] \033[34mFile results written \033[0m ')
if __name__ == '__main__':
    main()
