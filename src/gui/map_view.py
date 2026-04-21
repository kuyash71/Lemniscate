import json
import sys
from pathlib import Path

from PyQt6.QtCore import QUrl
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView

from src.core.models import Waypoint
from src.gui.bridge import MapBridge


def _map_html_path() -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent.parent.parent))
    return base / "assets" / "map.html"


class MapView(QWebEngineView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True
        )
        self.bridge = MapBridge()
        self.channel = QWebChannel()
        self.channel.registerObject("bridge", self.bridge)
        self.page().setWebChannel(self.channel)
        self.load_map()

    def load_map(self) -> None:
        url = QUrl.fromLocalFile(str(_map_html_path()))
        self.load(url)

    def update_lemniscate(self, waypoints: list[Waypoint]) -> None:
        data = [{"lat": wp.lat, "lon": wp.lon} for wp in waypoints]
        self._js(f"drawLemniscate({json.dumps(data)})")

    def update_imported_mission(self, waypoints: list[Waypoint]) -> None:
        data = [{"index": wp.index, "lat": wp.lat, "lon": wp.lon} for wp in waypoints]
        self._js(f"drawImportedMission({json.dumps(data)})")

    def pan_to(self, lat: float, lon: float) -> None:
        self._js(f"panTo({lat}, {lon})")

    def set_theme(self, theme: str) -> None:
        if theme == "light":
            self._js("document.body.classList.add('light')")
        else:
            self._js("document.body.classList.remove('light')")

    def _js(self, script: str) -> None:
        self.page().runJavaScript(script)
