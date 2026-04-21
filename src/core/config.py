import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path


def _defaults_path() -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent.parent.parent))
    return base / "assets" / "default_config.json"


def _user_config_path() -> Path:
    return Path(sys.executable).parent / "config.json"


@dataclass
class AppConfig:
    default_lat: float = 39.9
    default_lon: float = 32.8
    default_altitude: float = 30.0
    default_semi_locus: float = 50.0
    default_orientation: float = 0.0
    default_n_waypoints: int = 36
    default_speed: float = 0.0
    tile_layer: str = "satellite"
    include_takeoff: bool = True
    include_rtl: bool = True
    leaflet_local: bool = False
    theme: str = "dark"


def load() -> AppConfig:
    data: dict = {}

    try:
        with open(_defaults_path()) as f:
            data.update(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    try:
        with open(_user_config_path()) as f:
            data.update(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return AppConfig(**{k: v for k, v in data.items() if k in AppConfig.__dataclass_fields__})


def save(config: AppConfig) -> None:
    defaults = load_defaults()
    overrides = {
        k: v for k, v in asdict(config).items()
        if v != getattr(defaults, k)
    }
    if not overrides:
        return
    path = _user_config_path()
    with open(path, "w") as f:
        json.dump(overrides, f, indent=2)


def load_defaults() -> AppConfig:
    try:
        with open(_defaults_path()) as f:
            data = json.load(f)
        return AppConfig(**{k: v for k, v in data.items() if k in AppConfig.__dataclass_fields__})
    except (FileNotFoundError, json.JSONDecodeError):
        return AppConfig()
