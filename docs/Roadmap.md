# Roadmap

## Phase 1 — Core Engine

- [x] `MissionConfig` and `Waypoint` dataclass definitions (`models.py`)
- [x] Bernoulli lemniscate parametric computation (`lemniscate_engine.py`)
- [x] ENU → WGS84 coordinate conversion (`coordinate_converter.py`)
- [x] ArduPilot `.waypoints` file write + parse (`mission_formatter.py`)
- [x] Input validation (`input_handler.py`)
- [x] Headless CLI interface via `argparse` (`main.py --no-gui`)

**Done when:** the tool runs from the command line and produces a valid, importable `.waypoints` file.

---

## Phase 2 — GUI

- [x] `MainWindow` two-pane layout (parameter panel + map view)
- [x] `ParameterPanel` with all `MissionConfig` fields and live `config_changed` signal
- [x] `MapView` — `QWebEngineView` loading `assets/map.html`
- [x] `MapBridge` — `QWebChannel` connection between Python and Leaflet
- [x] Real-time lemniscate polyline update on parameter change (150 ms debounce)
- [x] `.waypoints` import via file dialog — imported mission overlaid as grey markers
- [x] Export button wired to `mission_formatter.write_waypoints_file`
- [x] `SettingsPanel` — offline asset download (Leaflet JS/CSS + tile cache), tile layer preference, default coordinates

**Done when:** the full GUI workflow (set parameters → preview on map → import existing mission → export) works end to end.

---

## Phase 3 — Testing & Validation

- [ ] Unit tests for all core modules (`unittest`)
- [ ] Regression tests across varied `a`, `n`, and `orientation` values
- [ ] Edge case handling: `n < 4`, non-positive `a`, polar-adjacent coordinates
- [ ] Visual verification by importing output into Mission Planner

---

## Phase 4 — Usability

- [ ] JSON / YAML config file support (save and load mission profiles)
- [ ] Summary table printed to stdout in CLI mode
- [ ] TAKEOFF and RTL commands toggled via GUI checkbox and CLI flag
- [ ] `DO_CHANGE_SPEED` command injected into the waypoint chain

---

## Phase 5 — Advanced (Optional)

- [ ] Multi-lap lemniscate (repeat count parameter)
- [ ] 3D lemniscate: altitude as a function of `t`
- [ ] Mission Planner plugin integration (C# bridge or script API)

---

## Open Questions

- How will inter-waypoint speed be enforced reliably in ArduPilot?
- Mission Planner's default waypoint limit is 750 — document the effective `n` ceiling.
- `center_lat / center_lon` defaults will be updated once the competition site coordinates are confirmed.
