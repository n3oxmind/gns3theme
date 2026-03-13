"""
Predefined color schemes for gns3theme.

Each scheme is a dict with these keys:

    bg     main background color
    bg2    secondary background (sidebars, fields, inputs)
    fg     foreground / text color
    fg2    accent color (section headers, group titles)
    sbg    selection background color
    sfg    selection foreground color
    tbg    toolbar / statusbar background color
    lc     link color (ethernet/serial links on canvas)
    lw     link width (float, default 1.2)
    gc     grid color (subtle, near bg)
    color  theme type: 'light' or 'dark'

To add your own scheme, either:
  1. Add it to this file and submit a PR, or
  2. Drop a JSON file in ~/.config/gns3theme/schemes/
     (see README for the JSON format)
"""

schemes = {

    # -------------------------------------------------------------------------
    # Solarized  —  Ethan Schoonover
    # -------------------------------------------------------------------------

    'solarized-light': {
        'bg':    '#fdf6e3',
        'bg2':   '#eee8d5',
        'fg':    '#657b83',
        'fg2':   '#268bd2',
        'sbg':   '#268bd2',
        'sfg':   '#fdf6e3',
        'tbg':   '#eee8d5',
        'lc':    '#657b83',
        'lw':    1.2,
        'gc':    '#f5edda',
        'color': 'light',
    },
    'solarized-dark': {
        'bg':    '#002b36',
        'bg2':   '#073642',
        'fg':    '#839496',
        'fg2':   '#268bd2',
        'sbg':   '#073642',
        'sfg':   '#93a1a1',
        'tbg':   '#073642',
        'lc':    '#839496',
        'lw':    1.2,
        'gc':    '#003d4d',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # Gruvbox  —  morhetz
    # -------------------------------------------------------------------------

    'gruvbox-light': {
        'bg':    '#fbf1c7',
        'bg2':   '#ebdbb2',
        'fg':    '#3c3836',
        'fg2':   '#504945',
        'sbg':   '#d5c4a1',
        'sfg':   '#3c3836',
        'tbg':   '#ebdbb2',
        'lc':    '#3c3836',
        'lw':    1.2,
        'gc':    '#f2e8be',
        'color': 'light',
    },
    'gruvbox-dark': {
        'bg':    '#282828',
        'bg2':   '#3c3836',
        'fg':    '#ebdbb2',
        'fg2':   '#d5c4a1',
        'sbg':   '#504945',
        'sfg':   '#ebdbb2',
        'tbg':   '#3c3836',
        'lc':    '#ebdbb2',
        'lw':    1.2,
        'gc':    '#2e2e2e',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # Tokyo Night  —  enkia
    # -------------------------------------------------------------------------

    'tokyonight': {
        'bg':    '#1a1b26',
        'bg2':   '#16161e',
        'fg':    '#a9b1d6',
        'fg2':   '#7aa2f7',
        'sbg':   '#515c7e',
        'sfg':   '#a9b1d6',
        'tbg':   '#16161e',
        'lc':    '#a9b1d6',
        'lw':    1.2,
        'gc':    '#1e1f2b',
        'color': 'dark',
    },
    'tokyonight-storm': {
        'bg':    '#24283b',
        'bg2':   '#1f2335',
        'fg':    '#a9b1d6',
        'fg2':   '#7aa2f7',
        'sbg':   '#6f7bb6',
        'sfg':   '#c0caf5',
        'tbg':   '#1f2335',
        'lc':    '#a9b1d6',
        'lw':    1.2,
        'gc':    '#292e42',
        'color': 'dark',
    },
    'tokyonight-light': {
        'bg':    '#e6e7ed',
        'bg2':   '#d6d8df',
        'fg':    '#343b59',
        'fg2':   '#34548a',
        'sbg':   '#acb0bf',
        'sfg':   '#343b59',
        'tbg':   '#d6d8df',
        'lc':    '#343b59',
        'lw':    1.2,
        'gc':    '#dcdde3',
        'color': 'light',
    },

    # -------------------------------------------------------------------------
    # Catppuccin  —  catppuccin
    # -------------------------------------------------------------------------

    'catppuccin-mocha': {
        'bg':    '#1e1e2e',
        'bg2':   '#181825',
        'fg':    '#cdd6f4',
        'fg2':   '#b4befe',
        'sbg':   '#585b70',
        'sfg':   '#cdd6f4',
        'tbg':   '#11111b',
        'lc':    '#cdd6f4',
        'lw':    1.2,
        'gc':    '#232334',
        'color': 'dark',
    },
    'catppuccin-latte': {
        'bg':    '#eff1f5',
        'bg2':   '#e6e9ef',
        'fg':    '#4c4f69',
        'fg2':   '#7287fd',
        'sbg':   '#acb0be',
        'sfg':   '#4c4f69',
        'tbg':   '#dce0e8',
        'lc':    '#4c4f69',
        'lw':    1.2,
        'gc':    '#e4e6ec',
        'color': 'light',
    },

    # -------------------------------------------------------------------------
    # Dracula  —  dracula/dracula-theme
    # -------------------------------------------------------------------------

    'dracula': {
        'bg':    '#282a36',
        'bg2':   '#21222c',
        'fg':    '#f8f8f2',
        'fg2':   '#6272a4',
        'sbg':   '#44475a',
        'sfg':   '#f8f8f2',
        'tbg':   '#191a21',
        'lc':    '#f8f8f2',
        'lw':    1.2,
        'gc':    '#2d2f3b',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # Nord  —  nordtheme
    # -------------------------------------------------------------------------

    'nord': {
        'bg':    '#2e3440',
        'bg2':   '#3b4252',
        'fg':    '#d8dee9',
        'fg2':   '#81a1c1',
        'sbg':   '#434c5e',
        'sfg':   '#d8dee9',
        'tbg':   '#3b4252',
        'lc':    '#d8dee9',
        'lw':    1.2,
        'gc':    '#343a48',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # One Dark  —  Atom
    # -------------------------------------------------------------------------

    'one-dark': {
        'bg':    '#282c34',
        'bg2':   '#21252b',
        'fg':    '#abb2bf',
        'fg2':   '#61afef',
        'sbg':   '#3e4451',
        'sfg':   '#abb2bf',
        'tbg':   '#21252b',
        'lc':    '#abb2bf',
        'lw':    1.2,
        'gc':    '#2d3139',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # Monokai  —  Wimer Hazenberg (Sublime Text)
    # -------------------------------------------------------------------------

    'monokai': {
        'bg':    '#272822',
        'bg2':   '#1e1f1c',
        'fg':    '#f8f8f2',
        'fg2':   '#a6e22e',
        'sbg':   '#49483e',
        'sfg':   '#f8f8f2',
        'tbg':   '#414339',
        'lc':    '#f8f8f2',
        'lw':    1.2,
        'gc':    '#2d2e27',
        'color': 'dark',
    },

    # -------------------------------------------------------------------------
    # Tomorrow  —  Chris Kempson
    # -------------------------------------------------------------------------

    'tomorrow': {
        'bg':    '#ffffff',
        'bg2':   '#f2f2f2',
        'fg':    '#4d4d4d',
        'fg2':   '#4271ae',
        'sbg':   '#d6d6d6',
        'sfg':   '#4271ae',
        'tbg':   '#cccccc',
        'lc':    '#4d4d4d',
        'lw':    1.2,
        'gc':    '#e6e6e6',
        'color': 'light',
    },

    # -------------------------------------------------------------------------
    # n30x custom themes
    # -------------------------------------------------------------------------

    'n30x-dark': {
        'bg':    '#252525',
        'bg2':   '#2a2a2a',
        'fg':    '#00997a',
        'fg2':   '#b7855f',
        'sbg':   '#323232',
        'sfg':   '#9575cd',
        'tbg':   '#404040',
        'lc':    '#939393',
        'lw':    1.2,
        'gc':    '#323232',
        'color': 'dark',
    },
    'n30x-darkblue': {
        'bg':    '#28283e',
        'bg2':   '#26263e',
        'fg':    '#00997a',
        'fg2':   '#934806',
        'sbg':   '#22223e',
        'sfg':   '#c46008',
        'tbg':   '#20203a',
        'lc':    '#939393',
        'lw':    1.2,
        'gc':    '#32324e',
        'color': 'dark',
    },
}
