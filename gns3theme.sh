#!/bin/env bash
set -e
_usage() {
    printf "%s\n" "Usage: gns3hack gns3-gui_dir [OPTION]... <value>"
    printf "%s\n" "       gns3hack gns3-project_dir [OPTION] <value>"
    printf "%s\n" "OPTIONS:"
    printf "  %s\t\t\t%s\n" "--bg"  "Change primary background color"
    printf "  %s\t\t\t%s\n" "--bg2" "Change secondary background color"
    printf "  %s\t\t\t%s\n" "--fg"  "Change primary foreground color"
    printf "  %s\t\t\t%s\n" "--fg2" "Change secondary foreground color"
    printf "  %s\t\t\t%s\n" "--tbg"   "Change toolbar background color"
    printf "  %s\t\t\t%s\n" "--sbg" "Change selection background color"
    printf "  %s\t\t\t%s\n" "--sfg" "Change selelction foreground color"
    printf "  %s\t\t\t%s\n" "--btn" "Change button background color"
    printf "  %s\t\t\t%s\n" "--lc" "Change ethernet link color"
    printf "  %s\t\t\t%s\n" "--lw" "Change ethernet and serial links width"
    printf "  %s\t\t%s\n" "-o, --opacity" "Apply transparency to gns3 gui"
    printf "  %s\t\t%s\n" "--theme" "Change gns3 theme from predefined themes"
    printf "\t\t\t%s\n" "supported themes: gruvbox-{light,dark}, solarized-{light,dark}"
    printf "  %s\t\t%s\n" "--install" "Install gns3-gui"
    printf "\n"
    printf "%s\n" "Examples:"
    printf "%s\n" "Install predefined theme"
    printf "  %s\t\t%s\n"  "cd ~/Download/gns3-gui-1.2.4" 
    printf "  %s\t\t%s\n"  "./gns3hack.sh --theme gruvbox-light" 
    printf "  %s\t\t%s\n"  "./gns3hack.sh --theme solarized-light" 
    printf "%s\n" "Install custom theme"
    printf "  %s\t\t%s\n"  "cd ~/Download/gns3-gui-1.2.4" 
    printf "  %s\t\t%s\n"  "./gns3hack.sh --bg \"#282828\" --bg2 \"#323232\" --fg \"#FFFFFF\" --tbg \"#303030\"" 
    printf "  %s\t\t%s\n"  "./gns3hack.sh --bg \"#282828\" --bg2 \"#323232\" --fg \"#FFFFFF\" --tbg \"#303030\" -o 0.95" 
}
if [ $# -lt 1 ]; then
    echo "$0: missing option"
    echo "Try '$0 --help' for more information."
    exit 1
fi
# Validate the color
_isvalidcolor () {
    if [[ ! "$1" =~ $re_hexcolor ]]; then
        echo "ERROR: Color must be in hex format or names e.g. "#ffffff". "
        exit 1
    fi
}
# Validate the opacity
_isvalidopacity () {
    if [[ ! "$1" =~ $re_opacity ]] && [ "$1" != "1.0" ] ; then
        echo "ERROR: Window opacity must be between 0.0 and 1.0"
        exit 1
    fi
}
# Check if the script running as root
_isroot () {
    if [ "$(whoami)" != "root" ]; then
        echo "Please, run as root"
        exit 1
    fi
}
_isdigit () {
    if [[ ! $1 =~ $re_digit ]];then
        echo "ERROR: Font-size must be in this format dd.d(12.5)"
        exit 1
    fi
}
_gns3themes () {
    # Array format named=('bg' 'bg2' 'fg' 'fg2' 'tbg' 'sbg' 'sfg' 'bbg' 'bfg' lc' afont-type' 'style')
    theme_name=$1
    if [ "$theme_name" == "gruvbox-light" ]; then
        scheme=('#fbf1c7' '#ebdbb2' '#282828' '#458588' '#d5c4a1' '#076678' '#f9f5d7' '#cc241d' '#3c3836' 'black')
    elif [ "$theme_name" == "gruvbox-dark" ]; then
        scheme=('#282828' '#3c3836' '#ebdbb2' '#fe8019' '#504945' '#fb4934' '#32302f' '#458588' '#1d2021' 'gray')
    elif [ "$theme_name" == "solarized-light" ]; then
        scheme=('#fdf6e3' '#eee8d5' '#657b83' '#808080' '#eee8d5' '#0087ff' '#e4e4e4' '#d70000' '#1d2021' 'black')
    elif [ "$theme_name" == "solarized-dark" ]; then
        scheme=('#002b36' '#073642' '#839496' '#808080' '#073642' '#d75f00' '#1c1c1c' '#8a8a8a' '#1d2021' 'gray')
    else
        echo "ERROR: Unsupported theme, Try '$0 --help' for more information."
        exit 1
    fi
    _changecolor ${scheme[0]} "bg" 
    _changecolor ${scheme[1]} "bg2" 
    _changecolor ${scheme[2]} "fg" 
    _changecolor ${scheme[3]} "fg2" 
    _changecolor ${scheme[4]} "tbg" 
    _changecolor ${scheme[5]} "sbg" 
    _changecolor ${scheme[6]} "sfg" 
    _changecolor ${scheme[7]} "bbg" 
    _changecolor ${scheme[8]} "bfg" 
    _changecolor ${scheme[9]} "lc" 
}
_changecolor() {
    local color=$1
    local type=$2
    if [ $type == "bg" ]; then
        sed -i -e "/QWidget/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMenuBar::item/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTextEdit#uiConsole/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget,/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMenu\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QScrollBar:vertical/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QScrollBar:horizontal/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QScrollBar::up/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QAbstractScrollArea/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui 
    elif [ $type == "bg2" ]; then
        sed -i -e "/QTextEdit, /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget#uiTree/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTabBar::tab\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QScrollBar::handle/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget,\ /{n;n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QLabel#uiTitleLabel/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "fg" ]; then
        sed -i -e "/QDockWidget, /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget,/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget#uiTree/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTabBar::tab\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTextEdit#uiConsole/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTextEdit,\ /{n;n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QLabel/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QStatusBar/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QRadioButton/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMenu\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "fg2" ]; then
        sed -i -e "/QGroupBox\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "tbg" ]; then
        sed -i -e "/QDockWidget::title/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QToolBar/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QStatusBar/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMainWindow::separator/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "sbg" ]; then
        sed -i -e "/^QComboBox\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget::item:hover/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMenu::item:selected/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "sfg" ]; then
        sed -i -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/^QComboBox\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTreeWidget::item:hover/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QMenu::item:selected/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "bbg" ]; then
        sed -i -e "/QPushButton\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTabBar::tab:selected/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QToolButton\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "bfg" ]; then
        sed -i -e "/^QPushButton/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui \
               -e "/^QToolButton\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "lc" ]; then
        sed -i "s/\(self\.setPen.*Qt\.\).*\(,\ self\._pen_width,.*))\)/\1"$color"\2/" "$SRCDIR"/gns3/items/ethernet_link_item.py
    fi
}
ui_files=(main.py 
        main_window.py
        graphics_view.py
        modules/docker/pages/docker_vm_preferences_page.py
        modules/dynamips/pages/ios_router_preferences_page.py
        modules/iou/pages/iou_device_preferences_page.py
        modules/qemu/pages/qemu_vm_preferences_page.py
        modules/virtualbox/pages/virtualbox_vm_preferences_page.py
        modules/vmware/pages/vmware_vm_preferences_page.py
        modules/vpcs/pages/vpcs_node_preferences_page.py
        modules/builtin/pages/cloud_preferences_page.py
        modules/builtin/pages/ethernet_switch_preferences_page.py
        modules/builtin/pages/ethernet_hub_preferences_page.py
        )
_uitransparent() {
    local opacity=$1
    for uifile in "${ui_files[@]}"; do
        sed -i '/.*\.setWindowOpacity.*/d' "$SRCDIR"/gns3/$uifile
        sed -i "s/\(^\ *\)\(.*\)\(\.show()$\)/\1\2.setWindowOpacity\($opacity\)\n\1\2\3/g" $SRCDIR/gns3/$uifile 
    done 
}
# Install gns3-gui
_gns3install () {
    # perform Cleanup
    find /usr/lib \( -name "gns3" -o -name "gns3_gui-*.egg" -o -name "gns3_gui-*.egg-info" \) -type d -prune -exec rm -rf "{}" \+
    find /usr/local/lib \( -name "gns3" -o -name "gns3_gui-*.egg" -o -name "gns3_gui-*.egg-info" \) -type d -prune -exec rm -rf "{}" \+
    # apply changes and install 
    cd $SRCDIR
    scripts/build_pyqt.py
    python3 setup.py install
    echo 
    echo "gns3-gui successfully changed ..."
    echo "gns3-gui Installation Finished ..."
    echo "Restart gns3 to apply changes ..."
}
re_digit='^[0-9]{,2}\.[0-9]$'
re_hexcolor='^#[0-9a-fA-F]{6}$'
re_opacity='^0\.[0-9]{,2}$'

SRCDIR=$(cd $(dirname $0) && cd gns3-gui-2.1.4 && 'pwd')
flags=(false false false false false false false false false false false false false false)
OPTS="$(getopt -o o:,t:,i,h --long bg:,bg2:,fg:,fg2:,tbg:,opacity:,sbg:,sfg:,bbg:,bfg:,lw:,lc:,theme:,help,install -n $0 -- "$@")"
if [ $? -ne 0 ]; then
    echo "Failed parsing options, see '$0 --help' for more info."
    exit 1
fi
while [ $# -gt 0 ] && [ "$1" != "--" ]; do 
    case "$1" in
        --bg)
            _isvalidcolor "$2"
            _changecolor "$2" "bg"
            flags[0]=true
            shift 2
            ;;
        --bg2)
            _isvalidcolor "$2"
            _changecolor "$2" "bg2"
            flags[1]=true
            shift 2
            ;;
        --fg)
            _isvalidcolor "$2"
            _changecolor "$2" "fg"
            flags[2]=true
            shift 2
            ;;
        --fg2)
            _isvalidcolor "$2"
            _changecolor "$2" "fg2"
            flags[3]=true
            shift 2
            ;;
        --tbg)
            _isvalidcolor "$2"
            _changecolor "$2" "tbg"
            flags[4]=true
            shift 2
            ;;
        --sbg)
            _isvalidcolor "$2"
            _changecolor "$2" "sbg"
            flags[5]=true
            shift 2
            ;;
        --sfg)
            _isvalidcolor $2
            _changecolor "$2" "sfg"
            flags[6]=true
            shift 2
            ;;
        --bbg)
            _isvalidcolor $2
            _changecolor "$2" "bbg"
            flags[7]=true
            shift 2
            ;;
        --bfg)
            _isvalidcolor $2
            _changecolor "$2" "bfg"
            flags[8]=true
            shift 2
            ;;
        --lw)
            sed -i -e "s/\(self\._pen_width\ =\ \).*$/\1"$2"/" "$SRCDIR"/gns3/items/link_item.py \
                -e "s/\(self._point_size\ =\ \).*$/\18/" "$SRCDIR"/gns3/items/link_item.py
            flags[9]=true
            shift 2
            ;;
        --lc)
            _changecolor "$2" "lc"
            flags[10]=true
            shift 2
            ;;
        -o|--opacity)
            _isvalidopacity "$2"
            _uitransparent "$2"
            flags[11]=true
            shift 2
            ;;
        -t|--theme)
            if [ $# -gt 2 ]; then
                echo "Too many arguments, '--theme' takes only 1 argument."
                echo "Try '$0 --help' for more information."
                exit 1
            fi
            _gns3themes $2
            flags[12]=true
            shift 2
            ;;
        -h|--help)
            _usage
            exit 0
            ;;
        *) 
            echo "Unrecognized argument: "$1""
            exit 1
            ;;
    esac
done
for flag in "${flags[@]}"; do
    if [ $flag == true ]; then
        _isroot
        _gns3install
        break
    fi
done
