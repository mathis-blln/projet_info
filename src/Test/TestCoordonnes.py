import unittest
from Classe.Coordonnees import Coordonnees


class TestCoordonnees(unittest.TestCase):
    def test_str_method(self):
        coord = Coordonnees(1, 12.9716, 77.5946)
        expected_output = (
            "la station 1 a pour coordonnees (latitude=12.9716, longitude=77.5946)"
        )
        self.assertEqual(str(coord), expected_output)

    def test_dist_method_same_point(self):
        coord1 = Coordonnees(1, 12.9716, 77.5946)
        coord2 = Coordonnees(2, 12.9716, 77.5946)
        distance = coord1.dist(coord2)
        self.assertEqual(
            distance, [1, 0]
        )  # La distance entre un point et lui-même est 0

    def test_dist_method_different_points(self):
        coord1 = Coordonnees(1, 12.9716, 77.5946)
        coord2 = Coordonnees(2, 28.6139, 77.2090)
        # Calcul de la distance approximative entre ces deux points en km
        distance_attendue = 1739.0
        resultat = coord1.dist(coord2)
        self.assertEqual(resultat[0], 1)  # Vérifie l'ID de la station
        self.assertAlmostEqual(resultat[1], distance_attendue, delta=1)


if __name__ == "__main__":
    unittest.main()
