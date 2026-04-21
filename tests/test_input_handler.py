import unittest
from src.core import parse_and_validate


class TestInputHandler(unittest.TestCase):

    def _valid(self, **kwargs):
        defaults = dict(
            center_lat=39.9, center_lon=32.8,
            altitude=30, semi_locus=50,
            orientation=0, n_waypoints=36,
        )
        defaults.update(kwargs)
        return parse_and_validate(**defaults)

    def test_valid_config_accepted(self):
        config = self._valid()
        self.assertEqual(config.n_waypoints, 36)

    def test_nonpositive_semi_locus_rejected(self):
        with self.assertRaises(ValueError):
            self._valid(semi_locus=0)

    def test_too_few_waypoints_rejected(self):
        with self.assertRaises(ValueError):
            self._valid(n_waypoints=3)

    def test_invalid_latitude_rejected(self):
        with self.assertRaises(ValueError):
            self._valid(center_lat=91.0)

    def test_invalid_longitude_rejected(self):
        with self.assertRaises(ValueError):
            self._valid(center_lon=181.0)


if __name__ == "__main__":
    unittest.main()
