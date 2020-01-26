# import googlemaps

# gmaps_key = googlemaps.Client(key = "AIzaSyB0bPOg9jEX3s8c0QOcSDo3xN88L1HaKd8")

# geocode_result = gmaps_key.geocode("402 South Fifth Straeet, Champaign, IL")

# lat = geocode_result[0]["geometry"]["location"]["lat"]
# lng = geocode_result[0]["geometry"]["location"]["lng"]
# print("lat: " + str(lat))
# print("lng: " + str(lng))    

f = open("data.json", "r")
contents = f.read()
print(contents)