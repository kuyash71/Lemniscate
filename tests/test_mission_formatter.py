import unittest
import os
import tempfile
from src.core import MissionConfig, Waypoint
from src.core import write_waypoints_file, parse_waypoints_file


class TestMissionFormatter(unittest.TestCase):

    def _config(self):
        return MissionConfig(
            center_lat=39.9, center_lon=32.8,
            altitude=30, semi_locus=50,
            orientation=0, n_waypoints=4,
        )

    def _waypoints(self):
        return [
            Waypoint(index=i, lat=39.9 + i * 0.001, lon=32.8 + i * 0.001, alt=30)
            for i in range(4)
        ]

    def test_roundtrip(self):
        with tempfile.NamedTemporaryFile(suffix=".waypoints", delete=False) as f:
            path = f.name
        try:
            write_waypoints_file(self._waypoints(), self._config(), path,
                                 include_takeoff=False, include_rtl=False)
            parsed = parse_waypoints_file(path)
            self.assertEqual(len(parsed), 4)
            self.assertAlmostEqual(parsed[0].lat, 39.9, places=5)
        finally:
            os.unlink(path)

    def test_header_written(self):
        with tempfile.NamedTemporaryFile(suffix=".waypoints", delete=False, mode="w") as f:
            path = f.name
        try:
            write_waypoints_file(self._waypoints(), self._config(), path)
            with open(path) as f:
                self.assertTrue(f.readline().startswith("QGC WPL"))
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
