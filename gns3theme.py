#!/usr/bin/env python3

import re
import os
import sys
from pathlib import Path
from colorschemes import schemes
from argparser import parser
import custom_style as css
import subprocess


def is_valid_color(color):
    """validate color"""
    if re.fullmatch(r'#[0-9a-fA-f]{6}', color):
        return True
    return False


def is_valid_opacity(opacity_num):
    """validate opacity"""
    if re.fullmatch(r'0\.[0-9]{,2}|1.0', opacity_num):
        return True
    return False


def is_root():
    """Check if the script has been run as root"""
    if os.getuid() != 0:
        return False
    return True


def print_colorschemes():
    """ Print colorschemes """
    for th_name, th_color in schemes.items():
        print(f"{th_name}")
    print("\nAdd your colorscheme in 'colorschemes.py' file")


def is_valid_scheme(scheme):
    """ validate color scheme """
    if scheme not in schemes:
        print(f"\033[91mSchemeValidation\033[0m: Invalid colorscheme '{scheme}'. "
              f"Use 'gns3theme --list' to list available colorschemes")


def hex_to_rgb(hex_color, nobraces=False, tup=False):
    """convert hex color to rgb"""
    is_ok = is_valid_color(hex_color)
    if is_ok:
        hc = hex_color.lstrip("#")
        rgb = tuple(int(hc[i:i+2], 16) for i in range(0, len(hc), 2))
    else:
        print(f"\033[91ColorValidation\033[0m: Invalid color format '{hex_color}'")
        sys.exit(1)
    if tup:
        return rgb
    elif nobraces:
        return str(rgb).strip(')').strip('(')
    return str(rgb)


def update_gns3_ui(scheme, src_dir, username, home_dir=None):
    """
    Update gns3_gui files
    Args
        scheme (dict): colorscheme to apply
        src_dir (path): path to gns3_gui dir
        custom_style_path (str): custom_style.css save location
    Returns:
        True (bool): if succussfully update scheme
        False (bool): otherwise
    """
    if sys.platform == 'linux':
        home_dir = f"/home/{username}"
    elif sys.platform == 'darwin':
        home_dir = f"/Users/{username}"
    custom_style_path = f"{home_dir}.config/gns3theme/custom_style.css"
    # mkdir(Path(custom_style_path).parent)
    gns3_main_window_path = f"{src_dir}gns3/main_window.py"
    gns3_style_path = f"{src_dir}gns3/style.py"
    gns3_settings_path = f"{src_dir}gns3/settings.py"
    gns3_graphics_view_path = f"{src_dir}gns3/graphics_view.py"
    gns3_ethernet_link_item_path = f"{src_dir}gns3/items/ethernet_link_item.py"

    # apply patch
    tab = ' '*4
    new_main_window = None
    new_settings = None
    new_style = None
    new_graphics_view = None
    print("\033[92mPatchFile\033[0m: Start Patching gns3_gui source code")
    with open(gns3_main_window_path, 'r') as fh:
        contents = fh.read()
        if not re.search(r"style.setCustomStyle", contents):
            new_main_window = re.sub(r"(\s+)(style.setCharcoalStyle\(\))",
                                     f'\\1\\2\n{tab*2}elif style_name == "Custom":\\1style.setCustomStyle()',
                                     contents,
                                     re.M)
            print("\033[92mPatchFile\033[0m: Updated gns3_gui main_window.py")
        else:
            print("\033[93mPatchFile\033[0m: File already patched gns3_gui main_window.py, skipping..")

    with open(gns3_settings_path, 'r') as fh:
        contents = fh.read()
        if not re.search(r"STYLES.*Custom", contents):
            new_settings = re.sub(r"(STYLES\s+=\s+\[)(.*?])",
                                  r'\1"Custom", \2',
                                  contents,
                                  re.M)
            print("\033[92mPatchFile\033[0m: Updated gns3_gui settings.py")
        else:
            print("\033[93mPatchFile\033[0m: File already patched gns3_gui settings.py, skipping..")

    add_style_func = (f"{tab}def setCustomStyle(self):\n"
                      f"{tab*2}self.setClassicStyle()\n"
                      f"{tab*2}style_file = QtCore.QFile(\"{custom_style_path}\")\n"
                      f"{tab*2}style_file.open(QtCore.QFile.ReadOnly)\n"
                      f"{tab*2}style = QtCore.QTextStream(style_file).readAll()\n"
                      f"{tab*2}self._mw.setStyleSheet(style)\n")
    with open(gns3_style_path, 'r') as fh:
        contents = fh.read()
        if not re.search(r"setCustomStyle", contents):
            new_style = f"{contents}\n{add_style_func}"
            print("\033[92mPatchFile\033[0m: Updated gns3_gui style.py")
        else:
            print("\033[93mPatchFile\033[0m: File already patched gns3_gui style.py, skipping..")

    if scheme['gc'] != 'default':
        print("\033[92mPatchFile\033[0m: Changed gns3_gui grid color")
        if scheme['color'] == 'light':
            new_graphics_view = change_grid_color(scheme['gc'], dark=True, file_path=gns3_graphics_view_path)
        else:
            new_graphics_view = change_grid_color(scheme['gc'], light=True, file_path=gns3_graphics_view_path)

    if scheme['lc'] != 'default':
        new_ethernet_link_item = change_link_color(scheme['lc'], light=True, file_path=gns3_ethernet_link_item_path)
        print("\033[92mPatchFile\033[0m: Changed ethernet_link_item color")

    print("\033[92mPatchFile\033[0m: Finished patching gns3_gui source code")

    save_file(new_main_window, gns3_main_window_path)
    save_file(new_settings, gns3_settings_path)
    save_file(new_style, gns3_style_path)
    save_file(new_graphics_view, gns3_graphics_view_path)
    save_file(new_ethernet_link_item, gns3_ethernet_link_item_path)

    return True


def cleanup():
    """
    Delete old gns3 gui installation.
    """
    try:
        output = subprocess.run(['python3', '-m', 'pip', 'uninstall', 'gns3-gui', '-y'], stderr=subprocess.PIPE)
    except Exception as err:
        print(f"\033[91mCleanupError\033[0m: Failed to cleanup, {err}")
    else:
        if 'WARNING' in output.stderr.decode('utf-8'):
            print(f"\033[93mCleanup\033[0m: {output.stderr.decode('utf-8')}")
        else:
            print("\033[92mCleanup\033[0m: Removed old gns3_gui installation")


def generate_custom_css(data=None):
    """
    Create custom style
    Args:
        data (dir): css data represented in dict format
    """
    print("\033[92mCSSFormat\033[0m: Generating new CSS format")
    css_str = []
    if not data:
        data = css.custom_style
    for selectors, properties in data.items():
        css_str.append(selectors+'{\n')
        for property, value in properties.items():
            css_str.append(f"\t{property}: {value};\n")
        css_str.append("}\n")
    return ''.join(css_str)


def update_style(scheme):
    """
    Update default css data
    Args:
        scheme (dict): a predefined color schemes
    Returns:
        new_scheme (dict): new color scheme
    """
    new_scheme = css.custom_style
    for p, v in scheme.items():
        if p == 'bg':
            new_scheme[css.selector00]['background-color'] = v
            new_scheme[css.selector01]['background-color'] = v
            new_scheme[css.selector05]['background-color'] = v
            new_scheme[css.selector15]['background-color'] = v
            new_scheme[css.selector18]['background-color'] = v
            new_scheme[css.selector21]['background'] = v
            new_scheme[css.selector22]['background-color'] = v
            new_scheme[css.selector23]['background-color'] = v
        elif p == 'bg2':
            new_scheme[css.selector04]['background-color'] = v
            new_scheme[css.selector07]['background-color'] = v
            new_scheme[css.selector15]['background-color'] = v
            new_scheme[css.selector16]['background-color'] = v
            new_scheme[css.selector20]['color'] = v
            new_scheme[css.selector22]['background-color'] = v
            new_scheme[css.selector23]['background-color'] = v
        elif p == 'fg':
            new_scheme[css.selector03]['color'] = v
            new_scheme[css.selector04]['color'] = v
            new_scheme[css.selector05]['color'] = v
            new_scheme[css.selector07]['color'] = v
            new_scheme[css.selector15]['color'] = v
            new_scheme[css.selector16]['color'] = v
            new_scheme[css.selector18]['color'] = v
            new_scheme[css.selector19]['color'] = v
            new_scheme[css.selector28]['color'] = v
            new_scheme[css.selector29]['color'] = v
        elif p == 'fg2':
            new_scheme[css.selector09]['color'] = v
        elif p == 'tbg':
            new_scheme[css.selector02]['background'] = v
            new_scheme[css.selector10]['background'] = v
            new_scheme[css.selector12]['background'] = v
            new_scheme[css.selector14]['background-color'] = v
            new_scheme[css.selector28]['background-color'] = v
        elif p == 'sbg':
            new_scheme[css.selector11]['selection-background-color'] = v
            new_scheme[css.selector17]['background-color'] = v
        elif p == 'sfg':
            new_scheme[css.selector08]['color'] = v
            new_scheme[css.selector11]['selection-color'] = v
            new_scheme[css.selector17]['color'] = v
        elif p == 'bbg':
            new_scheme[css.selector13]['background-color'] = v
            new_scheme[css.selector08]['background'] = v
        elif p == 'bfg':
            new_scheme[css.selector13]['color'] = v
            new_scheme[css.selector14]['color'] = v
            new_scheme[css.selector08]['color'] = v
        elif p == 'lc':
            # not needed anymore
            # change_link_color(v)
            pass
        elif p == 'lw':
            # not implemented
            # change_link_width(v)
            pass
    new_scheme = generate_custom_css(new_scheme)
    return new_scheme


def change_link_color(link_color, light=False, dark=False, file_path=None):
    """
    Change link color based on the select theme. Only new projects will be affected.
    Old projects will maintains their original link color.
    """

    with open(file_path, 'r') as fh:
        contents = fh.read()
        new_ethernet_link_item = re.sub(r"(\s+self.setPen\(QtGui.QPen\(QtGui.QColor\(\").*?(\"\).*)",
                                        f"\\1{link_color}\\2",
                                        contents,
                                        re.M)
    return new_ethernet_link_item


def color_luminate(color, lighten=False, darken=False, lum=0):
    """
    Get Lighter/Darker variant of hex color
    Args:
        color (str): hex/rgb color format
        lum (int): 0 to 1 for lighter color, 0 to -1 for darker color
                  e.g. lum=0.2, lum=-0.5
    Returns:
        rr, gg, bb
    """
    if lighten:
        lum = 0.1
    elif darken:
        lum = -0.08
    if is_valid_color(color):
        color = hex_to_rgb(color, tup=True)
    r = color[0]
    g = color[1]
    b = color[2]
    r = round(min(max(0, r + r * lum), 255))
    g = round(min(max(0, g + g * lum), 255))
    b = round(min(max(0, b + b * lum), 255))
    return f"({r}, {g}, {b})"


def change_grid_color(grid_color, dark=False, light=False, file_path=None):
    """
    Change grid color to fit the current theme
    """
    drawing_grid_color = hex_to_rgb(grid_color)
    node_grid_color = color_luminate(grid_color, darken=dark, lighten=light)
    gns3_graphics_view_path = file_path

    with open(gns3_graphics_view_path, 'r') as fh:
        contents = fh.read()
        new_graphics_view = re.sub(r"(\s+)(grids\s+=\s+.*?QtGui.QColor).*?\)",
                                   f"\\1\\2{drawing_grid_color}",
                                   contents,
                                   re.M)
        new_graphics_view = re.sub(r"(\s+)(\(self.nodeGridSize.*?QtGui.QColor).*?\)",
                                   f"\\1\\2{node_grid_color}",
                                   new_graphics_view,
                                   re.M)
    return new_graphics_view


def save_file(data, file_path):
    """
    Write data to the given file
    Args:
        data (str): data to be written to file
        file_path (str): absolut path to file
    """
    if not data:
        return
    try:
        with open(file_path, 'w') as fh:
            fh.write(data)
    except TypeError as err:
        print(f"\033[91m{err}\033[0m")
        sys.exit(1)
    else:
        print(f"\033[920mCreateFile\033[0m: Created new \033[92m{file_path}\033[0m")
        return True


def mkdir(dir_path):
    """
    Create new directory if not exist
    """
    try:
        Path.mkdir(Path(dir_path), parents=True, exist_ok=True)
    except OSError as err:
        print(err)
        sys.exit(1)
    else:
        return dir_path


def is_dir_exists(dir_path):
    """check if dir exist"""
    if Path(dir_path).is_dir():
        return True
    return False


def install_gns3_gui(gns3_gui_dir):
    """
    Apply changes and install
    """
    # cleanup previous gns3_gui installation
    if not is_root():
        print("\033[91mInstallError\033[0m: Please run as root")
        exit(1)
    cleanup()
    cmd = f"cd {gns3_gui_dir}; python3 setup.py install"
    try:
        subprocess.run(['sh', '-c', cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as err:
        print(f"\033[91mInstall\033[0m: Could not install gns3_gui, {err}")
        exit(1)
    else:
        print("\033[92mInstall\033[0m: Successfully installed gns3_gui")


def parse_scheme_args(scheme, **kwargs):
    """parse schemes options supplied via command line"""
    if kwargs['bg']:  scheme['bg']  = f"#{kwargs['bg'].strip('#')}"
    if kwargs['bg2']: scheme['bg2'] = f"#{kwargs['bg2'].strip('#')}"
    if kwargs['fg']:  scheme['fg']  = f"#{kwargs['fg'].strip('#')}"
    if kwargs['fg2']: scheme['fg2'] = f"#{kwargs['fg2'].strip('#')}"
    if kwargs['tbg']: scheme['tbg'] = f"#{kwargs['tbg'].strip('#')}"
    if kwargs['sbg']: scheme['sbg'] = f"#{kwargs['sbg'].strip('#')}"
    if kwargs['sfg']: scheme['sfg'] = f"#{kwargs['sfg'].strip('#')}"
    if kwargs['bbg']: scheme['bbg'] = f"#{kwargs['bbg'].strip('#')}"
    if kwargs['lc']:  scheme['lc']  = f"#{kwargs['lc'].strip('#')}"
    if kwargs['lw']:  scheme['lw']  = f"#{kwargs['lw'].strip('#')}"
    if kwargs['gc']:  scheme['gc']  = f"#{kwargs['gc'].strip('#')}"

    return scheme


def main():
    """main"""

    args = parser.parse_args()
    if args.install_scheme:
        gns3_gui_dir = args.install_scheme
        if not args.color_scheme:
            print("\033[91mInstallError\033[0m: --install requires --scheme option to work")
            exit(1)
        if not args.username:
            print("\033[91mInstallError\033[0m: --install requires --username option to work")
            exit(1)
        if not is_root():
            print("\033[91mInstallError\033[0m: Please run as root")
            exit(1)
        is_valid_scheme(args.color_scheme)
        if not is_dir_exists(args.install_scheme):
            print("\033[91mInstallError\033[0m: Director does not exists '{args.install_scheme}'")

        scheme = schemes[args.color_scheme]
        scheme = parse_scheme_args(scheme, bg=args.bg, bg2=args.bg2, fg=args.fg, fg2=args.fg2, tbg=args.tbg,
                                   sbg=args.sbg, sfg=args.sfg, bbg=args.bbg, lc=args.lc, lw=args.lw, gc=args.gc)
        update_style(scheme)
        update_gns3_ui(scheme, gns3_gui_dir, args.username)
        #install_gns3_gui(gns3_gui_dir)
    elif args.color_scheme and not args.install_scheme:
        if is_root():
            print("\033[91mInstallError\033[0m: Please run as nonroot")
            exit(1)
        custom_style_path = f"{Path.home()}/.config/gns3theme/custom_style.css"
        mkdir(Path(custom_style_path).parent)

        scheme = schemes[args.color_scheme]

        scheme = parse_scheme_args(scheme, bg=args.bg, bg2=args.bg2, fg=args.fg, fg2=args.fg2, tbg=args.tbg,
                                   sbg=args.sbg, sfg=args.sfg, bbg=args.bbg, lc=args.lc, lw=args.lw, gc=args.gc)
        style = update_style(scheme)
        save_file(style, custom_style_path)
    elif args.list_schemes:
        print_colorschemes()
    else:
        print("\033[91mOptionError\033[0m: --install/--scheme are required")
        exit(1)


if __name__ == "__main__":
    main()
