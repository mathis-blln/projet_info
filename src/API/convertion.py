from geopy.geocoders import Nominatim


def adresse_en_coordonnees(adresse):
    geolocator = Nominatim(user_agent="géoloc")  # Remplacez "myGeocoder" par votre propre nom d'utilisateur.

    location = geolocator.geocode(adresse)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None
adresse_en_coordonnees("rue jules vernes, Langueux")

