# Programme utilisant la méthode REST API et le site Yelp Developper pour obtenir le nom des sallons de coiffures pour homme avec une note de plus de 4.5 à New York
# Nous avons en plus créé un fichier appelé Config.py pour y mettre notre API Key, de façon à ce que une fois notre code publiée et visible de tous, il soit plus sécurisé.

import requests
import Config

url = "https: // api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + Config.api_key
}
params = {
    "term": "Barber ",
    "location": "NYC"
}
response = requests.get(url, params=params, headers=headers)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
