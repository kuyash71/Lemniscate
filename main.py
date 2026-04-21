import argparse
import sys


def run_gui() -> None:
    from PyQt6.QtWidgets import QApplication
    from src.gui import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1280, 800)
    window.show()
    sys.exit(app.exec())


def run_cli(args) -> None:
    from src.core import parse_and_validate
    from src.core import generate_local_points
    from src.core import to_waypoints
    from src.core import write_waypoints_file

    config = parse_and_validate(
        center_lat=args.lat,
        center_lon=args.lon,
        altitude=args.altitude,
        semi_locus=args.semi_locus,
        orientation=args.orientation,
        n_waypoints=args.waypoints,
        speed=args.speed,
    )
    points = generate_local_points(config)
    waypoints = to_waypoints(points, config)
    write_waypoints_file(waypoints, config, args.output)
    print(f"Wrote {len(waypoints)} waypoints to {args.output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="LEMNISCATE waypoint generator")
    parser.add_argument("--no-gui", action="store_true")
    parser.add_argument("--lat", type=float)
    parser.add_argument("--lon", type=float)
    parser.add_argument("--altitude", type=float, default=30.0)
    parser.add_argument("--semi-locus", type=float, default=50.0)
    parser.add_argument("--orientation", type=float, default=0.0)
    parser.add_argument("--waypoints", type=int, default=36)
    parser.add_argument("--speed", type=float, default=0.0)
    parser.add_argument("--output", default="mission.waypoints")

    args = parser.parse_args()

    if args.no_gui:
        run_cli(args)
    else:
        run_gui()


if __name__ == "__main__":
    main()
