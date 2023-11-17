import unittest
from Classe.Station import Station

class TestStationMethods(unittest.TestCase):
    def setUp(self):
        # Crée une nouvelle instance de Station avant chaque test
        self.station = Station(
            id_station=1,
            longitude=10.1234,
            latitude=20.5678,
            ville="Ville1",
            adresse="Adresse1",
            type_carburant="Essence",
            prix_carburant=2.5,
            coordonnees="(10.1234, 20.5678)"
        )
        self.station.ajouter_service("Lavage de voiture")
        self.station.ajouter_service("Réparation mécanique")

    def test_ajouter_service(self):
        # Vérifie si le service est correctement ajouté
        self.assertIn("Lavage de voiture", self.station.services)
        self.assertIn("Réparation mécanique", self.station.services)

    def test_service_disponible(self):
        # Vérifie si les services ajoutés sont disponibles
        self.assertTrue(self.station.service_disponible("Lavage de voiture"))
        self.assertTrue(self.station.service_disponible("Réparation mécanique"))

        # Vérifie un service qui n'a pas été ajouté
        self.assertFalse(self.station.service_disponible("Service inexistant"))

if __name__ == '__main__':
    unittest.main()