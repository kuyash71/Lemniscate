from src.core.models import MissionConfig


def parse_and_validate(
    center_lat: float,
    center_lon: float,
    altitude: float,
    semi_locus: float,
    orientation: float,
    n_waypoints: int,
    speed: float = 0.0,
) -> MissionConfig:

    # CENTER LAT
    if not isinstance(center_lat, (int,float)):
        raise TypeError("center_lat must be a number")
    if not -90 <= center_lat <= 90:
        raise ValueError("center_lat must be between -90 and 90")

    # CENTER LON
    if not isinstance(center_lon, (int,float)):
        raise TypeError("center_lon must be a number")
    if not -180 <= center_lon <= 180:
        raise ValueError("center_lon must be between -180 and 180")

    # ALTITUDE
    if not isinstance(altitude, (int,float)):
        raise TypeError("altitude must be a number")
    if 0<altitude<=10:
        pass
    elif not 10<=altitude:
        raise ValueError("altitude must be higher than 10")

    #  SEMI LOCUS
    if not isinstance(semi_locus, (int,float)):
        raise TypeError("semi_locus must be a number")
    if not 0<semi_locus:
        raise ValueError("semi_locus must be higher than 0")

    # ORIENTATION
    if not isinstance(orientation, (int, float)):
        raise TypeError("orientation must be a number")
    if not 0<=orientation<=360:
        orientation = orientation % 360

    # N WAYPOINTS
    if not isinstance(n_waypoints, int):
        raise TypeError("n_waypoints must be a number")
    if not 7<=n_waypoints:
        raise ValueError("n_waypoints must be higher than 6")

    # SPEED
    if not isinstance(speed, (int,float)):
        raise TypeError("speed must be a number")
    if 0>speed:
        raise ValueError("speed must be 0 or higher")

    return MissionConfig(center_lat, center_lon, altitude, semi_locus, orientation, n_waypoints, speed)