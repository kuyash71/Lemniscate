from src.core.models import Waypoint
from src.core.mission_formatter import parse_waypoints_file


def import_from_file(path: str) -> list[Waypoint]:
    return parse_waypoints_file(path)
