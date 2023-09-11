import requests
import json 
url = "https://api.foursquare.com/v3/places/fsq_id/tips"
responses=input("enter -")
params = {
  	"query": responses,
  	#"ll": "47.606,-122.349358",
  	"open_now": "true",
  	"sort":"DISTANCE"
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3Z8BDCUNA1ElGQ22IuIBG0Uy0FRzrozsZOyG69/9t6zk="
}

response = requests.request("GET", url, params=params, headers=headers)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract and format specific information from the JSON
    formatted_text = ""
    for result in data.get("results", []):
        name = result.get("name", "N/A")
        address = result.get("location", {}).get("address", "N/A")
        formatted_text += f"Name: {name}\nAddress: {address}\n\n"

    # Print the formatted text
    print(formatted_text)
else:
    print(f"Error: HTTP status code {response.status_code}")