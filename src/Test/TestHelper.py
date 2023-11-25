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

    def test_trier(self):
        # Test avec une liste non vide
        liste_non_vide = [[1, 5], [3, 2], [5, 8]]
        resultat_non_vide = trier(liste_non_vide)
        self.assertEqual(resultat_non_vide, [[3, 2], [1, 5], [5, 8]])

        # Test avec une liste vide
        liste_vide = []
        resultat_vide = trier(liste_vide)
        self.assertEqual(resultat_vide, [])

    def test_selectionner_n_premiers(self):
        # Test avec une liste non vide
        liste_non_vide = [[1, 5], [3, 2], [5, 8], [7, 1]]
        resultat_non_vide = selectionner_n_premiers(2, liste_non_vide)
        self.assertEqual(resultat_non_vide, [[1, 5], [3, 2]])

    def test_split_input_with_elements(self):
        # Test avec une chaîne non vide contenant des éléments séparés par des virgules
        input_with_elements = "apple,banana,orange"
        result_with_elements = split_input(input_with_elements)
        self.assertEqual(result_with_elements, ["apple", "banana", "orange"])


if __name__ == "__main__":
    unittest.main()
