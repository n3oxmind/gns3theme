import argparse
import shutil


class CustomFormatter(argparse.RawDescriptionHelpFormatter):
    """Formatter that shows short+long flags on one line with aligned help text."""

    def __init__(self, prog, **kwargs):
        term_cols = shutil.get_terminal_size(fallback=(80, 24)).columns
        width = min(term_cols, 100)
        super().__init__(prog, width=width, max_help_position=34, **kwargs)

    def _format_action_invocation(self, action):
        if not action.option_strings:
            return super()._format_action_invocation(action)

        opts = list(action.option_strings)
        if action.nargs != 0 and action.metavar:
            # e.g. "-i, --install PATH"
            long = [o for o in opts if o.startswith('--')]
            short = [o for o in opts if not o.startswith('--')]
            if short and long:
                return f"{short[0]}, {long[0]} {action.metavar}"
            elif long:
                return f"{long[0]} {action.metavar}"
            else:
                return f"{short[0]} {action.metavar}"
        else:
            return ', '.join(opts)


USAGE = """%(prog)s --scheme <colorscheme> [options]
       %(prog)s --restore [PATH]\n"""

DESCRIPTION = "gns3theme adds custom themes to GNS3 GUI. Supports Linux and macOS."

parser = argparse.ArgumentParser(
    prog='gns3theme',
    usage=USAGE,
    description=DESCRIPTION,
    formatter_class=CustomFormatter,
    add_help=False,
)

group_main = parser.add_argument_group(title='main arguments')
group_options = parser.add_argument_group(title='optional arguments')
group_flags = parser.add_argument_group(title='flags')

group_main.add_argument('-s', '--scheme', dest='color_scheme', metavar='NAME',
                        help='color scheme to apply and install')
group_main.add_argument('--gns3-dir', dest='gns3_dir', metavar='PATH',
                        help='GNS3 site-packages path (auto-detected if omitted)')

group_options.add_argument('--bg', dest='bg', metavar='COLOR',
                           help='primary background color')
group_options.add_argument('--bg2', dest='bg2', metavar='COLOR',
                           help='secondary background color')
group_options.add_argument('--fg', dest='fg', metavar='COLOR',
                           help='primary foreground color')
group_options.add_argument('--fg2', dest='fg2', metavar='COLOR',
                           help='secondary foreground color')
group_options.add_argument('--tbg', dest='tbg', metavar='COLOR',
                           help='toolbar background color')
group_options.add_argument('--sbg', dest='sbg', metavar='COLOR',
                           help='selection background color')
group_options.add_argument('--sfg', dest='sfg', metavar='COLOR',
                           help='selection foreground color')
group_options.add_argument('--lc', dest='lc', metavar='COLOR',
                           help='link color on canvas')
group_options.add_argument('--lw', dest='lw', metavar='NUM',
                           help='link width')
group_options.add_argument('--gc', dest='gc', metavar='COLOR',
                           help='grid color')
group_options.add_argument('--lbl', dest='lbl', metavar='COLOR',
                           help='device label text color')

group_flags.add_argument('--help', action='help', help='show this help')
group_flags.add_argument('--ls', dest='list_schemes', action='store_true',
                         help='list available color schemes')
group_flags.add_argument('--symbols', dest='install_symbols', action='store_true',
                         help='install bundled device symbols to ~/GNS3/symbols/')
group_flags.add_argument('--restore', dest='restore', metavar='PATH',
                         nargs='?', const='auto',
                         help='restore original GNS3 files from backups')
