import unittest
from Classe.Coordonnees import Coordonnees

class TestCoordonnees(unittest.TestCase):
    def test_dist_entre_meme_point(self):
        # Teste si la distance entre un point et lui-même est 0
        coord = Coordonnees(12.9716, 77.5946)
        resultat = coord.dist(coord)
        self.assertEqual(resultat, 0)

    def test_dist_entre_deux_points_identiques(self):
        # Teste si la distance entre deux points identiques est 0
        coord1 = Coordonnees(12.9716, 77.5946)
        coord2 = Coordonnees(12.9716, 77.5946)
        resultat = coord1.dist(coord2)
        self.assertEqual(resultat, 0)

    def test_dist_entre_deux_points_differents(self):
        # Teste la distance entre deux points différents
        coord1 = Coordonnees(12.9716, 77.5946)
        coord2 = Coordonnees(28.6139, 77.2090)
        # Calcul de la distance approximative entre ces deux points en km
        distance_attendue = 1739.0
        resultat = round(coord1.dist(coord2))
        self.assertAlmostEqual(resultat, distance_attendue, delta=1)

if __name__ == '__main__':
    unittest.main()