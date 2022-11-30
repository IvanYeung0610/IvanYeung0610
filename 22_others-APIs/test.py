import requests

#The Metropolitian Museum of Art Collection API

object_id = "488690"
MET_API = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + object_id

# r = requests.get(MET_API)
# dict = r.json()
#print(dict["accessionNumber"])

anime =  "naruto"
anime_chan_url = "https://animechan.vercel.app/api/random/character?name=naruto"

r = requests.get(anime_chan_url)
print(r.json()["0"])
