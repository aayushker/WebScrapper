import requests

api_url = "https://example.com/api/data"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(api_url, headers=headers)
data = response.json()  # If it's JSON response
print(data)
