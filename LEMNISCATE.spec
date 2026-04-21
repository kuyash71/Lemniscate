# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_all, collect_data_files

icon = 'assets/icon.ico' if sys.platform == 'win32' else 'assets/logo_dark.png'

datas     = [('assets', 'assets')]
binaries  = []
hiddenimports = [
    'PyQt6.QtWebEngineWidgets',
    'PyQt6.QtWebEngineCore',
    'PyQt6.QtWebChannel',
    'PyQt6.QtNetwork',
]

# Collect PyQt6 WebEngine resources (translations, locales, etc.)
for pkg in ('PyQt6.QtWebEngineWidgets', 'PyQt6.QtWebEngineCore'):
    d, b, h = collect_all(pkg)
    datas        += d
    binaries     += b
    hiddenimports += h

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'tkinter', 'unittest', 'test', 'email', 'html',
        'http', 'urllib', 'xml', 'xmlrpc', 'pydoc', 'doctest',
        'difflib', 'ftplib', 'imaplib', 'poplib', 'smtplib',
        'telnetlib', 'logging', 'multiprocessing', 'concurrent',
        'asyncio', 'ctypes.test', 'lib2to3',
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LEMNISCATE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=['QtWebEngineCore', 'QtWebEngineWidgets'],
    console=False,
    icon=icon,
)
