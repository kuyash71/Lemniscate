from PyQt6.QtWidgets import QDialog, QFormLayout, QDoubleSpinBox, QSpinBox, QComboBox, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSignal
from src.core.config import AppConfig, save


class SettingsPanel(QDialog):
    settings_saved = pyqtSignal(AppConfig)

    def __init__(self, config: AppConfig, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self._config = config
        self._build_ui()

    def _build_ui(self) -> None:
        form = QFormLayout()

        self._lat = QDoubleSpinBox()
        self._lon = QDoubleSpinBox()
        self._altitude = QDoubleSpinBox()
        self._semi_locus = QDoubleSpinBox()
        self._orientation = QDoubleSpinBox()
        self._n_waypoints = QSpinBox()
        self._speed = QDoubleSpinBox()
        self._tile_layer = QComboBox()
        self._include_takeoff = QCheckBox()
        self._include_rtl = QCheckBox()
        self._download_leaflet = QPushButton("Download Leaflet for offline use")

        self._tile_layer.addItems(["satellite", "street"])

        form.addRow("Default Latitude", self._lat)
        form.addRow("Default Longitude", self._lon)
        form.addRow("Default Altitude (m)", self._altitude)
        form.addRow("Default Semi-locus (m)", self._semi_locus)
        form.addRow("Default Orientation (°)", self._orientation)
        form.addRow("Default Waypoints", self._n_waypoints)
        form.addRow("Default Speed (m/s)", self._speed)
        form.addRow("Tile Layer", self._tile_layer)
        form.addRow("Include TAKEOFF", self._include_takeoff)
        form.addRow("Include RTL", self._include_rtl)
        form.addRow("Offline Assets", self._download_leaflet)

        buttons = QHBoxLayout()
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(buttons)

        self._load_values()
        save_btn.clicked.connect(self._save)
        cancel_btn.clicked.connect(self.reject)
        self._download_leaflet.clicked.connect(self._on_download_leaflet)

    def _load_values(self) -> None:
        c = self._config
        self._lat.setValue(c.default_lat)
        self._lon.setValue(c.default_lon)
        self._altitude.setValue(c.default_altitude)
        self._semi_locus.setValue(c.default_semi_locus)
        self._orientation.setValue(c.default_orientation)
        self._n_waypoints.setValue(c.default_n_waypoints)
        self._speed.setValue(c.default_speed)
        self._tile_layer.setCurrentText(c.tile_layer)
        self._include_takeoff.setChecked(c.include_takeoff)
        self._include_rtl.setChecked(c.include_rtl)

    def _save(self) -> None:
        self._config.default_lat = self._lat.value()
        self._config.default_lon = self._lon.value()
        self._config.default_altitude = self._altitude.value()
        self._config.default_semi_locus = self._semi_locus.value()
        self._config.default_orientation = self._orientation.value()
        self._config.default_n_waypoints = self._n_waypoints.value()
        self._config.default_speed = self._speed.value()
        self._config.tile_layer = self._tile_layer.currentText()
        self._config.include_takeoff = self._include_takeoff.isChecked()
        self._config.include_rtl = self._include_rtl.isChecked()
        save(self._config)
        self.settings_saved.emit(self._config)
        self.accept()

    def _on_download_leaflet(self) -> None:
        pass
