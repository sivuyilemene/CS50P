import sys
import requests
import json
# get input from user
if len(sys.argv) != 2:
    sys.exit()
# send a request to itunes
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=3&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
# display the tracks
for result in o["results"]: 
    print(result["trackName"])
