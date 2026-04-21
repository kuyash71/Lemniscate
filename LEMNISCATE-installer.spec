# -*- mode: python ; coding: utf-8 -*-
# Onedir build — used by NSIS / AppImage packaging
import sys
from PyInstaller.utils.hooks import collect_all

icon = 'assets/icon.ico' if sys.platform == 'win32' else 'assets/logo_dark.png'

datas     = [('assets', 'assets')]
binaries  = []
hiddenimports = [
    'PyQt6.QtWebEngineWidgets',
    'PyQt6.QtWebEngineCore',
    'PyQt6.QtWebChannel',
    'PyQt6.QtNetwork',
]

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
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'tkinter', 'unittest', 'test', 'email', 'html',
        'http', 'urllib', 'xml', 'xmlrpc', 'pydoc', 'doctest',
        'difflib', 'ftplib', 'imaplib', 'poplib', 'smtplib',
        'telnetlib', 'multiprocessing', 'concurrent',
        'asyncio', 'ctypes.test', 'lib2to3',
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LEMNISCATE',
    debug=False,
    strip=True,
    upx=True,
    upx_exclude=['QtWebEngineCore', 'QtWebEngineWidgets'],
    console=False,
    icon=icon,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=['QtWebEngineCore', 'QtWebEngineWidgets'],
    name='LEMNISCATE',
)
