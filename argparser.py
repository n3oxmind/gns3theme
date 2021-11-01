import argparse
import shutil


class CustomFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        # determine the required width and the entry label
        term_size = shutil.get_terminal_size(fallback=(80, 24))
        self._width = term_size.columns - 11 if term_size.columns < 140 else 129
        help_position = min(self._action_max_length + 2,
                            self._max_help_position)
        help_width = max(self._width - help_position, 11)
        action_header = self._format_action_invocation(action)

        header_indent = 2 * ' '
        max_action_header_width = 30
        custom_action_header = [i.strip(',') for i in action_header.split()]

        if not action.help:
            tup = self._current_indent, '', action_header
            action_header = '%*s%s\n' % tup

        elif custom_action_header[0][:2] == '--' and len(custom_action_header) > 1:
            custom_header_format = f"{custom_action_header[0]} {custom_action_header[1]}"
            action_header = f"{header_indent}{custom_header_format:<{max_action_header_width}}"

        elif len(custom_action_header) > 4:
            custom_header_format = f"{custom_action_header[0]}, {custom_action_header[4]} {custom_action_header[1]}"
            action_header = f"{header_indent}{custom_header_format:<{max_action_header_width}}"

        elif len(custom_action_header) == 4:
            custom_header_format = f"{custom_action_header[0]}, {custom_action_header[2]} {custom_action_header[1]}"
            action_header = f"{header_indent}{custom_header_format:<{max_action_header_width}}"
        else:
            action_header = f"{header_indent}{action_header:<{max_action_header_width}}"

        parts = [action_header]

        if action.help:
            help_text = self._expand_help(action)
            help_lines = self._split_lines(help_text, help_width)
            parts.append(f"{help_lines[0]}\n")
            for line in help_lines[1:]:
                parts.append(f"{header_indent}{' ':<{max_action_header_width}}{line}\n")

        elif not action_header.endswith('\n'):
            parts.append('\n')

        for subaction in self._iter_indented_subactions(action):
            parts.append(self._format_action(subaction))
        return self._join_parts(parts)


def usage():
    """usage header"""
    usage = """%(prog)s --install <path/to/gns3_gui_dir> --scheme <colorscheme>
       %(prog)s --scheme <colorscheme> [options]\n"""
    return usage


def description():
    description_format = "gns3theme is a script that will add a custom style for gns3-gui."
    return description_format


parser = argparse.ArgumentParser(prog='gns3theme', usage=usage(), formatter_class=CustomFormatter, add_help=False)

parser_group_manditory = parser.add_argument_group(title='manditory arguments')
parser_group_options = parser.add_argument_group(title='optional arguments')
parser_group_flags = parser.add_argument_group(title='optional flags')

parser_group_options.add_argument('--bg', dest='bg', metavar='COLOR',
                                  help='change primary background color')
parser_group_options.add_argument('--bg2', dest='bg2', metavar='COLOR',
                                  help='change secondary background color')
parser_group_options.add_argument('--fg', dest='fg', metavar='COLOR',
                                  help='change primary foreground color')
parser_group_options.add_argument('--fg2', dest='fg2', metavar='COLOR',
                                  help='change secondary foreground color')
parser_group_options.add_argument('--tbg', dest='tbg', metavar='COLOR',
                                  help='change toolbar background color')
parser_group_options.add_argument('--sbg', dest='sbg', metavar='COLOR',
                                  help='change selection background color')
parser_group_options.add_argument('--sfg', dest='sfg', metavar='COLOR',
                                  help='change selection foreground color')
parser_group_options.add_argument('--bbg', dest='bbg', metavar='COLOR',
                                  help='change button background color')
parser_group_options.add_argument('--lc', dest='lc', metavar='COLOR',
                                  help='change ethernet link color. Reinstall gns3-gui as root is required')
parser_group_options.add_argument('--lw', dest='lw', metavar='NUM',
                                  help='change ethernet and serial links width. Reinstall gns3-gui as root is required')
parser_group_options.add_argument('--gc', dest='gc', metavar='COLOR',
                                  help='change grid color. Reinstall gns3-gui as root is required')

parser_group_manditory.add_argument('-i', '--install', dest='install_scheme', metavar='PATH',
                                    help='path to gns3-gui source directory ')

parser_group_manditory.add_argument('-s', '--scheme', dest='color_scheme', metavar='NAME',
                                    help='choose color scheme to apply for gns3-gui')
parser_group_manditory.add_argument('-u', '--user', dest='username', metavar='USER',
                                    help='Specify username for installation. only used with --install option')

parser_group_flags.add_argument("--help", action='help', help='show this help')
parser_group_flags.add_argument('--ls', dest='list_schemes', action='store_true',
                                help='list predefined color schemes')

parser_group_manditory = parser.add_argument_group(title='manditory arguments')

#args = parser.parse_args()
#parser.print_help()
