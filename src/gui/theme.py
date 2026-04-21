from PyQt6.QtWidgets import QApplication

# ── Catppuccin Mocha ───────────────────────────────────────────────────────────
DARK = """
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 13px;
}

QMainWindow, QDialog {
    background-color: #1e1e2e;
}

QWidget#parameterPanel {
    background-color: #181825;
    border-right: 1px solid #313244;
}

QLabel { background: transparent; color: #cdd6f4; }
QLabel#sectionTitle {
    color: #cdd6f4;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
QLabel#logoText {
    color: #cba6f7;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 4px;
}
QLabel#accentLabel    { color: #cba6f7; font-size: 12px; }
QLabel#warningLabel   { color: #fab387; font-size: 12px; }
QLabel#paramLabel     { color: #a6adc8; font-size: 12px; }
QLabel#signatureLabel { color: #b4befe; font-size: 11px; letter-spacing: 1px; }

QDoubleSpinBox, QSpinBox {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 4px 8px;
    color: #cdd6f4;
    selection-background-color: #cba6f7;
    selection-color: #1e1e2e;
}
QDoubleSpinBox:focus, QSpinBox:focus {
    border: 1px solid #cba6f7;
}
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,
QSpinBox::up-button, QSpinBox::down-button {
    background-color: #313244; border: none; width: 18px;
}
QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 5px solid #585b70;
    width: 0; height: 0;
}
QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #585b70;
    width: 0; height: 0;
}

QPushButton {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 7px 14px;
    font-size: 13px;
}
QPushButton:hover {
    background-color: #45475a;
    border-color: #cba6f7;
    color: #cdd6f4;
}
QPushButton:pressed { background-color: #1e1e2e; }
QPushButton#primaryButton {
    background-color: #cba6f7;
    color: #1e1e2e;
    font-weight: 700;
    border: none;
}
QPushButton#primaryButton:hover { background-color: #b4befe; }
QPushButton:disabled {
    background-color: #181825;
    color: #45475a;
    border-color: #313244;
}
QPushButton#themeToggle {
    background: transparent;
    border: none;
    color: #6c7086;
    font-size: 18px;
    padding: 2px 6px;
}
QPushButton#themeToggle:hover { color: #cdd6f4; }

QComboBox {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 4px 8px;
    color: #cdd6f4;
}
QComboBox:focus { border-color: #cba6f7; }
QComboBox QAbstractItemView {
    background-color: #313244;
    border: 1px solid #45475a;
    selection-background-color: #cba6f7;
    selection-color: #1e1e2e;
}

QCheckBox { spacing: 6px; color: #cdd6f4; }
QCheckBox::indicator {
    width: 16px; height: 16px;
    border: 1px solid #45475a;
    border-radius: 4px;
    background: #313244;
}
QCheckBox::indicator:checked {
    background: #cba6f7;
    border-color: #cba6f7;
}

QMenuBar {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border-bottom: 1px solid #313244;
}
QMenuBar::item:selected { background-color: #313244; }
QMenu {
    background-color: #181825;
    border: 1px solid #45475a;
    color: #cdd6f4;
}
QMenu::item { padding: 6px 16px; }
QMenu::item:selected { background-color: #313244; color: #cba6f7; }

QScrollBar:vertical {
    background: #1e1e2e; width: 8px; border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #45475a; border-radius: 4px; min-height: 30px;
}
QScrollBar::handle:vertical:hover { background: #585b70; }

"""

# ── Catppuccin Latte ───────────────────────────────────────────────────────────
LIGHT = """
QWidget {
    background-color: #eff1f5;
    color: #4c4f69;
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 13px;
}

QMainWindow, QDialog { background-color: #eff1f5; }

QWidget#parameterPanel {
    background-color: #e6e9ef;
    border-right: 1px solid #ccd0da;
}

QLabel { background: transparent; color: #4c4f69; }
QLabel#sectionTitle {
    color: #4c4f69;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.3px;
}
QLabel#logoText {
    color: #8839ef;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 4px;
}
QLabel#accentLabel    { color: #8839ef; font-size: 12px; }
QLabel#warningLabel   { color: #fe640b; font-size: 12px; }
QLabel#paramLabel     { color: #5c5f77; font-size: 12px; }
QLabel#signatureLabel { color: #8839ef; font-size: 11px; letter-spacing: 1px; }

QDoubleSpinBox, QSpinBox {
    background-color: #eff1f5;
    border: 1px solid #bcc0cc;
    border-radius: 6px;
    padding: 4px 8px;
    color: #4c4f69;
    selection-background-color: #8839ef;
    selection-color: #eff1f5;
}
QDoubleSpinBox:focus, QSpinBox:focus {
    border: 1px solid #8839ef;
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
    border-bottom: 5px solid #acb0be;
    width: 0; height: 0;
}
QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #acb0be;
    width: 0; height: 0;
}

QPushButton {
    background-color: #e6e9ef;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    border-radius: 6px;
    padding: 7px 14px;
    font-size: 13px;
}
QPushButton:hover {
    background-color: #ccd0da;
    border-color: #8839ef;
    color: #4c4f69;
}
QPushButton:pressed { background-color: #bcc0cc; }
QPushButton#primaryButton {
    background-color: #8839ef;
    color: #eff1f5;
    font-weight: 700;
    border: none;
}
QPushButton#primaryButton:hover { background-color: #7287fd; }
QPushButton:disabled {
    background-color: #e6e9ef;
    color: #acb0be;
    border-color: #ccd0da;
}
QPushButton#themeToggle {
    background: transparent;
    border: none;
    color: #9ca0b0;
    font-size: 18px;
    padding: 2px 6px;
}
QPushButton#themeToggle:hover { color: #4c4f69; }

QComboBox {
    background-color: #eff1f5;
    border: 1px solid #bcc0cc;
    border-radius: 6px;
    padding: 4px 8px;
    color: #4c4f69;
}
QComboBox:focus { border-color: #8839ef; }
QComboBox QAbstractItemView {
    background-color: #e6e9ef;
    border: 1px solid #bcc0cc;
    selection-background-color: #8839ef;
    selection-color: #eff1f5;
}

QCheckBox { spacing: 6px; color: #4c4f69; }
QCheckBox::indicator {
    width: 16px; height: 16px;
    border: 1px solid #bcc0cc;
    border-radius: 4px;
    background: #eff1f5;
}
QCheckBox::indicator:checked {
    background: #8839ef;
    border-color: #8839ef;
}

QMenuBar {
    background-color: #e6e9ef;
    color: #4c4f69;
    border-bottom: 1px solid #ccd0da;
}
QMenuBar::item:selected { background-color: #ccd0da; }
QMenu {
    background-color: #e6e9ef;
    border: 1px solid #bcc0cc;
    border-radius: 6px;
    color: #4c4f69;
}
QMenu::item { padding: 6px 16px; }
QMenu::item:selected { background-color: #ccd0da; color: #8839ef; }

QScrollBar:vertical {
    background: #eff1f5; width: 8px; border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #bcc0cc; border-radius: 4px; min-height: 30px;
}
QScrollBar::handle:vertical:hover { background: #acb0be; }

"""


def apply(theme: str) -> None:
    QApplication.instance().setStyleSheet(DARK if theme == "dark" else LIGHT)
