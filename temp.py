#GET https://api.spacexdata.com/v5/launches/latest
import requests

response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
response.raise_for_status()
print(response.json()['id'])
[print(link) for  link in response.json()['links']['flickr']['original']]


