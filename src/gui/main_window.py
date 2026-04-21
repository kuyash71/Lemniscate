from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QAction

from src.core import (
    parse_and_validate, generate_local_points,
    to_waypoints, write_waypoints_file, parse_waypoints_file
)
from src.core.config import load as load_config, save as save_config
from src.core.models import MissionConfig
from src.gui import theme as theme_mod
from src.gui.map_view import MapView
from src.gui.parameter_panel import ParameterPanel
from src.gui.settings_panel import SettingsPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LEMNISCATE")
        self._app_config = load_config()
        self._last_waypoints = []
        theme_mod.apply(self._app_config.theme)
        self._build_ui()
        self._build_menu()

    def _build_ui(self) -> None:
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._panel = ParameterPanel(self._app_config)
        self._map = MapView()

        layout.addWidget(self._panel)
        layout.addWidget(self._map, stretch=1)

        self.setCentralWidget(container)

        self._panel.config_changed.connect(self._on_config_changed)
        self._panel.export_requested.connect(self._on_export)
        self._panel.import_requested.connect(self._on_import)
        self._panel.theme_toggle_requested.connect(self._on_theme_toggle)
        self._panel.settings_requested.connect(self._open_settings)
        self._map.bridge.center_selected.connect(self._panel.set_center)

    def _build_menu(self) -> None:
        self.menuBar().setVisible(False)

    # ── Core pipeline ──────────────────────────────────────────────────

    def _on_config_changed(self, config: MissionConfig) -> None:
        try:
            validated = parse_and_validate(
                center_lat=config.center_lat,
                center_lon=config.center_lon,
                altitude=config.altitude,
                semi_locus=config.semi_locus,
                orientation=config.orientation,
                n_waypoints=config.n_waypoints,
                speed=config.speed,
            )
            points = generate_local_points(validated)
            self._last_waypoints = to_waypoints(points, validated)
            self._map.update_lemniscate(self._last_waypoints)
            self._map.pan_to(validated.center_lat, validated.center_lon)
        except (ValueError, TypeError):
            pass

    def _on_export(self, config: MissionConfig, path: str) -> None:
        if not self._last_waypoints or not path:
            return
        write_waypoints_file(
            self._last_waypoints, config, path,
            include_takeoff=self._app_config.include_takeoff,
            include_rtl=self._app_config.include_rtl,
        )

    def _on_import(self, path: str) -> None:
        try:
            waypoints = parse_waypoints_file(path)
            self._map.update_imported_mission(waypoints)
        except Exception as e:
            QMessageBox.warning(self, "Import Failed", str(e))

    # ── Theme ──────────────────────────────────────────────────────────

    def _on_theme_toggle(self) -> None:
        self._app_config.theme = "light" if self._app_config.theme == "dark" else "dark"
        theme_mod.apply(self._app_config.theme)
        self._panel.update_theme_icon(self._app_config.theme)
        self._map.set_theme(self._app_config.theme)
        save_config(self._app_config)

    # ── Settings ───────────────────────────────────────────────────────

    def _open_settings(self) -> None:
        dialog = SettingsPanel(self._app_config, self)
        dialog.settings_saved.connect(self._on_settings_saved)
        dialog.exec()

    def _on_settings_saved(self, config) -> None:
        self._app_config = config
