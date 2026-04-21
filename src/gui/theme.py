from PyQt6.QtWidgets import QApplication

DARK = """
QWidget {
    background-color: #0d0d1a;
    color: #e0e0f0;
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 13px;
}

QMainWindow, QDialog {
    background-color: #0d0d1a;
}

/* Panel surface */
QWidget#parameterPanel {
    background-color: #13132a;
    border-right: 1px solid #1f1f3a;
}

/* Labels */
QLabel {
    background: transparent;
    color: #e0e0f0;
}
QLabel#sectionTitle {
    color: #ffffff;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
QLabel#warningLabel {
    color: #f0a500;
    font-size: 12px;
}
QLabel#paramLabel {
    color: #888aa0;
    font-size: 12px;
}

/* Spin boxes */
QDoubleSpinBox, QSpinBox {
    background-color: #1a1a33;
    border: 1px solid #2a2a50;
    border-radius: 6px;
    padding: 4px 8px;
    color: #e0e0f0;
    selection-background-color: #00d4ff;
}
QDoubleSpinBox:focus, QSpinBox:focus {
    border: 1px solid #00d4ff;
}
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,
QSpinBox::up-button, QSpinBox::down-button {
    background-color: #1a1a33;
    border: none;
    width: 18px;
}
QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 5px solid #888aa0;
    width: 0; height: 0;
}
QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #888aa0;
    width: 0; height: 0;
}

/* Buttons */
QPushButton {
    background-color: #1a1a33;
    color: #c0c0e0;
    border: 1px solid #2a2a50;
    border-radius: 6px;
    padding: 7px 14px;
    font-size: 13px;
}
QPushButton:hover {
    background-color: #22224a;
    border-color: #00d4ff;
    color: #ffffff;
}
QPushButton:pressed {
    background-color: #0d0d1a;
}
QPushButton#primaryButton {
    background-color: #00d4ff;
    color: #0d0d1a;
    font-weight: 700;
    border: none;
}
QPushButton#primaryButton:hover {
    background-color: #33ddff;
}
QPushButton:disabled {
    background-color: #131325;
    color: #444466;
    border-color: #1a1a33;
}

/* Theme toggle */
QPushButton#themeToggle {
    background: transparent;
    border: none;
    color: #888aa0;
    font-size: 18px;
    padding: 2px 6px;
}
QPushButton#themeToggle:hover {
    color: #ffffff;
}

/* ComboBox */
QComboBox {
    background-color: #1a1a33;
    border: 1px solid #2a2a50;
    border-radius: 6px;
    padding: 4px 8px;
    color: #e0e0f0;
}
QComboBox:focus { border-color: #00d4ff; }
QComboBox QAbstractItemView {
    background-color: #1a1a33;
    border: 1px solid #2a2a50;
    selection-background-color: #00d4ff;
    selection-color: #0d0d1a;
}

/* CheckBox */
QCheckBox { spacing: 6px; color: #e0e0f0; }
QCheckBox::indicator {
    width: 16px; height: 16px;
    border: 1px solid #2a2a50;
    border-radius: 4px;
    background: #1a1a33;
}
QCheckBox::indicator:checked {
    background: #00d4ff;
    border-color: #00d4ff;
}

/* Menu */
QMenuBar {
    background-color: #0d0d1a;
    color: #c0c0e0;
    border-bottom: 1px solid #1f1f3a;
}
QMenuBar::item:selected { background-color: #1a1a33; }
QMenu {
    background-color: #13132a;
    border: 1px solid #2a2a50;
    color: #e0e0f0;
}
QMenu::item:selected { background-color: #1a1a33; }

/* Scrollbar */
QScrollBar:vertical {
    background: #0d0d1a; width: 8px; border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #2a2a50; border-radius: 4px; min-height: 30px;
}

/* Separator */
QFrame[frameShape="4"], QFrame[frameShape="5"] {
    color: #1f1f3a;
}
"""

LIGHT = """
QWidget {
    background-color: #f0f2f5;
    color: #111827;
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 13px;
}

QMainWindow, QDialog {
    background-color: #f0f2f5;
}

QWidget#parameterPanel {
    background-color: #ffffff;
    border-right: 1px solid #d1d5db;
}

QLabel { background: transparent; color: #111827; }
QLabel#sectionTitle {
    color: #0a0a18;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.3px;
}
QLabel#warningLabel { color: #b45309; font-size: 12px; }
QLabel#paramLabel { color: #374151; font-size: 12px; }

QDoubleSpinBox, QSpinBox {
    background-color: #f9fafb;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 4px 8px;
    color: #111827;
}
QDoubleSpinBox:focus, QSpinBox:focus {
    border: 1px solid #2563eb;
    background-color: #ffffff;
}
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,
QSpinBox::up-button, QSpinBox::down-button {
    background-color: transparent; border: none; width: 18px;
}
QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 5px solid #6b7280;
    width: 0; height: 0;
}
QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #6b7280;
    width: 0; height: 0;
}

QPushButton {
    background-color: #ffffff;
    color: #374151;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 7px 14px;
    font-size: 13px;
}
QPushButton:hover {
    background-color: #f3f4f6;
    border-color: #2563eb;
    color: #111827;
}
QPushButton:pressed { background-color: #e5e7eb; }
QPushButton#primaryButton {
    background-color: #1d4ed8;
    color: #ffffff;
    font-weight: 700;
    border: none;
}
QPushButton#primaryButton:hover { background-color: #2563eb; }
QPushButton:disabled {
    background-color: #f9fafb;
    color: #9ca3af;
    border-color: #e5e7eb;
}

QPushButton#themeToggle {
    background: transparent;
    border: none;
    color: #6b7280;
    font-size: 18px;
    padding: 2px 6px;
}
QPushButton#themeToggle:hover { color: #111827; }

QComboBox {
    background-color: #f9fafb;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 4px 8px;
    color: #111827;
}
QComboBox:focus { border-color: #2563eb; }
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    selection-background-color: #2563eb;
    selection-color: #ffffff;
}

QCheckBox { spacing: 6px; color: #111827; }
QCheckBox::indicator {
    width: 16px; height: 16px;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    background: #ffffff;
}
QCheckBox::indicator:checked {
    background: #1d4ed8;
    border-color: #1d4ed8;
}

QMenuBar {
    background-color: #ffffff;
    color: #111827;
    border-bottom: 1px solid #d1d5db;
}
QMenuBar::item:selected { background-color: #f3f4f6; }
QMenu {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    color: #111827;
}
QMenu::item { padding: 6px 16px; }
QMenu::item:selected { background-color: #eff6ff; color: #1d4ed8; }

QScrollBar:vertical {
    background: #f0f2f5; width: 8px; border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #d1d5db; border-radius: 4px; min-height: 30px;
}
QScrollBar::handle:vertical:hover { background: #9ca3af; }

QFrame[frameShape="4"], QFrame[frameShape="5"] { color: #e5e7eb; }
"""


def apply(theme: str) -> None:
    QApplication.instance().setStyleSheet(DARK if theme == "dark" else LIGHT)
