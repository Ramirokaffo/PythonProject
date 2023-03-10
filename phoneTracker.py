import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium


# Trouver un pays

num = "+237672279946"
mon_num = phonenumbers.parse(num)

localisation = geocoder.description_for_number(mon_num, "fr")
print(localisation)
localisatio = geocoder.description_for_valid_number(mon_num, "fr")
print(localisatio)

operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))
print(carrier.safe_display_name(operateur, "fr"))

clef = "8f9e714f382b4f9aa5dbf4ae1638066e"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
for i in reponse:
    print(i["geometry"])
# print(len(reponse), reponse, )
# reponse[0].

lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]

print(lat)
print(lng)

# Creation du map
monMap = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map1.html")
print("ici")

# 4.6125522
# 13.1535811






