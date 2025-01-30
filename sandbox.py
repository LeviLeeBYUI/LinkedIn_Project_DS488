import requests

api_key = '2iwJv-dLMFGJjKuquz7FNA'
headears = {'Authorization': 'Bearer' + api_key}

api_endpoint = 'https://nubela.co/proxycurl/api/search/linkedin'

params = {
    'query': "Brigham Young University-Idaho",
    'limit': 10
}

response = requests.get(api_endpoint, params=params, headers=headears)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")