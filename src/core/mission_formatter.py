from src.core.models import MissionConfig, Waypoint


def write_waypoints_file(
    waypoints: list[Waypoint],
    config: MissionConfig,
    output_path: str,
    include_takeoff: bool = True,
    include_rtl: bool = True,
) -> None:
    with open(output_path, "w") as f:
        f.write("QGC WPL 110\n")

        index = 0

        # Home
        home = waypoints[0]
        f.write(_row(index, 1, 0, 16, 0, 0, 0, 0, home.lat, home.lon, home.alt, 1))
        index += 1

        # Takeoff
        if include_takeoff:
            f.write(_row(index, 0, 3, 22, 0, 0, 0, 0, 0, 0, config.altitude, 1))
            index += 1

        # Waypoints
        for wp in waypoints:
            f.write(_row(index, 0, 3, 16, 0, 0, 0, 0, wp.lat, wp.lon, wp.alt, 1))
            index += 1

        # RTL
        if include_rtl:
            f.write(_row(index, 0, 3, 20, 0, 0, 0, 0, 0, 0, 0, 1))


def parse_waypoints_file(path: str) -> list[Waypoint]:
    waypoints = []
    with open(path) as f:
        lines = f.readlines()

    for line in lines[1:]:  # skip header
        parts = line.strip().split("\t")
        if len(parts) < 12:
            continue
        try:
            index = int(parts[0])
            command = int(parts[3])
            lat = float(parts[8])
            lon = float(parts[9])
            alt = float(parts[10])
            waypoints.append(Waypoint(index=index, lat=lat, lon=lon, alt=alt, command=command))
        except (ValueError, IndexError):
            continue

    return waypoints


def _row(*values) -> str:
    return "\t".join(str(v) for v in values) + "\n"
