"""
File contains a list of predefined color schemes. Here where you can add/change gns3 color schemes
where
   fg:  	forground color(text)
   fg2:  	secondary forground color(header text)
   bg:  	background color of main window
   bg2: 	secondary background color of sidebars, menus, fields, ...,etc
   sbg: 	selection background color
   sfg: 	selection forground color
   tbg: 	toolbar background color
   bbg:     button background color
   bfg:     button forground color
   lc:      link color
   lw:      link width
   gc:      grid color
   color:   theme color [light,dark]
"""

schemes = {
    'solarized-light': {
        'bg': '#fdf6e3',
        'bg2': '#eee8d5',
        'fg': '#657b83',
        'fg2': '#0087ff',
        'sbg': '#0087ff',
        'sfg': '#e4e4e4',
        'tbg': '#3338d5',
        'bbg': '#d70000',
        'bfg': '#1d2021',
        'lc': '#657b83',
        'lw': 1.2,
        'gc': '#e6e6e6',
        'color': 'light',
    },
    'solarized-dark': {
        'bg': '#002b36',
        'bg2': '#073642',
        'fg': '#839496',
        'fg2': '#0087ff',
        'tbg': '#073642',
        'sbg': '#d75f00',
        'sfg': '#1c1c1c',
        'bbg': '#8a8a8a',
        'bfg': '#1d2021',
        'lc': '#839496',
        'lw': 1.2,
        'gc': '#003d4d',
        'color': 'dark',
    },
    'n30x-dark': {
        'bg': '#252525',
        'bg2': '#2a2a2a',
        'fg': '#00997a',
        'fg2': '#b7855f',
        'tbg': '#404040',
        'sbg': '#323232',
        'sfg': '#9575cd',
        'bbg': '#c2185b',
        'bfg': '#1a1a1a',
        'lc': '#939393',
        'lw': 1.2,
        'gc': '#323232',
        'color': 'dark',
    },
    'n30x-darker': {
        'bg': '#0d0d0d',
        'bg2': '#141414',
        'fg': '#008066',
        'fg2': '#2979ff',
        'tbg': '#181818',
        'sbg': '#000000',
        'sfg': '#ba4551',
        'bbg': '#161616',
        'bfg': '#b3b3b3',
        'lc': '#008066',
        'lw': 1.2,
        'gc': '#181818',
        'color': 'dark',
    },
    'n30x-darkblue': {
        'bg': '#28283e',
        'bg2': '#26263e',
        'fg': '#00997a',
        'fg2': '#934806',
        'tbg': '#20203a',
        'sbg': '#22223e',
        'sfg': '#c46008',
        'bbg': '#24243e',
        'bfg': '#00997a',
        'lc': '#939393',
        'lw': 1.2,
        'gc': '#32324e',
        'color': 'dark',
    },
    'n30x-light': {
        'bg': '#fafafa',
        'bg2': '#eeeeee',
        'fg': '#424242',
        'fg2': '#03a9f4',
        'tbg': '#eeeeee',
        'sbg': '#03a9f4',
        'sfg': '#ffffff',
        'bbg': '#e91e63',
        'bfg': '#1a1a1a',
        'lc': '#424242',
        'lw': 1.2,
        'gc': '#e6e6e6',
        'color': 'light',
    },
    'tomorrow': {
        'bg': '#ffffff',
        'bg2': '#f2f2f2',
        'fg': '#4d4d4d',
        'fg2': '#0087ff',
        'tbg': '#cccccc',
        'sbg': '#d6d6d6',
        'sfg': '#4271ae',
        'bbg': '#3e999f',
        'bfg': '#ffffff',
        'lc': '#4d4d4d',
        'lw': 1.2,
        'gc': '#e6e6e6',
        'color': 'light',
    },
    'dwm-dark': {
        'bg': '#0d0d0d',
        'bg2': '#141414',
        'fg': '#ffffff',
        'fg2': '#00b6ff',
        'tbg': '#181818',
        'sbg': '#000000',
        'sfg': '#BA4551',
        'bbg': '#161616',
        'bfg': '#b3b3b3',
        'lc': '#0a7aca',
        'lw': 2,
        'gc': '#303030',
        'color': 'dark',
    }
}
