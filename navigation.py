import requests
import json
import geocoder
from mapbox import Directions


mapbox_token = "pk.eyJ1IjoidmlzMDkiLCJhIjoiY2xnMG1lenY5MTB1dDNncXI1MHdya3IyNyJ9.4fNDqh2u7-EtRzPPZfyfIA"

start_location = "Chennai"
end_location = "Banglore"

start_l = geocoder.osm(start_location)
startt = start_l.lng, start_l.lat
start = ("{}".format(",".join(str(x) for x in startt)))
end_l = geocoder.osm(end_location)
endt = end_l.lng, end_l.lat
end = ("{}".format(",".join(str(y) for y in endt)))


url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{start};{end}?geometries=geojson&steps=true&access_token={mapbox_token}"
response = requests.get(url)
data = response.json()

shortest_route = min(data["routes"], key=lambda r: r["duration"])
coordinates = shortest_route["geometry"]
print(coordinates) 
instructions = []
for leg in shortest_route["legs"]:
    for step in leg["steps"]:
        instructions.append(step["maneuver"]["instruction"])
print("\n".join(instructions))  
