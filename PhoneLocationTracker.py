import phonenumbers
import opencage
import folium

from phonenumbers import geocoder

phoneNumber = input("Enter a number (including the International dialing code): ")

pepNumber = phonenumbers.parse(phoneNumber)
location = geocoder.description_for_number(pepNumber, "en")

print(location)

from phonenumbers import carrier

service_pro = phonenumbers.parse(phoneNumber)
service_pro_name = carrier.name_for_number(service_pro, "en")
print(service_pro_name)

from opencage.geocoder import OpenCageGeocode

#inorder to get your activation key simply create a profile on opencage 
key = "Put_your_activation_key_key"


geocoder = OpenCageGeocode(key)

query = str(location)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("Mylocation.html")
