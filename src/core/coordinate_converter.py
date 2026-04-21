import math

from src.core.models import MissionConfig, Waypoint


def to_waypoints(
    local_points: list[tuple[float, float]],
    config: MissionConfig,
) -> list[Waypoint]:

    waypoints = []
    center_lat = config.center_lat
    center_lon = config.center_lon
    R = 6_371_000

    for i in range(len(local_points)):
        lat = center_lat + (local_points[i][1] / R) * (180/math.pi)
        lon = center_lon + (local_points[i][0] / (R * math.cos(math.radians(center_lat)))) * (180/math.pi)
        waypoints.append(Waypoint(i, lat, lon, config.altitude))
    return waypoints

