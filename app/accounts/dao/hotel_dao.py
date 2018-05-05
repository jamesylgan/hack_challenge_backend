from . import *
import requests

gkey = "AIzaSyC64ESM5aEpU3IL4tTSBTBXohAPIAe0p9M"

user_schema = UserSchema()
user_trip_schema = UserTripSchema()

def getCoords(city):
  url = "https://maps.googleapis.com/maps/api/geocode/json?address="+city+"&key="+gkey

  r = requests.get(url)
  
  for result in r.json['results']:
    # print result
    if "geometry" in result:
      geometry = result['geometry']
    else:
      geometry = None
    # print geometry
    if "location" in geometry:
      location = geometry['location']
    else:
      location = None
    # print location
    return str(location['lat']) + ',' + str(location['lng'])

# Some code taken from prior hackathon project: frlrm by Jordan Pizza, Kevin Yin, James Gan, Linh Vuu: https://github.com/kevinyin1/frlrm
def getNearby(city, searchType): 
  # City can be any address
  location = getCoords(city)
  # Default 10km
  distance = 10
  # call with "lodging" to find hotels, can also use for points of interest (send more than one keyword through searchType)
  # Google Places API Request pulls all hotels within 10km
  url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location+"&keyword=" + searchType + "&rankby=prominence&radius="+distance+"000&key="+gkey

  r = requests.get(url)
  
  response = []

  for result in r.json['results']:
    if "rating" in result:
      rating = result['rating']
    else:
      rating = None

    tempDict = {
      "name": result['name'].encode('utf-8'),
      "address": result['vicinity'],
      "rating": rating,
      "city": city
    }

    response.append(tempDict)

  for hotel in response:
    utils.commit_model(Hotel(response['name'], response['address'],
      response['rating'], response['city']))

  return response