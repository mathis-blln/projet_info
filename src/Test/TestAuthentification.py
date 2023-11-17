from Classe.Authentification import Authentification
import unittest

class TestAuthentificationMethods(unittest.TestCase):
    def test_init(self):
        # Vérifie si l'initialisation de l'objet Authentification se déroule correctement
        auth = Authentification("utilisateur1", "123")
        self.assertEqual(auth._id_utilisateur, "utilisateur1")
        self.assertEqual(auth._mot_de_passe, "123")

    def test_compare(self):
        # Crée un objet Authentification pour les tests
        auth = Authentification("utilisateur1", "123")

        # Vérifie si la méthode compare fonctionne correctement pour des identifiants valides
        self.assertTrue(auth.compare("utilisateur1", "123"))

        # Vérifie si la méthode compare fonctionne correctement pour des identifiants invalides
        self.assertFalse(auth.compare("utilisateur2", "456"))

if __name__ == '__main__':
    unittest.main()