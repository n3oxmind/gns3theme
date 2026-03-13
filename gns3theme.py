#!/usr/bin/env python3

import re
import sys
import json
import struct
import shutil
import subprocess
from pathlib import Path
from copy import deepcopy
from colorschemes import schemes as builtin_schemes
from argparser import parser
import custom_style as css

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
DIM = '\033[2m'
RESET = '\033[0m'

IS_MACOS = sys.platform == 'darwin'
MACOS_GNS3_APP = Path('/Applications/GNS3.app')
SCRIPT_DIR = Path(__file__).resolve().parent
BUNDLED_SYMBOLS_DIR = SCRIPT_DIR / 'symbols'
GNS3_SYMBOLS_DIR = Path.home() / 'GNS3' / 'symbols'
CONFIG_DIR = Path.home() / '.config' / 'gns3theme'
USER_SCHEMES_DIR = CONFIG_DIR / 'schemes'
CSS_PATH = CONFIG_DIR / 'custom_style.css'
CONFIG_PATH = CONFIG_DIR / 'config.json'

REQUIRED_SCHEME_KEYS = {'bg', 'bg2', 'fg', 'fg2', 'sbg', 'sfg', 'tbg', 'color'}

# Magic number mapping for Python version detection
MAGIC_TO_VERSION = {
    3394: '3.8', 3401: '3.8', 3413: '3.9', 3425: '3.10',
    3433: '3.10', 3438: '3.10', 3450: '3.11', 3495: '3.12',
    3531: '3.13', 3571: '3.13', 3600: '3.14',
}


# --- Utilities ---

def error(tag, msg):
    print(f"{RED}{tag}{RESET}: {msg}")


def success(tag, msg):
    print(f"{GREEN}{tag}{RESET}: {msg}")


def warn(tag, msg):
    print(f"{YELLOW}{tag}{RESET}: {msg}")


def is_valid_color(color):
    return bool(re.fullmatch(r'#[0-9a-fA-F]{6}', color))


def mkdir(dir_path):
    try:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    except OSError as err:
        error("MkdirError", str(err))
        sys.exit(1)


def save_file(data, file_path):
    if not data:
        return
    try:
        with open(file_path, 'w') as fh:
            fh.write(data)
    except (TypeError, OSError) as err:
        error("WriteError", str(err))
        sys.exit(1)
    success("SaveFile", f"Wrote {file_path}")


def backup_file(file_path, backup_dir):
    """Back up file to the specified backup directory."""
    mkdir(backup_dir)
    bak = backup_dir / Path(file_path).name
    if not bak.exists():
        shutil.copy(file_path, bak)
        success("Backup", f"Backed up {Path(file_path).name}")
    else:
        warn("Backup", f"Backup already exists: {bak}")


def load_user_schemes():
    """Load custom schemes from ~/.config/gns3theme/schemes/*.json"""
    user = {}
    if not USER_SCHEMES_DIR.is_dir():
        return user
    for f in sorted(USER_SCHEMES_DIR.glob('*.json')):
        try:
            data = json.loads(f.read_text())
            name = f.stem
            missing = REQUIRED_SCHEME_KEYS - set(data.keys())
            if missing:
                warn("Scheme", f"Skipping {f.name}: missing keys {', '.join(sorted(missing))}")
                continue
            user[name] = data
        except (json.JSONDecodeError, OSError) as err:
            warn("Scheme", f"Skipping {f.name}: {err}")
    return user


def get_all_schemes():
    """Return merged dict of builtin + user schemes (user overrides builtin)."""
    all_schemes = dict(builtin_schemes)
    all_schemes.update(load_user_schemes())
    return all_schemes


def print_colorschemes():
    """Print available schemes grouped by type (dark/light)."""
    all_schemes = get_all_schemes()
    user_names = set(load_user_schemes().keys())

    dark = {k: v for k, v in all_schemes.items() if v.get('color') == 'dark'}
    light = {k: v for k, v in all_schemes.items() if v.get('color') == 'light'}

    if dark:
        print(f"\n  {CYAN}dark{RESET}")
        for name in dark:
            tag = f"  {DIM}(custom){RESET}" if name in user_names else ""
            print(f"    {name}{tag}")

    if light:
        print(f"\n  {CYAN}light{RESET}")
        for name in light:
            tag = f"  {DIM}(custom){RESET}" if name in user_names else ""
            print(f"    {name}{tag}")

    print(f"\n  Add custom schemes as JSON files in ~/.config/gns3theme/schemes/\n")


def validate_scheme(name):
    all_schemes = get_all_schemes()
    if name not in all_schemes:
        error("SchemeError", f"Unknown scheme '{name}'. Use --ls to list available schemes")
        sys.exit(1)


# --- Path detection ---

def detect_pyc_version(pyc_path):
    """Detect Python version from .pyc magic number."""
    try:
        with open(pyc_path, 'rb') as f:
            magic = struct.unpack('<H', f.read(2))[0]
        return MAGIC_TO_VERSION.get(magic)
    except Exception:
        return None


def find_gns3_lib():
    """Auto-detect the lib directory containing gns3 package.

    Returns (path, install_type) where install_type is 'app' or 'source'.
    'app' means macOS GNS3.app bundle with .pyc files.
    'source' means pip/brew install with .py files (Linux or macOS).
    """
    # macOS GNS3.app bundle (cx_Freeze, .pyc files)
    if IS_MACOS and MACOS_GNS3_APP.exists():
        lib = MACOS_GNS3_APP / 'Contents' / 'Resources' / 'lib'
        if (lib / 'gns3' / 'main_window.pyc').exists():
            return lib, 'app'

    # pip/brew/source install (.py files) — works on both macOS and Linux
    for cmd in [
        ['python3', '-c',
         'import importlib.util as u; print(u.find_spec("gns3").submodule_search_locations[0])'],
        ['pip3', 'show', 'gns3-gui'],
    ]:
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True).strip()
            if 'Location:' in out:
                for line in out.splitlines():
                    if line.startswith('Location:'):
                        out = line.split(':', 1)[1].strip()
                        break
            p = Path(out)
            if p.name == 'gns3' and (p / 'main_window.py').exists():
                return p.parent, 'source'
            if (p / 'gns3' / 'main_window.py').exists():
                return p, 'source'
        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            continue

    # Fallback: scan common locations
    home = Path.home()
    candidates = []
    for pyver in ['3.14', '3.13', '3.12', '3.11', '3.10', '3.9', '3.8']:
        candidates.extend([
            home / f'.local/lib/python{pyver}/site-packages',
            Path(f'/usr/lib/python{pyver}/site-packages'),
            Path(f'/usr/lib/python{pyver}/dist-packages'),
            Path(f'/usr/local/lib/python{pyver}/site-packages'),
            Path(f'/usr/local/lib/python{pyver}/dist-packages'),
            Path(f'/usr/lib64/python{pyver}/site-packages'),
        ])
    candidates.append(Path('/usr/lib/python3/dist-packages'))
    # Homebrew on macOS
    if IS_MACOS:
        for pyver in ['3.14', '3.13', '3.12', '3.11', '3.10', '3.9']:
            candidates.extend([
                Path(f'/opt/homebrew/lib/python{pyver}/site-packages'),
                Path(f'/usr/local/lib/python{pyver}/site-packages'),
            ])
    # virtualenvs / pipx
    for venv_base in [home / '.local/pipx/venvs/gns3-gui',
                      home / '.virtualenvs/gns3']:
        if venv_base.exists():
            for pyver in ['3.14', '3.13', '3.12', '3.11', '3.10', '3.9', '3.8']:
                candidates.append(venv_base / 'lib' / f'python{pyver}' / 'site-packages')
    for path in candidates:
        if (path / 'gns3' / 'main_window.py').exists():
            return path, 'source'

    return None, None


def find_matching_python(pyc_path):
    """Find a Python interpreter matching the .pyc version."""
    version = detect_pyc_version(pyc_path)
    if not version:
        return None, None
    minor = version.split(".")[-1]
    for cmd in [f'python{version}', f'python3.{minor}',
                f'/opt/homebrew/bin/python{version}',
                f'/opt/homebrew/bin/python3.{minor}',
                f'/usr/local/bin/python{version}',
                f'/usr/local/bin/python3.{minor}']:
        try:
            result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                return cmd, version
        except FileNotFoundError:
            continue
    return None, version


# --- macOS bytecode patching ---

def _patch_settings_pyc_subprocess(python_cmd, pyc_path):
    """Patch settings.pyc: add 'Custom' to STYLES tuple."""
    script = '''
import io, marshal, sys

pyc_path = sys.argv[1]
with open(pyc_path, 'rb') as f:
    header = f.read(16)
    code = marshal.load(f)

styles_tuple = ('Charcoal', 'Classic', 'Legacy')
new_styles = ('Custom', 'Charcoal', 'Classic', 'Legacy')

def patch_consts(code_obj):
    changed = False
    new_consts = list(code_obj.co_consts)
    for i, const in enumerate(new_consts):
        if const == styles_tuple:
            new_consts[i] = new_styles
            changed = True
        elif hasattr(const, 'co_consts'):
            patched = patch_consts(const)
            if patched is not const:
                new_consts[i] = patched
                changed = True
    if changed:
        return code_obj.replace(co_consts=tuple(new_consts))
    return code_obj

new_code = patch_consts(code)
if new_code is code:
    for c in code.co_consts:
        if isinstance(c, tuple) and 'Custom' in c:
            print("ALREADY_PATCHED")
            sys.exit(0)
        if hasattr(c, 'co_consts'):
            for cc in c.co_consts:
                if isinstance(cc, tuple) and 'Custom' in cc:
                    print("ALREADY_PATCHED")
                    sys.exit(0)
    print("STYLES_NOT_FOUND")
    sys.exit(1)

buf = io.BytesIO()
buf.write(header)
marshal.dump(new_code, buf)
with open(pyc_path, 'wb') as f:
    f.write(buf.getvalue())
print("PATCHED")
'''
    ret = subprocess.run(
        [python_cmd, '-c', script, str(pyc_path)],
        capture_output=True, text=True)
    output = ret.stdout.strip()
    if ret.returncode != 0:
        error("Patch", f"Failed to patch settings.pyc: {ret.stderr}")
        sys.exit(1)
    if output == 'ALREADY_PATCHED':
        warn("Patch", "settings.pyc already patched")
    elif output == 'PATCHED':
        success("Patch", "Added 'Custom' to STYLES in settings.pyc")


def _patch_pycutext_pyc(python_cmd, pyc_path, hex_color):
    """Patch pycutext.pyc: replace hardcoded black QColor(0,0,0) in write()
    and default (0,0,0) in SyntaxColor.get_color() with theme color."""
    if not pyc_path.exists():
        warn("Patch", "pycutext.pyc not found, skipping")
        return
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    script = f'''
import io, marshal, sys, types, opcode

pyc_path = sys.argv[1]
with open(pyc_path, 'rb') as f:
    header = f.read(16)
    code = marshal.load(f)

LOAD_CONST = opcode.opmap['LOAD_CONST']
R, G, B = {r}, {g}, {b}

def find_code(co, name):
    for c in co.co_consts:
        if isinstance(c, types.CodeType) and c.co_name == name:
            return c
        elif isinstance(c, types.CodeType):
            r = find_code(c, name)
            if r:
                return r
    return None

def patch_write(write_co):
    consts = list(write_co.co_consts)
    r_idx = len(consts)
    consts.append(R)
    g_idx = len(consts)
    consts.append(G)
    b_idx = len(consts)
    consts.append(B)

    bc = bytearray(write_co.co_code)
    zero_idx = None
    for i, c in enumerate(write_co.co_consts):
        if c == 0 and isinstance(c, int):
            zero_idx = i
            break
    if zero_idx is None:
        print("ZERO_NOT_FOUND")
        return write_co

    # Find three consecutive LOAD_CONST zero_idx (the normal text color QColor(0,0,0))
    # Skip the error color pattern (preceded by LOAD_CONST 255)
    patched = False
    for i in range(0, len(bc) - 5, 2):
        if (bc[i] == LOAD_CONST and bc[i] == bc[i+2] == bc[i+4] and
            bc[i+1] == bc[i+3] == bc[i+5] == zero_idx):
            if i >= 2 and bc[i-2] == LOAD_CONST:
                prev_val = write_co.co_consts[bc[i-1]] if bc[i-1] < len(write_co.co_consts) else None
                if prev_val == 255:
                    continue
            bc[i+1] = r_idx
            bc[i+3] = g_idx
            bc[i+5] = b_idx
            patched = True
            break

    if not patched:
        print("PATTERN_NOT_FOUND")
        return write_co

    return write_co.replace(co_consts=tuple(consts), co_code=bytes(bc))

def replace_code(co, old_code, new_code):
    new_consts = list(co.co_consts)
    changed = False
    for i, c in enumerate(new_consts):
        if c is old_code:
            new_consts[i] = new_code
            changed = True
        elif isinstance(c, types.CodeType):
            replaced = replace_code(c, old_code, new_code)
            if replaced is not c:
                new_consts[i] = replaced
                changed = True
    if changed:
        return co.replace(co_consts=tuple(new_consts))
    return co

cls_co = find_code(code, 'PyCutExt')
if not cls_co:
    print("CLASS_NOT_FOUND")
    sys.exit(1)

write_co = find_code(cls_co, 'write')
if not write_co:
    print("WRITE_NOT_FOUND")
    sys.exit(1)

new_code = code
patched_any = False

new_write = patch_write(write_co)
if new_write is not write_co:
    new_code = replace_code(new_code, write_co, new_write)
    patched_any = True

# Patch SyntaxColor.get_color: replace default (0,0,0) tuple with theme color
# This colors typed input text in the console
sc_co = find_code(code, 'SyntaxColor')
if sc_co:
    gc_co = find_code(sc_co, 'get_color')
    if gc_co:
        gc_consts = list(gc_co.co_consts)
        changed = False
        for i, c in enumerate(gc_consts):
            if c == (0, 0, 0):
                gc_consts[i] = (R, G, B)
                changed = True
        if changed:
            new_gc = gc_co.replace(co_consts=tuple(gc_consts))
            new_code = replace_code(new_code, gc_co, new_gc)
            patched_any = True

if not patched_any:
    print("ALREADY_PATCHED")
    sys.exit(0)

buf = io.BytesIO()
buf.write(header)
marshal.dump(new_code, buf)
with open(pyc_path, 'wb') as f:
    f.write(buf.getvalue())
print("PATCHED")
'''
    ret = subprocess.run(
        [python_cmd, '-c', script, str(pyc_path)],
        capture_output=True, text=True)
    if ret.returncode != 0:
        warn("Patch", f"pycutext.pyc patch failed: {ret.stderr.strip()}")
        if ret.stdout.strip():
            warn("Patch", f"pycutext.pyc: {ret.stdout.strip()}")
    elif 'PATCHED' in ret.stdout:
        success("Patch", f"Console text color set to {hex_color}")
    else:
        warn("Patch", f"pycutext.pyc: {ret.stdout.strip()}")


def _patch_link_pyc(python_cmd, pyc_path, hex_color):
    """Patch link item .pyc: replace fallback '#000000' with theme color."""
    if not pyc_path.exists():
        warn("Patch", f"{pyc_path.name} not found, skipping")
        return
    script = '''
import io, marshal, sys, types

pyc_path = sys.argv[1]
new_color = sys.argv[2]
with open(pyc_path, 'rb') as f:
    header = f.read(16)
    code = marshal.load(f)

def patch_consts(co):
    changed = False
    new_consts = list(co.co_consts)
    for i, c in enumerate(new_consts):
        if c == '#000000' and isinstance(c, str):
            new_consts[i] = new_color
            changed = True
        elif isinstance(c, types.CodeType):
            patched = patch_consts(c)
            if patched is not c:
                new_consts[i] = patched
                changed = True
    if changed:
        return co.replace(co_consts=tuple(new_consts))
    return co

new_code = patch_consts(code)
if new_code is code:
    print("NO_CHANGE")
    sys.exit(0)
buf = io.BytesIO()
buf.write(header)
marshal.dump(new_code, buf)
with open(pyc_path, 'wb') as f:
    f.write(buf.getvalue())
print("PATCHED")
'''
    ret = subprocess.run(
        [python_cmd, '-c', script, str(pyc_path), hex_color],
        capture_output=True, text=True)
    if ret.returncode != 0:
        warn("Patch", f"{pyc_path.name} patch failed: {ret.stderr.strip()}")
    elif 'PATCHED' in ret.stdout:
        success("Patch", f"{pyc_path.name} link color set to {hex_color}")
    else:
        warn("Patch", f"{pyc_path.name}: {ret.stdout.strip()}")


# --- macOS style.py template ---

STYLE_PY_TEMPLATE = '''\
"""GNS3 Style module - patched by gns3theme for Custom style support."""
import pathlib
import importlib.util
from gns3.qt import QtCore, QtGui, QtWidgets

# Load original Style class from backup
_orig_path = pathlib.Path("$backup_path")
_OrigStyle = None
if _orig_path.exists():
    try:
        _spec = importlib.util.spec_from_file_location(
            'gns3._style_original', str(_orig_path))
        _orig_mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_orig_mod)
        _OrigStyle = _orig_mod.Style
    except Exception as e:
        import logging
        logging.getLogger(__name__).warning(
            "gns3theme: Could not load original style: %s", e)


def _hex_to_qcolor(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return QtGui.QColor(r, g, b)


class Style:
    """GNS3 GUI Style manager with Custom theme support."""

    def __init__(self, main_window):
        self._mw = main_window
        self._orig = _OrigStyle(main_window) if _OrigStyle else None

    def _getStyleIcon(self, normal_file, active_file):
        if self._orig:
            return self._orig._getStyleIcon(normal_file, active_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(normal_file),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(active_file),
                       QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        return icon

    def setLegacyStyle(self):
        try:
            if self._mw._settings.get("style") == "Custom":
                self.setCustomStyle()
                return
        except Exception:
            pass
        if self._orig:
            self._orig.setLegacyStyle()

    def setClassicStyle(self):
        if self._orig:
            self._orig.setClassicStyle()

    def setCharcoalStyle(self):
        if self._orig:
            self._orig.setCharcoalStyle()

    def setCustomStyle(self):
        """Apply custom theme from ~/.config/gns3theme/"""
        self.setClassicStyle()

        css_path = str(pathlib.Path.home() / '.config' / 'gns3theme' / 'custom_style.css')
        style_file = QtCore.QFile(css_path)
        if style_file.exists():
            try:
                style_file.open(QtCore.QIODeviceBase.OpenModeFlag.ReadOnly)
            except AttributeError:
                style_file.open(QtCore.QFile.ReadOnly)
            css_text = QtCore.QTextStream(style_file).readAll()
            self._mw.setStyleSheet(css_text)

        config_path = pathlib.Path.home() / '.config' / 'gns3theme' / 'config.json'
        config = {}
        if config_path.exists():
            import json
            try:
                config = json.loads(config_path.read_text())
            except Exception:
                pass

        if not config:
            return

        try:
            if hasattr(self._mw, 'uiGraphicsView'):
                gv = self._mw.uiGraphicsView
                settings = gv.settings()
                if 'label_color' in config:
                    settings['default_label_color'] = config['label_color']
                if 'note_color' in config:
                    settings['default_note_color'] = config['note_color']
                if 'grid_color' in config:
                    gc = config['grid_color']
                    r = int(gc[1:3], 16)
                    g = int(gc[3:5], 16)
                    b = int(gc[5:7], 16)
                    gv._drawing_grid_color = QtGui.QColor(r, g, b)
                    lum = 0.1 if (r + g + b) / 3 < 128 else -0.08
                    nr = round(min(max(0, r + r * lum), 255))
                    ng = round(min(max(0, g + g * lum), 255))
                    nb = round(min(max(0, b + b * lum), 255))
                    gv._node_grid_color = QtGui.QColor(nr, ng, nb)

                if 'sbg' in config:
                    hl = _hex_to_qcolor(config['sbg'])
                    palette = gv.palette()
                    try:
                        palette.setColor(QtGui.QPalette.ColorRole.Highlight, hl)
                    except AttributeError:
                        palette.setColor(QtGui.QPalette.Highlight, hl)
                    gv.setPalette(palette)

                if hasattr(gv, 'viewport'):
                    gv.viewport().update()
        except Exception:
            pass

'''


def _write_and_compile_style(python_cmd, gns3_dir, backup_dir):
    """Write patched style.py and compile to .pyc using matching Python."""
    gns3_pkg = Path(gns3_dir) / 'gns3'
    style_pyc = gns3_pkg / 'style.pyc'
    style_py = gns3_pkg / 'style.py'
    backup_pyc = backup_dir / 'style.pyc'

    if style_pyc.exists():
        style_pyc.unlink()

    from string import Template
    style_content = Template(STYLE_PY_TEMPLATE).substitute(backup_path=backup_pyc)
    style_py.write_text(style_content)
    success("Patch", "Wrote patched style.py")

    ret = subprocess.run(
        [python_cmd, '-c',
         f'import py_compile; py_compile.compile("{style_py}", "{style_pyc}", doraise=True)'],
        capture_output=True, text=True)
    if ret.returncode == 0:
        success("Compile", f"Compiled style.pyc with {python_cmd}")
        style_py.unlink()
    else:
        warn("Compile", f"Could not compile style.pyc: {ret.stderr}")
        warn("Compile", "Leaving style.py as source (may not work with frozen apps)")


# --- macOS install ---

def macos_patch_app(src_app, scheme, backup_dir):
    """Patch GNS3.app on macOS: copy to /tmp, patch, move back to /Applications.
    Requires sudo for the final move."""
    import tempfile

    # Always start from the original unpatched app so theme switches work
    bak_app = Path('/Applications/GNS3.app.bak')
    copy_from = bak_app if bak_app.exists() else src_app

    tmp_dir = Path(tempfile.mkdtemp(prefix='gns3theme_'))
    tmp_app = tmp_dir / 'GNS3.app'

    try:
        if copy_from == bak_app:
            success("Copy", "Copying original GNS3.app.bak to temp (this may take a moment)...")
        else:
            success("Copy", "Copying GNS3.app to temp location (this may take a moment)...")
        shutil.copytree(
            copy_from, tmp_app,
            copy_function=shutil.copy,
            symlinks=True,
        )
        success("Copy", f"Created clean copy at {tmp_app}")

        gns3_dir = tmp_app / 'Contents' / 'Resources' / 'lib'
        gns3_pkg = gns3_dir / 'gns3'

        sample_pyc = gns3_pkg / 'settings.pyc'
        python_cmd, pyc_version = find_matching_python(sample_pyc)

        if not python_cmd:
            error("Install",
                  f"GNS3 uses Python {pyc_version} but it's not installed. "
                  f"Install it with: brew install python@{pyc_version}")
            sys.exit(1)

        success("Install", f"Using {python_cmd} for .pyc patching (matches GNS3's Python {pyc_version})")

        # Backup originals
        backup_file(sample_pyc, backup_dir)
        backup_file(gns3_pkg / 'style.pyc', backup_dir)
        for extra in ['pycutext.pyc', 'items/ethernet_link_item.pyc', 'items/serial_link_item.pyc']:
            p = gns3_pkg / extra
            if p.exists():
                backup_file(p, backup_dir)

        # Patch settings.pyc
        _patch_settings_pyc_subprocess(python_cmd, gns3_pkg / 'settings.pyc')

        # Patch console text color
        fg = scheme.get('fg', '#00997a')
        _patch_pycutext_pyc(python_cmd, gns3_pkg / 'pycutext.pyc', fg)

        # Patch link colors
        link_color = scheme.get('lc', scheme.get('fg', '#00997a'))
        _patch_link_pyc(python_cmd, gns3_pkg / 'items' / 'ethernet_link_item.pyc', link_color)
        _patch_link_pyc(python_cmd, gns3_pkg / 'items' / 'serial_link_item.pyc', link_color)

        # Write patched style.py and compile
        _write_and_compile_style(python_cmd, gns3_dir, backup_dir)

        # Re-sign the app
        subprocess.run(
            ['codesign', '--force', '--deep', '--sign', '-', str(tmp_app)],
            capture_output=True)
        success("Sign", "Ad-hoc signed the patched app")

        # Move patched app to /Applications (requires sudo)
        check_sudo('gns3theme -s <scheme>')
        success("Install", "Moving patched GNS3.app to /Applications/...")
        if not bak_app.exists():
            ret = subprocess.run(['sudo', 'cp', '-a', str(src_app), str(bak_app)])
            if ret.returncode != 0:
                error("Install", "Failed to backup original app")
                sys.exit(1)
            success("Backup", f"Original app backed up to {bak_app}")

        ret = subprocess.run(
            ['sudo', 'cp', '-a', str(tmp_app) + '/', str(src_app) + '/'])
        if ret.returncode != 0:
            error("Install", "Failed to copy patched app to /Applications/")
            sys.exit(1)

        success("Install", "Patched GNS3.app installed to /Applications/")
        save_config(scheme)
        return True

    finally:
        if tmp_dir.exists():
            shutil.rmtree(tmp_dir, ignore_errors=True)


# --- Source .py patching ---

def patch_py_settings(file_path, backup_dir):
    """Add 'Custom' to STYLES in settings.py."""
    with open(file_path, 'r') as f:
        content = f.read()
    if re.search(r'STYLES.*Custom', content):
        warn("Patch", "settings.py already patched, skipping")
        return
    backup_file(file_path, backup_dir)
    new_content = re.sub(
        r'(STYLES\s*=\s*\[)',
        r'\1"Custom", ',
        content,
    )
    with open(file_path, 'w') as f:
        f.write(new_content)
    success("Patch", "Added 'Custom' to STYLES in settings.py")


def patch_py_main_window(file_path, backup_dir):
    """Add Custom style dispatch in main_window.py."""
    with open(file_path, 'r') as f:
        content = f.read()
    if 'setCustomStyle' in content:
        warn("Patch", "main_window.py already patched, skipping")
        return
    backup_file(file_path, backup_dir)
    new_content = re.sub(
        r'(\s+)(style\.setLegacyStyle\(\))',
        r'\1if style_name == "Custom":\n\1    style.setCustomStyle()\n\1    return\n\1\2',
        content,
    )
    with open(file_path, 'w') as f:
        f.write(new_content)
    success("Patch", "Added Custom dispatch in main_window.py")


CUSTOM_STYLE_METHOD = '''
    @staticmethod
    def _hex_to_qcolor(hex_color):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        return QtGui.QColor(r, g, b)

    @staticmethod
    def _patch_console_color(mw, theme_color):
        try:
            console = mw.findChild(QtCore.QObject, 'uiConsoleTextEdit')
            if not console or not hasattr(console, 'write'):
                return
            klass = type(console)
            if getattr(klass, '_gns3theme_patched', False):
                return
            base_stc = None
            for base in klass.__mro__:
                if base.__name__ in ('QTextEdit', 'QPlainTextEdit'):
                    base_stc = base.setTextColor
                    break
            if base_stc is None:
                base_stc = klass.setTextColor
            tc = theme_color
            def _themed_stc(self, color, _orig=base_stc, _tc=tc):
                if color.red() == 0 and color.green() == 0 and color.blue() == 0:
                    _orig(self, _tc)
                else:
                    _orig(self, color)
            klass.setTextColor = _themed_stc
            klass._gns3theme_patched = True
        except Exception:
            pass

    def setCustomStyle(self):
        """Apply custom theme from ~/.config/gns3theme/"""
        import pathlib, json
        self.setClassicStyle()
        css_path = str(pathlib.Path.home() / '.config' / 'gns3theme' / 'custom_style.css')
        style_file = QtCore.QFile(css_path)
        if style_file.exists():
            try:
                style_file.open(QtCore.QIODeviceBase.OpenModeFlag.ReadOnly)
            except AttributeError:
                style_file.open(QtCore.QFile.ReadOnly)
            css_text = QtCore.QTextStream(style_file).readAll()
            self._mw.setStyleSheet(css_text)
        config_path = pathlib.Path.home() / '.config' / 'gns3theme' / 'config.json'
        config = {}
        if config_path.exists():
            try:
                config = json.loads(config_path.read_text())
            except Exception:
                pass
        if not config:
            return
        try:
            if hasattr(self._mw, 'uiGraphicsView'):
                gv = self._mw.uiGraphicsView
                settings = gv.settings()
                if 'label_color' in config:
                    settings['default_label_color'] = config['label_color']
                if 'note_color' in config:
                    settings['default_note_color'] = config['note_color']
                if 'grid_color' in config:
                    gc = config['grid_color']
                    r = int(gc[1:3], 16)
                    g = int(gc[3:5], 16)
                    b = int(gc[5:7], 16)
                    gv._drawing_grid_color = QtGui.QColor(r, g, b)
                    lum = 0.1 if (r + g + b) / 3 < 128 else -0.08
                    nr = round(min(max(0, r + r * lum), 255))
                    ng = round(min(max(0, g + g * lum), 255))
                    nb = round(min(max(0, b + b * lum), 255))
                    gv._node_grid_color = QtGui.QColor(nr, ng, nb)
                if 'sbg' in config:
                    hl = self._hex_to_qcolor(config['sbg'])
                    palette = gv.palette()
                    try:
                        palette.setColor(QtGui.QPalette.ColorRole.Highlight, hl)
                    except AttributeError:
                        palette.setColor(QtGui.QPalette.Highlight, hl)
                    gv.setPalette(palette)
                if hasattr(gv, 'viewport'):
                    gv.viewport().update()
        except Exception:
            pass
        if 'console_color' in config:
            tc = self._hex_to_qcolor(config['console_color'])
            self._patch_console_color(self._mw, tc)
            QtCore.QTimer.singleShot(2000,
                lambda mw=self._mw, c=tc: Style._patch_console_color(mw, c))
'''


def patch_py_style(file_path, backup_dir):
    """Add setCustomStyle method to style.py."""
    with open(file_path, 'r') as f:
        content = f.read()
    if 'setCustomStyle' in content:
        warn("Patch", "style.py already patched, skipping")
        return
    backup_file(file_path, backup_dir)
    new_content = content.rstrip() + '\n' + CUSTOM_STYLE_METHOD
    with open(file_path, 'w') as f:
        f.write(new_content)
    success("Patch", "Added setCustomStyle to style.py")


def restore_from_backup(file_path, backup_dir):
    """Restore a single file from backup if one exists (for re-patching)."""
    bak = backup_dir / Path(file_path).name
    if bak.exists():
        shutil.copy(bak, file_path)


def patch_py_link_item(file_path, hex_color, backup_dir):
    """Patch link item .py: replace fallback '#000000' with theme color."""
    if not file_path.exists():
        warn("Patch", f"{file_path.name} not found, skipping")
        return
    # Restore original before patching so we always replace from clean state
    restore_from_backup(file_path, backup_dir)
    with open(file_path, 'r') as f:
        content = f.read()
    if '#000000' not in content:
        warn("Patch", f"{file_path.name}: no #000000 to replace, skipping")
        return
    backup_file(file_path, backup_dir)
    new_content = content.replace('#000000', hex_color)
    with open(file_path, 'w') as f:
        f.write(new_content)
    success("Patch", f"{file_path.name} link color set to {hex_color}")


def patch_py_pycutext(file_path, hex_color, backup_dir):
    """Patch pycutext.py: replace hardcoded black colors in write() and
    SyntaxColor.get_color() with the theme foreground color."""
    if not file_path.exists():
        warn("Patch", f"{file_path.name} not found, skipping")
        return
    # Restore original before patching so we always replace from clean state
    restore_from_backup(file_path, backup_dir)
    with open(file_path, 'r') as f:
        content = f.read()
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    new_qcolor = f'QColor({r}, {g}, {b})'
    new_tuple = f'({r}, {g}, {b})'
    patched = False
    new_content = content
    # Patch write() default color: QColor(0, 0, 0)
    if 'QColor(0, 0, 0)' in new_content:
        new_content = new_content.replace('QColor(0, 0, 0)', new_qcolor)
        patched = True
    # Patch SyntaxColor.get_color() default return: (0, 0, 0)
    # This is the tuple returned for non-keyword input text
    if 'return (0, 0, 0)' in new_content:
        new_content = new_content.replace('return (0, 0, 0)', f'return {new_tuple}')
        patched = True
    if not patched:
        warn("Patch", f"{file_path.name}: no black color patterns to replace, skipping")
        return
    backup_file(file_path, backup_dir)
    with open(file_path, 'w') as f:
        f.write(new_content)
    success("Patch", f"Console text color set to {hex_color}")


def install_patches_source(gns3_dir, scheme, backup_dir):
    """Patch GNS3 .py source files (pip/brew/source installs)."""
    gns3_pkg = Path(gns3_dir) / 'gns3'
    import os
    if not os.access(gns3_pkg / 'settings.py', os.W_OK):
        error("PermissionError",
              f"No write access to {gns3_pkg}. Try running with sudo")
        sys.exit(1)
    patch_py_settings(gns3_pkg / 'settings.py', backup_dir)
    patch_py_main_window(gns3_pkg / 'main_window.py', backup_dir)
    patch_py_style(gns3_pkg / 'style.py', backup_dir)

    # Patch console text color
    fg = scheme.get('fg', '#d8dee9')
    patch_py_pycutext(gns3_pkg / 'pycutext.py', fg, backup_dir)

    # Patch link colors
    link_color = scheme.get('lc', scheme.get('fg', '#d8dee9'))
    patch_py_link_item(gns3_pkg / 'items' / 'ethernet_link_item.py', link_color, backup_dir)
    patch_py_link_item(gns3_pkg / 'items' / 'serial_link_item.py', link_color, backup_dir)

    save_config(scheme)
    success("Install", "Patching complete!")


# --- CSS generation ---

def generate_custom_css(data):
    """Generate CSS string from selector-properties dict."""
    parts = []
    for selector, properties in data.items():
        parts.append(f'{selector}{{\n')
        for prop, value in properties.items():
            parts.append(f'\t{prop}: {value};\n')
        parts.append('}\n')
    return ''.join(parts)


def update_style(scheme):
    """Map color scheme to CSS selectors and generate CSS."""
    style = deepcopy(css.custom_style)

    color_map = {
        'bg': [
            (css.selector00, 'background-color'),
            (css.selector01, 'background-color'),
            (css.selector05, 'background-color'),
            (css.selector18, 'background-color'),
            (css.selector21, 'background'),
        ],
        'bg2': [
            (css.selector04, 'background-color'),
            (css.selector07, 'background'),
            (css.selector07, 'background-color'),
            (css.selector08, 'background'),
            (css.selector13, 'background-color'),
            (css.selector16, 'background-color'),
            (css.selector22, 'background'),
            (css.selector22, 'background-color'),
            (css.selector23, 'background'),
            (css.selector23, 'background-color'),
        ],
        'fg': [
            (css.selector03, 'color'),
            (css.selector04, 'color'),
            (css.selector05, 'color'),
            (css.selector07, 'color'),
            (css.selector13, 'color'),
            (css.selector14, 'color'),
            (css.selector15, 'color'),
            (css.selector16, 'color'),
            (css.selector18, 'color'),
            (css.selector19, 'color'),
            (css.selector20, 'color'),
            (css.selector28, 'color'),
            (css.selector29, 'color'),
            (css.selector31, 'color'),
        ],
        'fg2': [
            (css.selector09, 'color'),
            (css.selector32, 'color'),
        ],
        'tbg': [
            (css.selector02, 'background'),
            (css.selector10, 'background'),
            (css.selector12, 'background'),
            (css.selector14, 'background-color'),
            (css.selector15, 'alternate-background-color'),
            (css.selector28, 'background-color'),
            (css.selector31, 'background-color'),
        ],
        'sbg': [
            (css.selector11, 'selection-background-color'),
            (css.selector15, 'background-color'),
            (css.selector17, 'background-color'),
        ],
        'sfg': [
            (css.selector08, 'color'),
            (css.selector11, 'selection-color'),
            (css.selector17, 'color'),
        ],
    }

    for key, mappings in color_map.items():
        if key in scheme:
            for selector, prop in mappings:
                style[selector][prop] = scheme[key]

    # Selected tab accent border
    if 'sfg' in scheme:
        style[css.selector08]['border-bottom'] = f"2px solid {scheme['sfg']}"

    # Title label bottom accent
    if 'fg2' in scheme:
        style[css.selector20]['border-bottom'] = f"2px solid {scheme['fg2']}"

    # Brighten tab background so flat tabs visually match framed buttons
    if 'bg2' in scheme:
        hc = scheme['bg2'].lstrip('#')
        r, g, b = int(hc[0:2], 16), int(hc[2:4], 16), int(hc[4:6], 16)
        tab_bg = f'#{min(255, r + 20):02x}{min(255, g + 20):02x}{min(255, b + 20):02x}'
        style[css.selector07]['background'] = tab_bg
        style[css.selector07]['background-color'] = tab_bg

    # Lighten button text slightly for better readability
    if 'fg' in scheme:
        hc = scheme['fg'].lstrip('#')
        r, g, b = int(hc[0:2], 16), int(hc[2:4], 16), int(hc[4:6], 16)
        btn_fg = f'#{min(255, int(r + (255 - r) * 0.25)):02x}' \
                 f'{min(255, int(g + (255 - g) * 0.25)):02x}' \
                 f'{min(255, int(b + (255 - b) * 0.25)):02x}'
        style[css.selector13]['color'] = btn_fg
        style[css.selector14]['color'] = btn_fg

    return generate_custom_css(style)


# --- Config ---

def parse_scheme_args(scheme, args):
    """Override scheme colors with CLI arguments."""
    overrides = {
        'bg': args.bg, 'bg2': args.bg2, 'fg': args.fg, 'fg2': args.fg2,
        'tbg': args.tbg, 'sbg': args.sbg, 'sfg': args.sfg,
        'lc': args.lc, 'gc': args.gc, 'lbl': args.lbl,
    }
    for key, value in overrides.items():
        if value:
            scheme[key] = f"#{value.strip('#')}"
    if args.lw:
        scheme['lw'] = float(args.lw)
    return scheme


def save_config(scheme):
    """Save runtime config for setCustomStyle (grid/link/label/console colors)."""
    config = {}
    if scheme.get('gc') and scheme['gc'] != 'default':
        config['grid_color'] = scheme['gc']
    fg = scheme.get('fg')
    if fg:
        config['label_color'] = scheme.get('lbl', fg)
        config['note_color'] = scheme.get('lbl', fg)
        config['link_color'] = scheme.get('lc', fg)
        config['console_color'] = fg
    if scheme.get('sbg'):
        config['sbg'] = scheme['sbg']
    mkdir(CONFIG_DIR)
    CONFIG_PATH.write_text(json.dumps(config, indent=2))
    success("Config", f"Saved config to {CONFIG_PATH}")


# --- Symbols ---

def install_symbols():
    """Copy bundled SVG symbols to ~/GNS3/symbols/."""
    if not BUNDLED_SYMBOLS_DIR.is_dir():
        error("Symbols", f"Bundled symbols not found at {BUNDLED_SYMBOLS_DIR}")
        sys.exit(1)

    svgs = sorted(BUNDLED_SYMBOLS_DIR.glob('*.svg'))
    if not svgs:
        error("Symbols", "No SVG files found in bundled symbols directory")
        sys.exit(1)

    mkdir(GNS3_SYMBOLS_DIR)

    installed = 0
    skipped = 0
    for svg in svgs:
        dest = GNS3_SYMBOLS_DIR / svg.name
        if dest.exists():
            skipped += 1
            continue
        shutil.copy2(svg, dest)
        installed += 1

    if installed:
        success("Symbols", f"Installed {installed} symbols to {GNS3_SYMBOLS_DIR}")
    if skipped:
        warn("Symbols", f"Skipped {skipped} symbols (already exist)")
    if installed:
        print(f"\n{GREEN}Done!{RESET} Symbols are available in GNS3 symbol selection dialog.")


# --- Restore ---

def check_sudo(hint=''):
    """Validate sudo access before performing privileged operations."""
    ret = subprocess.run(['sudo', '-n', 'true'], capture_output=True)
    if ret.returncode != 0:
        msg = "This operation requires sudo."
        if hint:
            msg += f" Run with: sudo {hint}"
        error("PermissionError", msg)
        sys.exit(1)


def restore_macos():
    """Restore original GNS3.app from backup."""
    bak_app = Path('/Applications/GNS3.app.bak')
    if not bak_app.exists():
        warn("Restore", "No backup found at /Applications/GNS3.app.bak")
        return
    check_sudo('gns3theme --restore')
    success("Restore", "Restoring original GNS3.app...")
    ret = subprocess.run(['sudo', 'cp', '-a', str(bak_app), str(MACOS_GNS3_APP)])
    if ret.returncode != 0:
        error("Restore", "Failed to restore backup")
        sys.exit(1)
    success("Restore", "Original GNS3.app restored (backup kept at GNS3.app.bak)")


def restore_source(gns3_dir):
    """Restore original GNS3 files from backups."""
    gns3_pkg = Path(gns3_dir) / 'gns3'
    backup_dir = CONFIG_DIR / 'backups'
    restored = False

    import os
    if gns3_pkg.exists() and not os.access(gns3_pkg, os.W_OK):
        error("PermissionError",
              f"No write access to {gns3_pkg}. Try running with sudo")
        sys.exit(1)

    # Map backup filenames to their relative paths under gns3_pkg
    restore_map = {
        'settings.pyc': 'settings.pyc',
        'settings.py': 'settings.py',
        'main_window.py': 'main_window.py',
        'style.py': 'style.py',
        'pycutext.py': 'pycutext.py',
        'ethernet_link_item.py': 'items/ethernet_link_item.py',
        'serial_link_item.py': 'items/serial_link_item.py',
    }

    for name, rel_path in restore_map.items():
        bak = backup_dir / name
        if bak.exists():
            target = gns3_pkg / rel_path
            shutil.copy(bak, target)
            success("Restore", f"Restored {name}")
            restored = True

    if not restored:
        warn("Restore", f"No backups found in {backup_dir}")
    else:
        success("Restore", "All files restored to original state")


# --- Main ---

def main():
    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    if args.list_schemes:
        print_colorschemes()
        return

    if args.install_symbols:
        install_symbols()
        if not args.color_scheme:
            return

    if args.restore:
        if args.restore == 'auto':
            gns3_lib, install_type = find_gns3_lib()
            if not gns3_lib:
                error("Restore",
                      "Could not find GNS3 installation. "
                      "Specify the path manually: --restore /path/to/site-packages")
                sys.exit(1)
            if install_type == 'app':
                restore_macos()
            else:
                restore_source(str(gns3_lib))
        else:
            # User specified path — could be macOS source or Linux
            restore_source(args.restore)
        return

    if not args.color_scheme:
        error("OptionError", "--scheme is required. Use --help for usage")
        sys.exit(1)

    validate_scheme(args.color_scheme)
    all_schemes = get_all_schemes()
    scheme = deepcopy(all_schemes[args.color_scheme])
    scheme = parse_scheme_args(scheme, args)

    # Generate CSS and install
    mkdir(CONFIG_DIR)
    style_css = update_style(scheme)
    save_file(style_css, str(CSS_PATH))

    backup_dir = CONFIG_DIR / 'backups'

    if args.gns3_dir:
        # User-specified path — always source (.py) install
        gns3_dir = args.gns3_dir
        p = Path(gns3_dir)
        if not p.is_dir():
            error("InstallError", f"Directory does not exist: '{gns3_dir}'")
            sys.exit(1)
        if not (p / 'gns3' / 'main_window.py').exists():
            error("InstallError",
                  f"No GNS3 package found in '{gns3_dir}'. "
                  "Path should be the site-packages directory containing gns3/")
            sys.exit(1)
        success("Install", f"Using GNS3 at {gns3_dir}")
        install_patches_source(gns3_dir, scheme, backup_dir)
    else:
        # Auto-detect
        gns3_lib, install_type = find_gns3_lib()
        if not gns3_lib:
            error("InstallError",
                  "Could not find GNS3 installation. "
                  "Specify the path manually: --gns3-dir /path/to/site-packages")
            sys.exit(1)

        if install_type == 'app':
            success("AutoDetect", f"Found GNS3.app at {MACOS_GNS3_APP}")
            macos_patch_app(MACOS_GNS3_APP, scheme, backup_dir)
        else:
            success("AutoDetect", f"Found GNS3 at {gns3_lib}")
            install_patches_source(str(gns3_lib), scheme, backup_dir)

    print(f"\n{GREEN}Done!{RESET} Restart GNS3 and select "
          f"Edit -> Preferences -> General -> Interface Style -> {GREEN}Custom{RESET}")


if __name__ == "__main__":
    main()
