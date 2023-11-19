from geopy.geocoders import Nominatim


def adresse_en_coordonnees(adresse):
    geolocator = Nominatim(
        user_agent="géoloc"
    )  # Remplacez "myGeocoder" par votre propre nom d'utilisateur.

    location = geolocator.geocode(adresse)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None


print(adresse_en_coordonnees("3 rue de la fontaine saint martin, Soignolles-en-Brie"))
