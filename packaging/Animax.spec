# -*- mode: python ; coding: utf-8 -*-
"""Сборка Animax.exe (PyInstaller, один файл).

Запуск: python packaging\\build.py
"""

import os

# спек лежит в packaging/, исходники — уровнем выше
ROOT = os.path.dirname(SPECPATH)
APP = os.path.join(ROOT, 'animax')

a = Analysis(
    [os.path.join(ROOT, 'Animax.pyw')],
    pathex=[ROOT],
    binaries=[],
    datas=[
        (os.path.join(APP, 'web'), 'web'),
        (os.path.join(APP, 'animax.ico'), '.'),
        (os.path.join(APP, 'notify_toast.ps1'), '.'),
    ],
    hiddenimports=[
        # без этого модуля сервер молча работает без онлайн-озвучек — называем его явно
        'animax.sources',
        # импортируются внутри функций — PyInstaller их не всегда видит
        'PIL.Image',
        'PIL.ImageFilter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pytest', 'setuptools', 'pip', 'numpy', 'psutil', 'yaml', 'tkinter', '_tkinter'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Animax',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,              # без чёрного окна консоли
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(APP, 'animax.ico'),
    version=os.path.join(SPECPATH, 'version_info.txt'),
)
