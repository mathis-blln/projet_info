import unittest
from helper import *


class TestExtrairePremierElement(unittest.TestCase):
    """ne fonctionne pas encore"""

    def test_extraire_premier_element(self):
        # Test avec une liste non vide
        liste_non_vide = [[1, 2], [3, 4], [5, 6]]
        resultat_non_vide = extraire_premier_element(liste_non_vide)
        self.assertEqual(resultat_non_vide, [1, 3, 5])

        # Test avec une liste vide
        liste_vide = []
        resultat_vide = extraire_premier_element(liste_vide)
        self.assertEqual(resultat_vide, [])

        # Test avec des listes vides imbriquées
        liste_vide_imbriquee = [[], [], []]
        resultat_vide_imbriquee = extraire_premier_element(liste_vide_imbriquee)
        self.assertEqual(resultat_vide_imbriquee, [])

        # Test avec une sous-liste vide au milieu
        liste_avec_vide_interne = [[1, 2], [], [3, 4], [5, 6]]
        resultat_avec_vide_interne = extraire_premier_element(liste_avec_vide_interne)
        self.assertEqual(resultat_avec_vide_interne, [1, 3, 5])


if __name__ == "__main__":
    unittest.main()
