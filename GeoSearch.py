from mapbox import Geocoder
import json

class GeoSearcher():
    def __init__(self):
        self.geocode = Geocoder(access_token='pk.eyJ1IjoianBmY2FicmFsIiwiYSI6ImNrcmo4ODVpejBpNmoybnFydnZ4aTBhajYifQ.XWYj4QQ5tXxiehs6ffR_Sg')
        self.check_test = self.geocode.forward('Natal, RN')
        print(self.check_test.status_code)

    
    def find(self, address):
        self.response = self.geocode.forward(address)
        self.lon, self.lat = self.response.geojson()['features'][0]['geometry']['coordinates']
        return self.lat, self.lon


# geocode = GeoCoordinates()
# print(geocode.find('Parnamirim, RN'))