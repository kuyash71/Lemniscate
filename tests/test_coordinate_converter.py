import unittest
from src.core import MissionConfig
from src.core import to_waypoints


class TestCoordinateConverter(unittest.TestCase):

    def _config(self):
        return MissionConfig(
            center_lat=39.9, center_lon=32.8,
            altitude=30, semi_locus=50,
            orientation=0, n_waypoints=4,
        )

    def test_center_point_unchanged(self):
        waypoints = to_waypoints([(0.0, 0.0)], self._config())
        self.assertAlmostEqual(waypoints[0].lat, 39.9, places=5)
        self.assertAlmostEqual(waypoints[0].lon, 32.8, places=5)

    def test_altitude_preserved(self):
        waypoints = to_waypoints([(10.0, 0.0)], self._config())
        self.assertEqual(waypoints[0].alt, 30)

    def test_east_offset_increases_lon(self):
        waypoints = to_waypoints([(100.0, 0.0)], self._config())
        self.assertGreater(waypoints[0].lon, 32.8)

    def test_north_offset_increases_lat(self):
        waypoints = to_waypoints([(0.0, 100.0)], self._config())
        self.assertGreater(waypoints[0].lat, 39.9)


if __name__ == "__main__":
    unittest.main()
