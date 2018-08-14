#!/bin/env bash
set -e
if [ ! ./gns3hack.sh ]; then
    echo "Failed to locate src dir."
    exit 1
fi
REPO_DIR=$(cd $(dirname $0) && 'pwd')
SRCDIR=./gns3-gui-2.1.9
USER=$(logname)
gns3_gui_conf=/home/$USER/.config/GNS3/gns3_gui.conf
[[ ! -f $gns3_gui_conf.bak ]] && cp $gns3_gui_conf ${gns3_gui_conf}.bak

_usage() {
    printf "%s\n" "Usage: $0 --scheme <scheme-name> [OPTIONS]"
    printf "%s\n" "       $0 [OPTION].. "
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
    printf "  %s\t\t%s\n" "-s, --scheme" "Change gns3 theme from predefined schemes"
    printf "  %s\t%s\n" "-l, --list-schemes" "List gns3 schemes"
    printf "\n"
    printf "%s\n" "Install theme from predefined schemes"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme gruvbox-light" 
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light" 
    printf "%s\n" "Use the scheme but with different selection color"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light --sbg ef5350"
    printf "%s\n" "Install custom scheme"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 .." 
    printf "  %s\t\t%s\n"  "./gns3theme.sh --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 -o 0.95 .." 
}
tmpdir=$(mktemp -d -t)
cp -af ${REPO_DIR}/* ${tmpdir}
cd $tmpdir
trap clean_up 0 1 2 15
clean_up() {
    rm -rf ${tmpdir}
    #echo "Finished cleaning."
}
if [ $# -lt 1 ]; then
    echo "$0: missing option"
    echo "Try '$0 --help' for more information."
    exit 1
fi
# Validate the color
_isvalidcolor () {
    if [[ ! "$1" =~ $re_hexcolor ]]; then
        echo "ERROR: Color must be in hex format or names e.g. "2d2d2d". "
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
# List pre-defined color schemes
_listschemes() {
    sed -n '/scheme-template/,$p' $SRCDIR/../schemes
}
_gns3scheme () {
    local scheme_name=${1}
    scheme=($(grep "^${scheme_name}:" $SRCDIR/../schemes | cut -d: -f2))
    if [ -z ${scheme} ]; then
        echo "ERROR: Unsupported scheme '$1'."
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
    if [ ${scheme[9]} == "light" ]; then
        _changevariable black "lc"
        _changevariable 230 "gc"
        sed -i "s/\(\"style\": \).[^,]*/\1\"Classic\"/g" ${gns3_gui_conf}
    else
        _changevariable gray "lc"
        [[ ${scheme_name} == "tomorrow-night" ]] && _changevariable 36 "gc" || _changevariable 45 "gc"
        sed -i "s/\(\"style\": \).[^,]*/\1\"Charcoal\"/g" ${gns3_gui_conf}
    fi
    _changevariable 1.2 "lw"
}
_changecolor() {
    local color=$1
    local type=$2
    iflag=true
    if [ $type == "bg" ]; then
        sed -i -e "/QWidget/{n;s/#[^;].*/"$color";/}" \
               -e "/QMenuBar::item/{n;s/#[^;].*/"$color";/}" \
               -e "/QTextEdit#uiConsole/{n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget,/{n;s/#[^;].*/"$color";/}" \
               -e "/QMenu\ /{n;s/#[^;].*/"$color";/}" \
               -e "/QScrollBar:vertical/{n;s/#[^;].*/"$color";/}" \
               -e "/QScrollBar:horizontal/{n;s/#[^;].*/"$color";/}" \
               -e "/QScrollBar::up/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QAbstractScrollArea/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui 
    elif [ $type == "bg2" ]; then
        sed -i -e "/QTextEdit, /{n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget#uiTree/{n;s/#[^;].*/"$color";/}" \
               -e "/QTabBar::tab\ /{n;s/#[^;].*/"$color";/}" \
               -e "/QScrollBar::handle/{n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget,\ /{n;n;n;s/#[^;].*/"$color";/}" \
               -e "/QLabel#uiTitleLabel/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "fg" ]; then
        sed -i -e "/QDockWidget, /{n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget,/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget#uiTree/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTabBar::tab\ /{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTextEdit#uiConsole/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTextEdit,\ /{n;n;s/#[^;].*/"$color";/}" \
               -e "/QLabel/{n;s/#[^;].*/"$color";/}" \
               -e "/QStatusBar/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QRadioButton/{n;s/#[^;].*/"$color";/}" \
               -e "/QMenu\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "fg2" ]; then
        sed -i -e "/QGroupBox\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "tbg" ]; then
        sed -i -e "/QDockWidget::title/{n;s/#[^;].*/"$color";/}" \
               -e "/QToolBar/{n;s/#[^;].*/"$color";/}" \
               -e "/QStatusBar/{n;s/#[^;].*/"$color";/}" \
               -e "/QMainWindow::separator/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "sbg" ]; then
        sed -i -e "/^QComboBox\ /{n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget::item:hover/{n;s/#[^;].*/"$color";/}" \
               -e "/QMenu::item:selected/{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "sfg" ]; then
        sed -i -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"$color";/}" \
               -e "/^QComboBox\ /{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTreeWidget::item:hover/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QMenu::item:selected/{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "bbg" ]; then
        sed -i -e "/QPushButton\ /{n;s/#[^;].*/"$color";/}" \
               -e "/QTabBar::tab:selected/{n;s/#[^;].*/"$color";/}" \
               -e "/QToolButton\ /{n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    elif [ $type == "bfg" ]; then
        sed -i -e "/^QPushButton/{n;n;s/#[^;].*/"$color";/}" \
               -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"$color";/}" \
               -e "/^QToolButton\ /{n;n;s/#[^;].*/"$color";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
}
_changevariable() {
    var=$1;
    type=$2;
    if [ $type == "lw" ]; then
        sed -i -e "s/\(self\._pen_width\ =\ \).*$/\1"$var"/" \
               -e "s/\(self._point_size\ =\ \).*$/\18/" "$SRCDIR"/gns3/items/link_item.py
    elif [ $type == "lc" ]; then
        #possiblecolors: black, blue, cyan, green, gray, red, yellow, magenta, white, darkBlack, darkBlue, ....)
        sed -i "s/\(self\.setPen.*Qt\.\).*\(,\ self\._pen_width,.*))\)/\1"$var"\2/" "$SRCDIR"/gns3/items/ethernet_link_item.py
    elif [ $type == "gc" ]; then
        sed -i "s/\(painter\.setPen(QtGui.QPen(QtGui.QColor(\).*[0-9]\+,.*[0-9]\+,.*[0-9]\+\(.[^)]*\)/\1$var, $var, $var\2/g" $SRCDIR/gns3/graphics_view.py
    fi
    # fix zoom-in zoom-out step values
    sed -i -e "s/\(factor_in = pow(2.0, \).[^///]*\(.[^)]*\)/\130 \2/g" \
           -e "s/\(factor_out = pow(2.0, \).[^///]*\(.[^)]*\)/\1-30 \2/g" $SRCDIR/gns3/main_window.py
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
    echo "gns3-gui Installation Finished ..."
    echo "Restart gns3 to apply changes ..."
}
re_digit='^[0-9]{,2}\.[0-9]$'
re_hexcolor='^#[0-9a-fA-F]{6}$'
re_opacity='^0\.[0-9]{,2}$'

flags=(false false false false false false false false false false false false false false)
OPTS="$(getopt -o o:,s:,ihl --long bg:,bg2:,fg:,fg2:,tbg:,opacity:,sbg:,sfg:,bbg:,bfg:,lw:,lc:,scheme:,help,install -n $0 -- "$@")"
if [ $? -ne 0 ]; then
    echo "Failed parsing options, see '$0 --help' for more info."
    exit 1
fi
while [ $# -gt 0 ] && [ "$1" != "--" ]; do 
    case "$1" in
        --bg)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "bg"
            shift 2
            ;;
        --bg2)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "bg2"
            shift 2
            ;;
        --fg)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "fg"
            shift 2
            ;;
        --fg2)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "fg2"
            flags[3]=true
            shift 2
            ;;
        --tbg)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "tbg"
            shift 2
            ;;
        --sbg)
            _isvalidcolor "#${2}"
            _changecolor "#${2}" "sbg"
            shift 2
            ;;
        --sfg)
            _isvalidcolor #${2}
            _changecolor "#${2}" "sfg"
            flags[6]=true
            shift 2
            ;;
        --bbg)
            _isvalidcolor #${2}
            _changecolor "#${2}" "bbg"
            shift 2
            ;;
        --bfg)
            _isvalidcolor #${2}
            _changecolor "#${2}" "bfg"
            shift 2
            ;;
        --lw)
			_changevariable ${2} "lw"
            shift 2
            ;;
        --lc)
            _changecolor "#${2}" "lc"
            shift 2
            ;;
        -o|--opacity)
            _isvalidopacity "${2}"
            _uitransparent "${2}"
            shift 2
            ;;
        -s|--scheme)
            _gns3scheme "${2}" 
            shift 2
            ;;
        -l|--list-schemes)
            _listschemes
            exit 0
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
if [ $iflag == true ]; then
    _isroot
    _gns3install
fi
exit 0
