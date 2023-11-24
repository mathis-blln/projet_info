import unittest
from unittest.mock import MagicMock, patch
from DAO.stationDAO import StationDAO


class TestStationDAO(unittest.TestCase):
    @patch("DAO.stationDAO.DBConnection")
    def test_add_id_station(self, mock_DBConnection):
        # Créez une instance de StationDAO
        dao = StationDAO()

        # Mock de la connexion à la base de données
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_DBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Définir le résultat attendu
        expected_result = {"id_liste": 1, "id_stations": 42}
        mock_cursor.fetchone.return_value = expected_result

        # Appeler la méthode à tester
        result = dao.add_id_station(id_liste=1, id_stations=42)

        # Vérifier que la méthode execute a été appelée avec les bons arguments
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO projet.contenu_liste (id_liste, id_stations)"
            "VALUES (%(id_liste)s, %(id_stations)s)"
            "RETURNING id_liste, id_stations",
            {"id_liste": 1, "id_stations": 42},
        )

        # Vérifier que la méthode fetchone a été appelée
        mock_cursor.fetchone.assert_called_once()

        # Vérifier que le résultat de la méthode est correct
        self.assertEqual(result, [1, 42])

    @patch("DAO.stationDAO.DBConnection")
    def test_remove_id_station(self, mock_DBConnection):
        # Créez une instance de StationDAO
        dao = StationDAO()

        # Mock de la connexion à la base de données
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_DBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Appeler la méthode à tester
        dao.remove_id_station(id_liste=1, id_stations=42)

        # Vérifier que la méthode execute a été appelée avec les bons arguments
        mock_cursor.execute.assert_called_once_with(
            "DELETE FROM projet.contenu_liste "
            "WHERE id_liste = %(id_liste)s AND id_stations = %(id_stations)s",
            {"id_liste": 1, "id_stations": 42},
        )

        # Vérifier que la méthode commit a été appelée
        mock_connection.commit.assert_called_once()

    @patch("DAO.stationDAO.DBConnection")
    def test_get_id_stations_from_liste(self, mock_DBConnection):
        # Créez une instance de StationDAO
        dao = StationDAO()

        # Mock de la connexion à la base de données
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_DBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Définir le résultat attendu
        expected_result = [{"id_stations": 42}, {"id_stations": 43}]
        mock_cursor.fetchall.return_value = expected_result

        # Appeler la méthode à tester
        result = dao.get_id_stations_from_liste(id_liste=1)

        # Vérifier que la méthode execute a été appelée avec les bons arguments
        mock_cursor.execute.assert_called_once_with(
            "SELECT id_stations FROM projet.contenu_liste WHERE id_liste = %(id_liste)s",
            {"id_liste": 1},
        )

        # Vérifier que la méthode fetchall a été appelée
        mock_cursor.fetchall.assert_called_once()

        # Vérifier que le résultat de la méthode est correct
        self.assertEqual(result, [42, 43])


if __name__ == "__main__":
    unittest.main()
