#!/bin/env bash
set -eo errexit
if [ ! ./gns3hack.sh ]; then
    echo "Failed to locate src dir."
    exit 1
fi
REPO_DIR=$(cd $(dirname $0) && 'pwd')
SRCDIR=./gns3-gui-2.2.3
USER=$(logname)
gns3_gui_conf=/home/$USER/.config/GNS3/2.2/gns3_gui.conf
gns3_gui_conf_bak=/home/$USER/.config/GNS3/2.2/gns3_gui.conf.bak
gns3_projects_dir=/home/$USER/GNS3/projects
colorscheme=( "default" "default" "default" "default" "default" \
              "default" "default" "default" "default" "default" \
              "default" "default" "default" )  
_usage() {
    printf "%s\n" "Usage: $0 --scheme <scheme-name> [OPTIONS]"
    printf "%s\n" "   or: $0 --scheme <scheme-name> [OPTIONS] --pretty <scheme-name>"
    printf "%s\n" "   or: $0 --scheme <scheme-name> [OPTIONS] --pretty <scheme-name> --opacity <num>"
    printf "%s\n" "   or: $0 [OPTION].. "
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
    printf "  %s\t\t\t%s\n" "--gc" "Change grid color"
    printf "  %s\t\t\t%s\n" "--lw" "Change ethernet and serial links width"
    printf "  %s\t\t%s\n" "-p, --pretty" "Change project(s) fonts from a predefined colorscheme and symbols if exist"
    printf "  %s\t\t%s\n" "-o, --opacity" "Apply transparency to gns3 gui"
    printf "  %s\t\t%s\n" "-s, --scheme" "Change gns3 theme from predefined schemes"
    printf "  %s\t%s\n" "-l, --list-schemes" "List gns3 schemes"
    printf "  %s\t%s\n" "-r, --restore-config" "Restore Nagios config files"
    printf "\n"
    printf "%s\n" "Install theme from predefined schemes"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme gruvbox-light" 
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light" 
    printf "%s\n" "Use the scheme but with different selection color"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light --sbg ef5350"
    printf "%s\n" "Install custom scheme"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 .." 
    printf "  %s\t\t%s\n"  "./gns3theme.sh --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 -o 0.95 .." 
    printf "%s\n" "Restore Nagios Config Files"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --restore-config" 
    printf "%s\n" "Restore gns3-gui"
    printf "  %s\t\t%s\n"  "pip3 install gns3-gui=2.2.3"
}
tmpdir=$(mktemp -d -t)
cp -af ${REPO_DIR}/* ${tmpdir}
cd $tmpdir
trap clean_up 0 1 2 15
clean_up() {
    rm -rf ${tmpdir}
    #echo "Finished cleaning."
}
_backup() {
    if [ "${1}" == "gns3_gui_conf" ]; then
        [[ ! -f ${gns3_gui_conf}.bak ]] && cp -a ${gns3_gui_conf} ${gns3_gui_conf}.bak || true
    elif [ "${1}" == "gns3_project_files" ]; then
        find $gns3_projects_dir -type f -name '*.gns3' -exec \
            $SHELL -c '[[ ! -f "{}".bak ]] && cp -a "{}" "{}".bak' \;
    fi
}

_restore_config() {
    if [ "${1}" == "gns3_gui_conf_bak" ]; then
        if [ -f ${gns3_gui_conf_bak} ]; then
            cp -af ${gns3_gui_conf_bak} ${gns3_gui_conf}
        else
            echo "No backup exist"
            exit 1
        fi
    fi
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
    sed -n '/scheme-template/,$p' $SRCDIR/../colorschemes
}
_isvalidscheme() {
    colorscheme=($(grep "^${1}:" $SRCDIR/../colorschemes | cut -d: -f2))
    if [ -z ${colorscheme} ]; then
        echo "ERROR: Unsupported scheme '$1'."
        exit 1
    fi
    for v in "${colorscheme[@]:0:10}"; do
        _isvalidcolor ${v}
    done
}
_hex2rgb() {
    _isvalidcolor "${1}"
    local hexcolor="${1:1}"
    r=${hexcolor:0:2}
    g=${hexcolor:2:2}
    b=${hexcolor:4:2}
    rgb="$(( 0x$r )) $(( 0x$g  )) $(( 0x$b ))"
    rgbcolor="$(echo $rgb | tr ' ' ,)"
}
_gns3scheme() {
    # this function will change the default gns3-gui interface colors
    _hex2rgb ${colorscheme[11]}
    _changecolor
    _changesymbols
    _fixissues
}
_prettyproject() {
    # change project(s) default fonts, separate devices font from text (note) fonts 
    # this function will set 3 different colors for bold, appliance and note fonts:
    # set appliance (routers, switches, pc, ...,etc) a separate font color
    # set note font color to a different color than appliance or default
    # set any bold color that been set manually on the project to a different color than regular note and appliance
    _backup "gns3_project_files"
    newfontfamily='DejaVuSansMono Nerd Font Mono'
    newafontfamily='DejaVuSansMono Nerd Font Mono'
    newfontcolor="${colorscheme[2]}"
    newafontcolor="${colorscheme[3]}"
    boldfontcolor="${colorscheme[6]}"
    newafontsize=11
    find "${gns3_projects_dir}" -name "*.gns3" -type f -exec sed -i \
        -e "s:\(font-family=..\).[^\\\]*:\1$newfontfamily:g" \
        -e "s:\(text fill=..\).[^\\\]*:\1$newfontcolor:g" \
        -e "/bold/s:\(fill=..\).......:\1$boldfontcolor:g" \
        -e "/compute_id/{n;n;n;n;n;n;n;/style/{s/\(font-family:\).[^;]*/\1 $newafontfamily/" \
        -e "s/\(font-size:\).[^;]*/\1 $newafontsize/" \
        -e "s/\(fill:\).[^;]*/\1 $newafontcolor/" \
        -e "/font-weight/!s/\(font-size.[^;]*\)/\1;font-weight: bold/}}" "{}" \+
    # change default label font and color
    sed -i -e "s/\(\"default_label_color\": \).[^,]*/\1\"$newfontcolor\"/g" \
           -e "s/\(\"default_label_font\": \"\).[^,]*/\1$newfontfamily/g" ${gns3_gui_conf}
}
# change projects symbols (icons) according to theme color
_changesymbols() {
    # this function will change symbols already used by an existing project(s)
    # set the custom symbols that will be used for your light theme
    # set the custom symbols that will be used for your dark theme
    # detect the theme variant and change the symbols accordingly
    _backup "gns3_projects_dir"
    if [ "${colorscheme[12]}" == "light" ]; then
        find ${gns3_projects_dir} -name "*.gns3" -type f -exec sed -i \
            -e "s:multilayer_switch1:multilayer_switch4:g" \
            -e "s:router2:router5:g" \
            -e "s:cloud1:cloud2:g" \
            -e "s:monitoring2:monitoring5:g" \
            -e "s:router_switch_processor1:router_switch_processor4:g" \
            -e "s:PC3\|PC5\|PC2:PC1:g" \
            -e "s:Server4:Server3:g" "{}" \;
    else
        find ${gns3_projects_dir} -name "*.gns3" -type f -exec sed -i \
            -e "s:multilayer_switch4:multilayer_switch1:g" \
            -e "s:router5:router2:g" \
            -e "s:cloud2:cloud1:g" \
            -e "s:monitoring5:monitoring2:g" \
            -e "s:router_switch_processor4:router_switch_processor1:g" \
            -e "s:PC2\|PC1\|PC5:PC3:g" \
            -e "s:Server3:Server4:g" "{}" \;
    fi
    echo "Finished changing project(s) symbols..."
}
_changecolor() {
    if [ "${colorscheme[0]}" != "default" ]; then
        sed -i -e "/QWidget/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QMenuBar::item/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QTextEdit#uiConsole/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QTreeWidget,/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QMenu\ /{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar:vertical/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar:horizontal/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar::up/{n;n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QAbstractScrollArea/{n;s/#[^;].*/"${colorscheme[0]}";/}" "$SRCDIR"/gns3/ui/*.ui 
    fi
    if [ "${colorscheme[1]}" != "default" ]; then
        sed -i -e "/QTextEdit, /{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QHeaderView/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTreeWidget#uiTree/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTabBar::tab\ /{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QScrollBar::handle/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTreeWidget,\ /{n;n;n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QLabel#uiTitleLabel/{n;n;s/#[^;].*/"${colorscheme[1]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[2]}" != "default" ]; then
        sed -i -e "/QDockWidget, /{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTreeWidget,/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QHeaderView/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTreeWidget#uiTree/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTabBar::tab\ /{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTextEdit#uiConsole/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTextEdit,\ /{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QLabel/{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QStatusBar/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QRadioButton/{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QMenu\ /{n;n;s/#[^;].*/"${colorscheme[2]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[3]}" != "default" ]; then
        sed -i -e "/QGroupBox\ /{n;s/#[^;].*/"${colorscheme[3]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[4]}" != "default" ]; then
        sed -i -e "/QDockWidget::title/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/QToolBar/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/QStatusBar/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/QToolButton\ /{n;s/#[^;].*/"${colorscheme[4]}";/}"\
               -e "/QMainWindow::separator/{n;s/#[^;].*/"${colorscheme[4]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[5]}" != "default" ]; then
        sed -i -e "/^QComboBox\ /{n;s/#[^;].*/"${colorscheme[5]}";/}" \
               -e "/QTreeWidget::item:hover/{n;s/#[^;].*/"${colorscheme[5]}";/}" \
               -e "/QMenu::item:selected/{n;s/#[^;].*/"${colorscheme[5]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[6]}" != "default" ]; then
        sed -i -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/^QComboBox\ /{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/QTreeWidget::item:hover/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/QMenu::item:selected/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[7]}" != "default" ]; then
        sed -i -e "/QPushButton\ /{n;s/#[^;].*/"${colorscheme[7]}";/}" \
               -e "/QTabBar::tab:selected/{n;s/#[^;].*/"${colorscheme[7]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[8]}" != "default" ]; then
        sed -i -e "/^QPushButton/{n;n;s/#[^;].*/"${colorscheme[8]}";/}" \
               -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"${colorscheme[8]}";/}" \
               -e "/^QToolButton\ /{n;n;s/#[^;].*/"${colorscheme[8]}";/}" "$SRCDIR"/gns3/ui/*.ui
    fi
    if [ "${colorscheme[9]}" != "default" ]; then
        sed -i "s/\(self\.setPen(QtGui.QPen(\).*black\(,\ self\._pen_width,.*))\)/\1QtGui.QColor(\"${colorscheme[9]}\")\2/" "$SRCDIR"/gns3/items/ethernet_link_item.py
    fi

    if [ "${colorscheme[10]}" != "default" ]; then
        sed -i -e "s/\(self\._pen_width\ =\ \).*$/\1"${colorscheme[10]}"/" \
               -e "s/\(self._point_size\ =\ \).*$/\18/" "$SRCDIR"/gns3/items/link_item.py
    fi
    if [ "${colorscheme[11]}" != "default" ]; then
        #sed -i "s/\(painter\.setPen(QtGui.QPen(QtGui.QColor(\).*[0-9]\+,.*[0-9]\+,.*[0-9]\+\(.[^)]*\)/\1${rgbcolor}\2/" $SRCDIR/gns3/graphics_view.py
        sed -i "s/\(QtGui.QColor(\)[0-9]\+,.*[0-9]\+,.*[0-9]\+\(.[^)]*)\)/\1${rgbcolor}\2/" $SRCDIR/gns3/graphics_view.py
    fi
    # change style
    if [ "${colorscheme[12]}" != "default" ]; then
        _backup gns3_gui_conf
        if [ "${colorscheme[12]}" == "light" ]; then
            sed -i "s/\(\"style\": \).[^,]*/\1\"Classic\"/" ${gns3_gui_conf}
        elif [ "${colorscheme[12]}" == "dark" ]; then
            sed -i "s/\(\"style\": \).[^,]*/\1\"Charcoal\"/" ${gns3_gui_conf}
        fi
    fi
}
# These issues might be solved in future releases of gns3-gui
_fixissues() {
    # grid size already been solved [checked]
    # fix zoom-in zoom-out step values
    sed -i -e "s/\(factor_in = pow(2.0, \).[^///]*\(.[^)]*\)/\130 \2/g" \
           -e "s/\(factor_out = pow(2.0, \).[^///]*\(.[^)]*\)/\1-30 \2/g" $SRCDIR/gns3/main_window.py
}
uifiles=(main.py 
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
    for file in "${uifiles[@]}"; do
        sed -i -e '/.*\.setWindowOpacity.*/d' \
               -e "s/\(^\ *\)\(.*\)\(\.show()$\)/\1\2.setWindowOpacity\($opacityvalue\)\n\1\2\3/g" $SRCDIR/gns3/$file
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
    echo -e "\033[1;92mSuccessfully finished installing gns3-gui"
    echo -e "\033[1;92mRestart gns3 to apply changes"
}
re_digit='^[0-9]{,2}\.[0-9]$'
re_hexcolor='^#[0-9a-fA-F]{6}$'
re_opacity='^0\.[0-9]{,2}$'

#control flags
installFlag=false
opacityFlag=false
prettyFlag=false
schemeFlag=false

OPTS="$(getopt -o o:,s:,p:,ihlvr --long bg:,bg2:,fg:,fg2:,tbg:,opacity:,sbg:,sfg:,bbg:,bfg:,lw:,lc:,gc:,scheme:,pretty:,version,help,install,restore-config -n $0 -- "$@")"
if [ $? -ne 0 ]; then
    echo "Failed parsing options, see '$0 --help' for more info."
    exit 1
fi
while [ $# -gt 0 ] && [ "$1" != "--" ]; do 
    case "$1" in
        --bg)
            _isvalidcolor "#${2}"
            colorscheme[0]="#${2}"
            shift 2
            ;;
        --bg2)
            _isvalidcolor "#${2}"
            colorscheme[1]="#${2}"
            shift 2
            ;;
        --fg)
            _isvalidcolor "#${2}"
            colorscheme[2]="#${2}"
            shift 2
            ;;
        --fg2)
            _isvalidcolor "#${2}"
            colorscheme[3]="#${2}"
            shift 2
            ;;
        --tbg)
            _isvalidcolor "#${2}"
            colorscheme[4]="#${2}"
            shift 2
            ;;
        --sbg)
            _isvalidcolor "#${2}"
            colorscheme[5]="#${2}"
            shift 2
            ;;
        --sfg)
            _isvalidcolor "#${2}"
            colorscheme[6]="#${2}"
            shift 2
            ;;
        --bbg)
            _isvalidcolor "#${2}"
            colorscheme[7]="#${2}"
            shift 2
            ;;
        --bfg)
            _isvalidcolor "#${2}"
            colorscheme[8]="#${2}"
            shift 2
            ;;
        --lc)
            _isvalidcolor "#${2}"
            colorscheme[9]="#${2}"
            shift 2
            ;;
        --lw)
            colorscheme[10]="#${2}"
            shift 2
            ;;
        --gc)
            _isvalidcolor "#${2}"
            colorscheme[11]="#${2}"
            shift 2
            ;;
        -o|--opacity)
            _isvalidopacity "${2}"
            opacityvalue="${2:-1}"
            opacityFlag=true
            shift 2
            ;;
        -r|--restore-config)
            _restore_config "gns3_gui_conf_bak"
            exit 0
            ;;
        -s|--scheme)
            _isvalidscheme "${2}"
            _gns3scheme "${2}" 
            schemeFlag=true
            shift 2
            ;;
        -p|--pretty)
            prettyscheme="${2}"
            prettyFlag=true
            shift 2
            ;;
        -l|--list-schemes)
            _listschemes
            exit 0
            ;;
        -v|--version)
            echo "$0 version 2.2.3"
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
#check for any color(s) change(s)
for i in "${colorscheme[@]}"; do
    if [ "${i}" != "default" ]; then
        installFlag=true
        break
    fi
done
# apply full opacity to gns3-gui
if [ "${opacityFlag}" == true ]; then
    _uitransparent
    #echo "Finished applying opacity..."
fi
# change and install gns3-gui theme
if [ "${installFlag}" == true ]; then
    _isroot
    _changecolor
    _gns3install
fi
# apply separate font color for appliance and note
if [ "${prettyFlag}" == "true" ]; then
    if [ "${schemeFlag}" == false ]; then
        _isvalidscheme ${prettyscheme}
        _changesymbols
    fi
    _prettyproject
    echo "Finished prettifying project(s)..."
fi
exit 0
