# gns3theme

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Sponsor](https://img.shields.io/badge/support_this_project-pink?logo=github-sponsors)](https://github.com/sponsors/n3oxmind)

A Python tool that adds custom color themes to the GNS3 GUI. Works on **Linux** and **macOS**.

- 17 built-in color schemes (dark and light variants)
- Custom user schemes via JSON files
- Canvas link color, grid color, label color, and console text color
- Optional device symbol pack
- Auto-detects GNS3 installation (GNS3.app, pip, brew, source)
- Safe patching with automatic backups

## Quick start

```sh
git clone https://github.com/n3oxmind/gns3theme.git
cd gns3theme

# Apply a theme (auto-detects GNS3 location)
sudo ./gns3theme.py -s nord

# Restart GNS3 and select:
#   Edit -> Preferences -> General -> Interface Style -> Custom
```

> **Note**: `sudo` is required when GNS3 is installed system-wide or as a macOS `.app` bundle.
> If GNS3 is installed in your home directory (`~/.local/`), sudo is not needed.

## Usage

```
gns3theme -s <scheme>                     # apply theme (auto-detect GNS3)
gns3theme -s <scheme> --gns3-dir PATH     # apply theme to specific path
gns3theme --restore                       # restore original GNS3 files
gns3theme --ls                            # list available color schemes
gns3theme --symbols                       # install bundled device symbols
gns3theme -s <scheme> --symbols           # apply theme and install symbols
```

### Full options

```
main arguments:
  -s, --scheme NAME  color scheme to apply and install
  --gns3-dir PATH    GNS3 site-packages path (auto-detected if omitted)

color overrides:
  --bg COLOR         primary background color
  --bg2 COLOR        secondary background color
  --fg COLOR         primary foreground color
  --fg2 COLOR        secondary foreground color
  --tbg COLOR        toolbar background color
  --sbg COLOR        selection background color
  --sfg COLOR        selection foreground color
  --lc COLOR         link color on canvas
  --gc COLOR         grid color
  --lbl COLOR        device label text color

flags:
  --help             show this help
  --ls               list available color schemes
  --symbols          install bundled device symbols to ~/GNS3/symbols/
  --restore [PATH]   restore original GNS3 files from backups
```

## Color schemes

### Dark

| Scheme | Source |
|--------|--------|
| `nord` | [nordtheme](https://www.nordtheme.com/) |
| `dracula` | [dracula](https://draculatheme.com/) |
| `tokyonight` | [enkia](https://github.com/enkia/tokyo-night-vscode-theme) |
| `tokyonight-storm` | [enkia](https://github.com/enkia/tokyo-night-vscode-theme) |
| `catppuccin-mocha` | [catppuccin](https://github.com/catppuccin/catppuccin) |
| `one-dark` | [Atom](https://github.com/atom/one-dark-ui) |
| `monokai` | Wimer Hazenberg |
| `gruvbox-dark` | [morhetz](https://github.com/morhetz/gruvbox) |
| `solarized-dark` | [Ethan Schoonover](https://ethanschoonover.com/solarized/) |
| `n30x-dark` | n30x |
| `n30x-darkblue` | n30x |

### Light

| Scheme | Source |
|--------|--------|
| `tokyonight-light` | [enkia](https://github.com/enkia/tokyo-night-vscode-theme) |
| `catppuccin-latte` | [catppuccin](https://github.com/catppuccin/catppuccin) |
| `gruvbox-light` | [morhetz](https://github.com/morhetz/gruvbox) |
| `solarized-light` | [Ethan Schoonover](https://ethanschoonover.com/solarized/) |
| `tomorrow` | [Chris Kempson](https://github.com/chriskempson/tomorrow-theme) |

## Custom schemes

Create a JSON file in `~/.config/gns3theme/schemes/`:

```json
{
  "bg":    "#1e1e2e",
  "bg2":   "#181825",
  "fg":    "#cdd6f4",
  "fg2":   "#b4befe",
  "sbg":   "#585b70",
  "sfg":   "#cdd6f4",
  "tbg":   "#11111b",
  "lc":    "#cdd6f4",
  "gc":    "#232334",
  "color": "dark"
}
```

Save it as `~/.config/gns3theme/schemes/mytheme.json`, then use it with `-s mytheme`.

### Required keys

| Key | Description |
|-----|-------------|
| `bg` | Primary background |
| `bg2` | Secondary background (sidebars, inputs) |
| `fg` | Primary foreground / text |
| `fg2` | Accent color (section headers) |
| `sbg` | Selection background |
| `sfg` | Selection foreground |
| `tbg` | Toolbar background |
| `color` | `"dark"` or `"light"` |

### Optional keys

| Key | Description |
|-----|-------------|
| `lc` | Link color on canvas (defaults to `fg`) |
| `gc` | Grid color |
| `lbl` | Device label text color (defaults to `fg`) |
| `lw` | Link width (float, e.g. `1.2`) |

## Overriding individual colors

You can override any color on top of a base scheme:

```sh
# Use nord but with a custom selection background
./gns3theme.py -s nord --sbg 5e81ac

# Use dracula but change the link color
./gns3theme.py -s dracula --lc ff79c6
```

## Device symbols

gns3theme includes 16 SVG device symbols (routers, switches, firewalls, servers, PCs, clouds).

```sh
./gns3theme.py --symbols
```

Symbols are installed to `~/GNS3/symbols/` and appear in the GNS3 symbol selection dialog. You can combine `--symbols` with a scheme:

```sh
./gns3theme.py -s nord --symbols
```

## How it works

gns3theme patches the GNS3 GUI to add a **Custom** interface style option:

1. **CSS stylesheet** is generated from the color scheme and saved to `~/.config/gns3theme/custom_style.css`
2. **Runtime config** (grid color, link color, label color, console color) is saved to `~/.config/gns3theme/config.json`
3. **GNS3 source files** are patched to:
   - Add "Custom" to the interface style list
   - Load the CSS and config when "Custom" is selected
   - Apply theme colors to canvas links and console text

### Backups

Original files are always backed up to `~/.config/gns3theme/backups/` before patching. On macOS, the original `GNS3.app` is preserved as `/Applications/GNS3.app.bak`. Backups are never deleted.

### Restore

```sh
# Restore original files (auto-detect)
sudo ./gns3theme.py --restore

# Restore with explicit path
sudo ./gns3theme.py --restore /path/to/site-packages
```

## Supported installations

| Platform | Install method | Detection |
|----------|---------------|-----------|
| macOS | GNS3.app (DMG) | `/Applications/GNS3.app` |
| macOS | pip / brew | `python3 -c "import gns3"` or scans site-packages |
| Linux | pip | `~/.local/lib/pythonX.Y/site-packages` |
| Linux | system package | `/usr/lib/pythonX.Y/site-packages` |
| Linux | pipx / virtualenv | Scans common venv paths |

If auto-detection fails, specify the path manually with `--gns3-dir`.

## Requirements

- Python 3.8+
- GNS3 GUI installed

No additional Python dependencies are required.

## License

MIT
