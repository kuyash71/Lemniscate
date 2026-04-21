from dataclasses import dataclass


@dataclass
class MissionConfig:
    center_lat: float
    center_lon: float
    altitude: float
    semi_locus: float
    orientation: float
    n_waypoints: int
    speed: float = 0.0


@dataclass
class Waypoint:
    index: int
    lat: float
    lon: float
    alt: float
    command: int = 16
