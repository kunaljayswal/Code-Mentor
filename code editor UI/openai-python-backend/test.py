import requests

# Define the base URL of your Flask API
base_url = "http://localhost:5000"
# Define the endpoints you want to test
endpoints = ['/', '/juniorbot', '/taskmaster']

# Send GET requests to each endpoint and print the response
for endpoint in endpoints:
    url = base_url + endpoint
    response = requests.get(url)
    print(f'Request to {url}:')
    print(f'Status Code: {response.status_code}')
    print('Response Body:')
    print(response.text)
    print('\n')
