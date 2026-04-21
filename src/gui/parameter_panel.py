import sys
import webbrowser
from pathlib import Path

from PyQt6.QtCore import pyqtSignal, QTimer, Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QDoubleSpinBox,
    QSpinBox, QPushButton, QLabel, QHBoxLayout,
    QFileDialog, QFrame, QSizePolicy
)

from src.core.config import AppConfig
from src.core.models import MissionConfig

GITHUB_URL   = "https://github.com/kuyash71/Lemniscate"
PANEL_WIDTH  = 300
LOGO_MAX_W   = int(PANEL_WIDTH * 0.88)
LOGO_MAX_H   = 110


def _asset(name: str) -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent.parent.parent))
    return base / "assets" / name


class ParameterPanel(QWidget):
    config_changed         = pyqtSignal(MissionConfig)
    export_requested       = pyqtSignal(MissionConfig, str)
    import_requested       = pyqtSignal(str)
    theme_toggle_requested = pyqtSignal()
    settings_requested     = pyqtSignal()

    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.setObjectName("parameterPanel")
        self.setFixedWidth(PANEL_WIDTH)
        self._app_config  = app_config
        self._logo_pixmap = None
        self._debounce    = QTimer(singleShot=True, interval=150)
        self._debounce.timeout.connect(self._emit_config)
        self._build_ui()

    # ── UI construction ────────────────────────────────────────────────

    def _build_ui(self) -> None:
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        outer.addWidget(self._make_logo_bar())
        outer.addWidget(self._make_form(), stretch=1)
        outer.addWidget(self._make_bottom_bar())

    def _make_logo_bar(self) -> QWidget:
        bar = QWidget()
        bar.setObjectName("logoBar")
        bar.setStyleSheet("#logoBar { border-bottom: 1px solid rgba(128,128,128,0.2); }")

        self._logo_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self._logo_label.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )

        self._logo_text = QLabel("LEMNISCATE")
        self._logo_text.setObjectName("logoText")
        self._logo_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        col = QVBoxLayout()
        col.setContentsMargins(0, 0, 0, 0)
        col.setSpacing(4)
        col.addWidget(self._logo_label)
        col.addWidget(self._logo_text)

        layout = QHBoxLayout(bar)
        layout.setContentsMargins(0, 8, 0, 10)
        layout.addStretch()
        layout.addLayout(col)
        layout.addStretch()
        return bar

    def _make_form(self) -> QWidget:
        form_widget = QWidget()
        form_widget.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        lo = QVBoxLayout(form_widget)
        lo.setContentsMargins(16, 14, 16, 14)
        lo.setSpacing(10)

        title = QLabel("Mission Parameters")
        title.setObjectName("sectionTitle")
        lo.addWidget(title)

        form = QFormLayout()
        form.setSpacing(8)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        c = self._app_config
        self._lat        = self._dspin(-90,    90,    c.default_lat,        6)
        self._lon        = self._dspin(-180,   180,   c.default_lon,        6)
        self._altitude   = self._dspin(0.01,   10000, c.default_altitude,   1)
        self._semi_locus = self._dspin(0.01,   10000, c.default_semi_locus, 1)
        self._speed      = self._dspin(0,      200,   c.default_speed,      1)

        self._n_waypoints = QSpinBox()
        self._n_waypoints.setRange(7, 720)
        self._n_waypoints.setValue(c.default_n_waypoints)

        self._orientation = self._dspin(-9999, 9999, c.default_orientation, 1)
        self._orientation_norm = QLabel(f"{c.default_orientation % 360:.1f}°")
        self._orientation_norm.setObjectName("accentLabel")
        self._orientation_norm.setFixedWidth(44)
        self._orientation_norm.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        ori_row = QHBoxLayout()
        ori_row.setSpacing(6)
        ori_row.addWidget(self._orientation)
        ori_row.addWidget(self._orientation_norm)

        form.addRow(self._plabel("📍", "Center Lat"),      self._lat)
        form.addRow(self._plabel("📍", "Center Lon"),      self._lon)
        form.addRow(self._plabel("📐", "Altitude (m)"),    self._altitude)
        form.addRow(self._plabel("↔",  "Semi-locus (m)"),  self._semi_locus)
        form.addRow(self._plabel("🔄", "Orientation (°)"), ori_row)
        form.addRow(self._plabel("📌", "Waypoints"),       self._n_waypoints)
        form.addRow(self._plabel("💨", "Speed (m/s)"),     self._speed)
        lo.addLayout(form)

        self._low_alt_warning = QLabel("⚠  Low altitude")
        self._low_alt_warning.setObjectName("warningLabel")
        self._low_alt_warning.setVisible(False)
        lo.addWidget(self._low_alt_warning)

        self._btn_generate = QPushButton("Generate")
        self._btn_generate.setObjectName("primaryButton")
        self._btn_import   = QPushButton("Import Mission…")
        self._btn_export   = QPushButton("Export…")
        self._btn_export.setEnabled(False)

        lo.addWidget(self._btn_generate)
        lo.addWidget(self._btn_import)
        lo.addWidget(self._btn_export)
        lo.addStretch()

        # signals
        for w in (self._lat, self._lon, self._altitude, self._semi_locus, self._speed):
            w.valueChanged.connect(self._on_value_changed)
        self._orientation.valueChanged.connect(self._on_orientation_changed)
        self._n_waypoints.valueChanged.connect(self._on_value_changed)
        self._btn_generate.clicked.connect(self._emit_config)
        self._btn_import.clicked.connect(self._on_import)
        self._btn_export.clicked.connect(self._on_export)

        return form_widget

    def _make_bottom_bar(self) -> QWidget:
        bar = QWidget()
        bar.setObjectName("bottomBar")
        bar.setStyleSheet("#bottomBar { border-top: 1px solid rgba(128,128,128,0.2); }")

        self._theme_btn = self._icon_btn("🌙", "Toggle dark / light mode")
        self._theme_btn.clicked.connect(self._on_theme_toggle)

        settings_btn = self._icon_btn("⚙", "Settings")
        settings_btn.clicked.connect(lambda: self.settings_requested.emit())

        self._github_btn = self._icon_btn("", "Open GitHub repository")
        self._github_btn.clicked.connect(lambda: webbrowser.open(GITHUB_URL))

        lo = QHBoxLayout(bar)
        lo.setContentsMargins(12, 0, 12, 0)
        lo.setSpacing(8)
        lo.addStretch()
        lo.addWidget(self._theme_btn)
        lo.addWidget(settings_btn)
        lo.addWidget(self._github_btn)
        lo.addStretch()
        return bar

    # ── Helpers ────────────────────────────────────────────────────────

    def _dspin(self, lo, hi, val, dec) -> QDoubleSpinBox:
        s = QDoubleSpinBox()
        s.setRange(lo, hi)
        s.setDecimals(dec)
        s.setValue(val)
        return s

    def _plabel(self, emoji: str, text: str) -> QLabel:
        lbl = QLabel(f"{emoji}  {text}")
        lbl.setObjectName("paramLabel")
        return lbl

    def _icon_btn(self, icon: str, tooltip: str) -> QPushButton:
        btn = QPushButton(icon)
        btn.setObjectName("themeToggle")
        btn.setFixedSize(36, 36)
        btn.setToolTip(tooltip)
        return btn

    def _hsep(self) -> QFrame:
        line = QFrame()
        line.setObjectName("separator")
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        return line

    def _load_logo_pixmap(self, theme: str | None = None) -> None:
        t = theme or self._app_config.theme
        name = "logo_dark.png" if t == "dark" else "logo_light.png"
        path = _asset(name)
        if not path.exists():
            path = _asset("logo.png")
        self._logo_pixmap = QPixmap(str(path)) if path.exists() else None
        self._render_logo()

    def _render_logo(self) -> None:
        if self._logo_pixmap and not self._logo_pixmap.isNull():
            pix = self._logo_pixmap.scaled(
                LOGO_MAX_W, LOGO_MAX_H,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self._logo_label.setFixedSize(pix.width(), pix.height())
            self._logo_label.setPixmap(pix)
        else:
            self._logo_label.setFixedHeight(28)
            self._logo_label.setFixedWidth(LOGO_MAX_W)
            self._logo_label.setText("LEMNISCATE")
            self._logo_label.setStyleSheet(
                "color: #00d4ff; font-size: 20px; font-weight: 700; letter-spacing: 2px;"
            )

    def _update_github_icon(self, theme: str) -> None:
        name = "github_dark.png" if theme == "dark" else "github_light.png"
        path = _asset(name)
        if path.exists():
            self._github_btn.setIcon(QIcon(str(path)))
            self._github_btn.setIconSize(QSize(20, 20))
            self._github_btn.setText("")
        else:
            self._github_btn.setText("GH")

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self._load_logo_pixmap()
        self._update_github_icon(self._app_config.theme)

    # ── Slots ──────────────────────────────────────────────────────────

    def _on_value_changed(self) -> None:
        self._low_alt_warning.setVisible(0 < self._altitude.value() <= 10)
        self._debounce.start()

    def _on_orientation_changed(self) -> None:
        self._orientation_norm.setText(f"{self._orientation.value() % 360:.1f}°")
        self._debounce.start()

    def _emit_config(self) -> None:
        try:
            self._btn_export.setEnabled(True)
            self.config_changed.emit(self.get_config())
        except ValueError:
            pass

    def get_config(self) -> MissionConfig:
        return MissionConfig(
            center_lat=self._lat.value(),
            center_lon=self._lon.value(),
            altitude=self._altitude.value(),
            semi_locus=self._semi_locus.value(),
            orientation=self._orientation.value() % 360,
            n_waypoints=self._n_waypoints.value(),
            speed=self._speed.value(),
        )

    def _on_import(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Import Mission", "",
            "Waypoints (*.waypoints);;All Files (*)"
        )
        if path:
            self.import_requested.emit(path)

    def _on_export(self) -> None:
        path, _ = QFileDialog.getSaveFileName(
            self, "Export Mission", "mission.waypoints",
            "Waypoints (*.waypoints);;All Files (*)"
        )
        if path:
            self.export_requested.emit(self.get_config(), path)

    def _on_theme_toggle(self) -> None:
        self.theme_toggle_requested.emit()

    def update_theme_icon(self, theme: str) -> None:
        self._theme_btn.setText("☀" if theme == "dark" else "🌙")
        self._update_github_icon(theme)
        self._load_logo_pixmap(theme)

    def set_center(self, lat: float, lon: float) -> None:
        self._lat.blockSignals(True)
        self._lon.blockSignals(True)
        self._lat.setValue(lat)
        self._lon.setValue(lon)
        self._lat.blockSignals(False)
        self._lon.blockSignals(False)
        self._emit_config()
