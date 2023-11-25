import unittest
from Classe.Authentification import Authentification


class TestAuthentification(unittest.TestCase):
    def setUp(self):
        # Crée une instance d'Authentification avec des valeurs par défaut pour les tests
        self.auth = Authentification("utilisateur_test", "mot_de_passe_test")

    def test_compare_authentification_valide(self):
        result = self.auth.compare("utilisateur_test", "mot_de_passe_test")
        self.assertTrue(result)

    def test_compare_authentification_invalide_id_utilisateur(self):
        result = self.auth.compare("utilisateur_invalide", "mot_de_passe_test")
        self.assertFalse(result)

    def test_compare_authentification_invalide_mot_de_passe(self):
        result = self.auth.compare("utilisateur_test", "mot_de_passe_invalide")
        self.assertFalse(result)

    def test_compare_authentification_invalide_id_et_mot_de_passe(self):
        result = self.auth.compare("utilisateur_invalide", "mot_de_passe_invalide")
        self.assertFalse(result)

    def test_str_representation(self):
        expected_output = (
            "ID utilisateur: utilisateur_test, mot de passe : mot_de_passe_test"
        )
        self.assertEqual(str(self.auth), expected_output)


if __name__ == "__main__":
    unittest.main()
