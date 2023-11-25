import unittest
from unittest.mock import patch, MagicMock
from geopy.geocoders import Nominatim
from helper import *


class TestAdresseEnCoordonnees(unittest.TestCase):
    @patch("geopy.geocoders.Nominatim.geocode")
    def test_adresse_en_coordonnees_with_location(self, mock_geocode):
        # Pour configurer le mock pour simuler un emplacement
        mock_location = MagicMock()
        mock_location.latitude = 40.7128
        mock_location.longitude = -74.0060
        mock_geocode.return_value = mock_location

        # Pour appeler la méthode avec une adresse fictive
        result = adresse_en_coordonnees("New York, USA")

        # Pour vérifier que la méthode geocode a été appelée avec l'adresse attendue
        mock_geocode.assert_called_once_with("New York, USA")

        # POur vérifier que le résultat correspond aux coordonnées simulées
        self.assertEqual(result, (40.7128, -74.0060))

    @patch("geopy.geocoders.Nominatim.geocode")
    def test_adresse_en_coordonnees_with_none_location(self, mock_geocode):
        mock_geocode.return_value = None

        result = adresse_en_coordonnees("Adresse inexistante")

        mock_geocode.assert_called_once_with("Adresse inexistante")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
