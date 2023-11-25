import unittest
from Classe.Coordonnees import Coordonnees


class TestCoordonnees(unittest.TestCase):
    def test_str_method(self):
        coord = Coordonnees(1, 40.7128, -74.0060, "New York")
        expected_output = (
            "la station 1 a pour coordonnees (latitude=40.7128, longitude=-74.006)"
        )
        self.assertEqual(str(coord), expected_output)

    def test_dist_method_same_point(self):
        coord1 = Coordonnees(1, 40.7128, -74.0060, "New York")
        coord2 = Coordonnees(2, 40.7128, -74.0060, "New York")
        distance = coord1.dist(coord2)
        self.assertEqual(distance, [1, 0])

    def test_dist_method_different_points(self):
        coord1 = Coordonnees(1, 40.7128, -74.0060, "New York")
        coord2 = Coordonnees(2, 34.0522, -118.2437, "Los Angeles")

        expected_distance = 3935.0
        result = coord1.dist(coord2)
        self.assertEqual(result[0], 1)
        self.assertAlmostEqual(result[1], expected_distance, delta=1)


if __name__ == "__main__":
    unittest.main()
