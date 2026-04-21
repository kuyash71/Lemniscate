<p align="center">
  <img src="assets/banner.png" alt="LEMNISCATE banner">
</p>

# LEMNISCATE

A waypoint generator for ArduPilot Mission Planner that computes the flight path for a drone to trace an infinity (∞) symbol.

Given a set of mission parameters, LEMNISCATE produces a `.waypoints` file ready to import into Mission Planner. Developed for the SAÜRO UAV Team as part of the 2025/2026 Teknofest Rotary Wing UAV competition.

## Features

- Mathematically precise Bernoulli lemniscate parametric computation
- Configurable center point, scale, orientation, altitude, and waypoint density
- Outputs standard ArduPilot `.waypoints` format with optional TAKEOFF and RTL commands
- Interactive map preview (Leaflet.js) with OSM and satellite tile layers
- Import existing `.waypoints` missions and overlay the lemniscate on top
- Headless CLI mode for display-less ground stations (`--no-gui`)

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

**GUI (default):**
```bash
python main.py
```

**Headless CLI:**
```bash
python main.py --no-gui \
  --lat 40.7875 \
  --lon 30.3936 \
  --altitude 30 \
  --semi-locus 50 \
  --orientation 0 \
  --waypoints 36 \
  --output mission.waypoints
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `--lat` | Center latitude (decimal degrees) |
| `--lon` | Center longitude (decimal degrees) |
| `--altitude` | Flight altitude in meters (AGL) |
| `--semi-locus` | Scale parameter `a` — half the figure width (meters) |
| `--orientation` | Clockwise rotation from north (degrees) |
| `--waypoints` | Number of waypoints to generate |
| `--output` | Output file path (default: `mission.waypoints`) |

## Documentation

- [Architecture](docs/Architecture.md)
- [Design](docs/Design.md)
- [Roadmap](docs/Roadmap.md)

## License

MIT
