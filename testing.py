
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/Weezing")


if response.status_code == 200:
    data = json.loads(response.text)

    print(data['abilities'])
