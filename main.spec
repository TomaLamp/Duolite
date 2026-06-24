# -*- mode: python ; coding: utf-8 -*-
import os
import shutil
import sys

block_cipher = None
app_name = 'Duolité'

# Liste des fichiers annexes à inclure
added_files = [
    ('annexes', 'annexes'),
    ('image', 'image'),
    ('jeux', 'jeux'),
    ('module', 'module'),
    ('police', 'police')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

chosen_icon = None

if sys.platform == 'win32':
    # Windows a besoin du .ico
    chosen_icon = 'image/icon/icon.ico'
elif sys.platform == 'darwin':
    # macOS a besoin du .icns
    chosen_icon = 'image/icon/icon.icns'
else:
    # Linux (ou autre) n'embarque pas d'icone dans le binaire
    chosen_icon = None

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Pas de console à l'exécution
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=chosen_icon,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=app_name,
)

# --- SCRIPT DE DEPLACEMENT AUTOMATIQUE (UNIVERSEL TOUS OS) ---

# 1. Gestion adaptative des chemins selon l'OS
# Sur macOS, l'application est compilée dans un bundle ".app"
if sys.platform == 'darwin':
    dist_path = os.path.join('dist', f'{app_name}.app', 'Contents', 'MacOS')
else:
    dist_path = os.path.join('dist', app_name)

internal_path = os.path.join(dist_path, '_internal')
folders_to_move = ['image', 'jeux', 'module', 'police']

if os.path.exists(internal_path):
    for folder in folders_to_move:
        src = os.path.join(internal_path, folder)
        dst = os.path.join(dist_path, folder)
        
        if os.path.exists(src):
            if os.path.exists(dst):
                # Correction d'un bug Linux/macOS : shutil.rmtree peut planter 
                # si les permissions de certains fichiers sont verrouillées.
                try:
                    shutil.rmtree(dst)
                except PermissionError:
                    # Alternative forcée si rmtree échoue
                    os.system(f'rm -rf "{dst}"')
            
            # Déplacement sécurisé
            shutil.move(src, dst)