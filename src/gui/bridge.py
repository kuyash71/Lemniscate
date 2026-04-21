from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal


class MapBridge(QObject):
    center_selected = pyqtSignal(float, float)

    @pyqtSlot(float, float)
    def set_center_from_map(self, lat: float, lon: float) -> None:
        self.center_selected.emit(lat, lon)

    @pyqtSlot(list)
    def set_lemniscate(self, points: list) -> None:
        pass

    @pyqtSlot(list)
    def set_imported_mission(self, waypoints: list) -> None:
        pass
