import unittest
from src.core import MissionConfig
from src.core import generate_local_points


class TestLemniscateEngine(unittest.TestCase):

    def _config(self, **kwargs):
        defaults = dict(
            center_lat=39.9, center_lon=32.8,
            altitude=30, semi_locus=50,
            orientation=0, n_waypoints=36,
        )
        defaults.update(kwargs)
        return MissionConfig(**defaults)

    def test_point_count(self):
        points = generate_local_points(self._config(n_waypoints=36))
        self.assertEqual(len(points), 36)

    def test_origin_symmetry(self):
        points = generate_local_points(self._config(n_waypoints=36))
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        self.assertAlmostEqual(sum(xs) / len(xs), 0.0, places=6)
        self.assertAlmostEqual(sum(ys) / len(ys), 0.0, places=6)

    def test_scale(self):
        points = generate_local_points(self._config(semi_locus=100, n_waypoints=360))
        max_x = max(abs(p[0]) for p in points)
        self.assertAlmostEqual(max_x, 100.0, delta=0.5)


if __name__ == "__main__":
    unittest.main()
