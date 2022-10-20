import requests

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area["ISO3166-1"="DE"][admin_level=2];
(node["amenity"="charging_station"](area);
 way["amenity"="charging_station"](area);
 rel["amenity"="charging_station"](area);
);
out center;
"""
response = requests.get(overpass_url, params={"data": overpass_query})
data = response.json()