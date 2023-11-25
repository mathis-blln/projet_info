import unittest
from unittest.mock import patch
from Services.inscription import Inscription
from DAO.inscriptionDAO import InscriptionDAO


class TestInscription(unittest.TestCase):
    @patch("DAO.inscriptionDAO.InscriptionDAO")
    def test_inscrire(self, mock_inscription_dao):
        # POUR Configurer le mock pour simuler l'ajout d'un utilisateur
        utilisateur_id = 123
        utilisateur_nom = "UtilisateurTest"
        utilisateur_mdp = "MotDePasseTest"
        mock_inscription_dao.return_value = InscriptionDAO()

        # POUR Créer une instance de Inscription
        inscription = Inscription()

        # POUR Capturer la sortie imprimée lors de l'appel à la méthode inscrire
        with patch("builtins.print") as mock_print:
            inscription.inscrire(utilisateur_nom, utilisateur_mdp)

        # Pour vérifier que la méthode add_user a été appelée avec les bons arguments
        mock_inscription_dao.return_value.add_user.assert_called_once_with(
            utilisateur_nom, utilisateur_mdp
        )

        # Pour Vérifier que les arguments de add_user sont des instances de str
        self.assertIsInstance(
            mock_inscription_dao.return_value.add_user.call_args[0][0], str
        )
        self.assertIsInstance(
            mock_inscription_dao.return_value.add_user.call_args[0][1], str
        )

        # Pour Vérifier que la sortie imprimée correspond à ce qui est attendu
        expected_output = (
            "-----------------------------------\n"
            "Bienvenue.\nVos identifiants\n"
            f"ID: {utilisateur_id}\nNom: {utilisateur_nom}\nPassword: {utilisateur_mdp}.\n"
            "-----------------------------------"
        )
        mock_print.assert_called_once_with(expected_output)


if __name__ == "__main__":
    unittest.main()
