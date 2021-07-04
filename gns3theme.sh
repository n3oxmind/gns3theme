#!/usr/bin/env bash
set -eo errexit

SRCDIR=""
tmpdir=""
USERNAME=""
OSTYPE="linx"
colorscheme=( "default" "default" "default" "default" "default" \
              "default" "default" "default" "default" "default" \
              "default" "default" "default" )  

custom_css="QWidget{\n\tbackground-color: #fbf1c7;\n}\nQMenuBar::item{\n\tbackground-color: #fbf1c7;\n}\nQDockWidget::title{\n\tbackground: #d5c4a1;\n\tpadding-left: 5px;\n}\nQDockWidget, QMenuBar{\n\tcolor: #282828;\n\tfont: bold 14px;\n}\nQTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox{\n\tbackground-color: #d5c4a1;\n\tcolor: #282828;\n}\nQTextEdit#uiConsoleTextEdit{\n\tbackground-color: #fbf1c7;\n\tcolor: #282828;\n\tfont: 13px;\n}\nQTabWidget{\n\tfont: 14px;\n\tborder-top: 2px;\n}\nQTabBar::tab{\n\tbackground: #d5c4a1;\n\tcolor: #282828;\n\tmin-width: 8ex;\n\tpadding: 2px;\n\tborder-top-right-radius: 6px;\n\tborder-top-left-radius: 6px;\n}\nQTabBar::tab:selected{\n\tbackground: #458588;\n\tcolor: #FFFFFF;\n}\nQGroupBox{\n\tcolor: #076678;\n\tfont: 14px;\n\tpadding: 15px;\n\tborder-style: none;\n}\nQMainWindow::separator{\n\tbackground: #d5c4a1;\n\twidth: 1px;\n\theight: 1px;\n}\nQComboBox{\n\tselection-background-color: #458588;\n\tselection-color: #FFFFFF;\n}\nQToolBar{\n\tbackground: #d5c4a1;\n\tborder: 0px;\n}\nQPushButton{\n\tbackground-color: #d79921;\n\tcolor: #181818;\n\tfont: 14px;\n}\nQToolButton{\n\tbackground-color: #d5c4a1;\n\tcolor: #181818;\n\tfont: 14px;\n}\nQTreeWidget, QListWidget{\n\tbackground-color: #fbf1c7;\n\tcolor: #282828;\n\talternate-background-color: #d5c4a1; \n\tfont: 14px;\n}\nQTreeWidget#uiTreeWidget{\n\tbackground-color: #d5c4a1;\n\tcolor: #282828;\n\tfont: bold 16px;\n}\nQTreeWidget::item:selected, QTreeWidget::item:hover, QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover{\n\tbackground-color: #458588;\n\tcolor: #fafafa;\n}\nQMenu{\n\tbackground-color: #fbf1c7;\n\tcolor: #282828;\n}\nQLabel{\n\tcolor: #282828;\n\tfont: 14px;\n}\nQLabel#uiTitleLabel{\n\tcolor: #282828;\n\tfont: bold 16px;\n}\nQAbstractScrollArea::corner{\n\tbackground: #fbf1c7;\n}\nQScrollBar::handle:horizontal{\n\tbackground: #d5c4a1;\n\tmin-width: 20px;\n}\nQScrollBar::handle:vertical{\n\tbackground: #d5c4a1;\n\tmin-width: 20px;\n}\nQScrollBar:vertical{\n\twidth: 6px;\n}\nQScrollBar:horizontal{\n\theight: 6px;\n}\nQScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::down-arrow:horizontal, QScrollBar::up-arrow:horizontal{ \n\tborder: 0px;\n\theight: 0px; \n\twidth: 0px; \n}\nQScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n\tbackground: none\n}\nQStatusBar{\n\tbackground-color: #d5c4a1;\n\tcolor: #282828;\n}\nQRadioButton, QCheckBox{\n\tcolor: #282828;\n}\nQRadioButton::disabled, QCheckBox::disabled{\n\tcolor: gray;\n}"

if [ $(uname) == "Darwin" ]; then
    OSTYPE="Darwin"
fi
set_custom_theme() {
    USERNAME="${1}"
    THEME_TEMPLATE="/home/$USERNAME/.config/gns3theme/custom.css"
    if [ ${OSTYPE} == "Darwin" ]; then
        THEME_TEMPLATE="/Users/$USERNAME/.config/gns3theme/custom.css"
    fi
    if [ ! -f "${THEME_TEMPLATE}" ]; then
        mkdir -p ${THEME_TEMPLATE%/*}
        echo -e ${custom_css} > ${THEME_TEMPLATE}
        chown ${USERNAME} ${THEME_TEMPLATE}
        chmod 755 ${THEME_TEMPLATE}
    fi
}
#
usage() {
    printf "%s\n" "Usage: $0 --scheme <scheme-name> [OPTIONS] -u <username>"
    printf "%s\n" "   or: $0 --scheme <scheme-name> [OPTIONS] -u <username> --opacity <num>"
    printf "%s\n" "   or: $0 -u <username> [OPTION].. "
    printf "%s\n" "OPTIONS:"
    printf "  %s\t\t\t%s\n" "--bg"  "Change primary background color"
    printf "  %s\t\t\t%s\n" "--bg2" "Change secondary background color"
    printf "  %s\t\t\t%s\n" "--fg"  "Change primary foreground color"
    printf "  %s\t\t\t%s\n" "--fg2" "Change secondary foreground color"
    printf "  %s\t\t\t%s\n" "--tbg" "Change toolbar background color"
    printf "  %s\t\t\t%s\n" "--sbg" "Change selection background color"
    printf "  %s\t\t\t%s\n" "--sfg" "Change selelction foreground color"
    printf "  %s\t\t\t%s\n" "--btn" "Change button background color"
    printf "  %s\t\t\t%s\n" "--lc" "Change ethernet link color. Required reinstall gns3-gui"
    printf "  %s\t\t\t%s\n" "--gc" "Change grid color. Required reinstall"
    printf "  %s\t\t\t%s\n" "--src" "Path to gns3-gui source files directory"
    printf "  %s\t\t\t%s\n" "--lw" "Change ethernet and serial links width, Required reinstall gns3-gui"
    printf "  %s\t\t\t%s\n" "-u" "Specify username. Manditory option"
    printf "  %s\t\t%s\n" "-o, --opacity" "Apply transparency to gns3 gui. Required reinstall gns3-gui"
    printf "  %s\t\t%s\n" "-s, --scheme" "Change gns3 theme from predefined schemes"
    printf "  %s\t%s\n" "-l, --list-schemes" "List gns3 schemes"
    printf "\n"
    printf "%s\n" "Run this command only once as a root"
    printf "  %s\t\t%s\n"  "sudo ./gns3theme.sh --install --src /path/to/gns3-gui-source-dir -u <username>" 
    printf "%s\n" "Install theme from predefined schemes"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme gruvbox-light -u <username>" 
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light -u <username>" 
    printf "%s\n" "Use the scheme but with different selection color"
    printf "  %s\t\t%s\n"  "./gns3theme.sh --scheme solarized-light --sbg ef5350 -u <username>"
    printf "%s\n" "Install custom scheme"
    printf "  %s\t\t%s\n"  "./gns3theme.sh  -u <username> --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 .." 
    printf "  %s\t\t%s\n"  "./gns3theme.sh -u <username> --bg 282828 --bg2 323232 --fg FFFFFF --tbg 303030 -o 0.95 .." 
    printf "%s\n" "Change link and grid color"
    printf "  %s\t\t%s\n"  "./gns3theme.sh  -u <username>  --install --scheme n30x-darkw --lc 939393 --gc 323232" 
}

trap clean_up 0 1 2 15
clean_up() {
#    rm -rf ${tmpdir}
    echo $tmpdir
    #echo "Finished cleaning."
}

# Validate color
is_valid_color () {
    if [[ ! "$1" =~ $re_hexcolor ]]; then
        echo "ERROR: Color must be in hex format or names e.g. "2d2d2d". "
        exit 1
    fi
}

# Validate gns3-gui opacity
is_valid_opacity () {
    if [[ ! "$1" =~ $re_opacity ]] && [ "$1" != "1.0" ] ; then
        echo "ERROR: Window opacity must be between 0.0 and 1.0"
        exit 1
    fi
}
# Check if the script running as root
is_root () {
    if [ "$(whoami)" != "root" ]; then
        echo "Please, run as root"
        exit 1
    fi
}

# List pre-defined color schemes
print_colorschemes() {
    sed -n '/scheme-template/,$p' ./colorschemes
}

# Validate colorscheme
is_valid_scheme() {
    colorscheme=($(grep "^${1}:" ./colorschemes | cut -d: -f2))
    if [ -z ${colorscheme} ]; then
        echo "ERROR: Unsupported scheme '$1'."
        exit 1
    fi
    for v in "${colorscheme[@]:0:10}"; do
        is_valid_color ${v}
    done
}

# Validate user
is_valid_user() {
    if ! id "${1}" >/dev/null 2>&1; then
        echo "User does not exist '${1}'."
        exit 1
    fi
}
# change color format to RBG 
hex_to_rbg () {
    is_valid_color "${1}"
    local hexcolor="${1:1}"
    r=${hexcolor:0:2}
    g=${hexcolor:2:2}
    b=${hexcolor:4:2}
    rgb="$(( 0x$r )) $(( 0x$g  )) $(( 0x$b ))"
    rgbcolor="$(echo $rgb | tr ' ' ,)"
}

# Change the default gns3-gui colorscheme
gns3_colorscheme() {
    if [ ! "${colorscheme[11]}" == "default" ]; then
        hex_to_rbg  ${colorscheme[11]}
    fi
    change_colorscheme 
}

# Change colorscheme. gns3-gui restart is not required
change_colorscheme() {
    if [ "${colorscheme[0]}" != "default" ]; then
        sed -i -e "/QWidget/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QMenuBar::item/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QTextEdit#uiConsole/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QTreeWidget,/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QMenu{/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar:vertical/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar:horizontal/{n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QScrollBar::up/{n;n;s/#[^;].*/"${colorscheme[0]}";/}" \
               -e "/QAbstractScrollArea/{n;s/#[^;].*/"${colorscheme[0]}";/}" ${THEME_TEMPLATE} 
    fi
    if [ "${colorscheme[1]}" != "default" ]; then
        sed -i -e "/QTextEdit,/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QHeaderView/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTreeWidget#uiTree/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTabBar::tab{/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QScrollBar::handle/{n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QTreeWidget,/{n;n;n;s/#[^;].*/"${colorscheme[1]}";/}" \
               -e "/QLabel#uiTitleLabel/{n;n;s/#[^;].*/"${colorscheme[1]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[2]}" != "default" ]; then
        sed -i -e "/QDockWidget,/{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTreeWidget,/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QHeaderView/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTreeWidget#uiTree/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTabBar::tab{/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTextEdit#uiConsole/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QTextEdit,/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QLabel/{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QStatusBar/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QRadioButton/{n;s/#[^;].*/"${colorscheme[2]}";/}" \
               -e "/QMenu{/{n;n;s/#[^;].*/"${colorscheme[2]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[3]}" != "default" ]; then
        sed -i -e "/QGroupBox/{n;s/#[^;].*/"${colorscheme[3]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[4]}" != "default" ]; then
        sed -i -e "/QDockWidget::title/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/QToolBar/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/QStatusBar/{n;s/#[^;].*/"${colorscheme[4]}";/}" \
               -e "/^QToolButton/{n;s/#[^;].*/"${colorscheme[4]}";/}"\
               -e "/QMainWindow::separator/{n;s/#[^;].*/"${colorscheme[4]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[5]}" != "default" ]; then
        sed -i -e "/^QComboBox/{n;s/#[^;].*/"${colorscheme[5]}";/}" \
               -e "/QTreeWidget::item:hover/{n;s/#[^;].*/"${colorscheme[5]}";/}" \
               -e "/QMenu::item:selected/{n;s/#[^;].*/"${colorscheme[5]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[6]}" != "default" ]; then
        sed -i -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/^QComboBox/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/QTreeWidget::item:hover/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" \
               -e "/QMenu::item:selected/{n;n;s/#[^;].*/"${colorscheme[6]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[7]}" != "default" ]; then
        sed -i -e "/^QPushButton/{n;s/#[^;].*/"${colorscheme[7]}";/}" \
               -e "/QTabBar::tab:selected/{n;s/#[^;].*/"${colorscheme[7]}";/}" ${THEME_TEMPLATE}
    fi
    if [ "${colorscheme[8]}" != "default" ]; then
        sed -i -e "/^QPushButton/{n;n;s/#[^;].*/"${colorscheme[8]}";/}" \
               -e "/QTabBar::tab:selected/{n;n;s/#[^;].*/"${colorscheme[8]}";/}" \
               -e "/^QToolButton/{n;n;s/#[^;].*/"${colorscheme[8]}";/}" ${THEME_TEMPLATE}
    fi

}

# Change grid color. gns3-gui reinstall required
change_grid_color() {
    if [ "${colorscheme[11]}" != "default" ]; then
        sed -i "s/\(QtGui.QColor(\)[0-9].*),/\1${rgbcolor})),/" "${tmpdir}"/gns3/graphics_view.py
        sed -i "s/\(QtGui.QColor(\)[0-9].*)]/\1${rgbcolor}))]/" "${tmpdir}"/gns3/graphics_view.py
    fi
}

# Change grid color. gns3-gui reinstall required
change_link_color() {
    if [ "${colorscheme[9]}" != "default" ]; then
        sed -i "s/\(self\.setPen(QtGui.QPen(\).*black\(,\ self\._pen_width,.*))\)/\1QtGui.QColor(\"${colorscheme[9]}\")\2/" "${tmpdir}"/gns3/items/ethernet_link_item.py
    fi

    if [ "${colorscheme[10]}" != "default" ]; then
        sed -i -e "s/\(self\._pen_width\ =\ \).*$/\1"${colorscheme[10]}"/" \
               -e "s/\(self._point_size\ =\ \).*$/\18/" "${tmpdir}"/gns3/items/link_item.py
    fi
}

# these files will be modifed if one of these options is present [-o, --lc, --lw, --gc]
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

# apply full transparency to gns3-gui elements
apply_transparency() {
    for file in "${uifiles[@]}"; do
        sed -i -e '/.*\.setWindowOpacity.*/d' \
               -e "s/\(^\ *\)\(.*\)\(\.show()$\)/\1\2.setWindowOpacity\($opacityvalue\)\n\1\2\3/g" "${tmpdir}"/gns3/$file
    done 
}
# generate custom stylesheet
_custom_style_patch() {
    local tmpdir=${1}
    #settings.py
    sed -i 's/\(^STYLES\s\+=.*\)]$/\1, "CustomLight", "CustomDark"]/' ${tmpdir}/gns3/settings.py
    # main_window.py
    sed -i '/style\.setClassicStyle()/a\
        elif style_name == "CustomLight":\
            style.setCustomLightStyle()\
        elif style_name == "CustomDark":\
            style.setCustomDarkStyle()' ${tmpdir}/gns3/main_window.py
    #style.py
    # dark theme
    sed -n '/\s\+def\s\+setCharcoalStyle/,$p' "${tmpdir}"/gns3/style.py > new_style_dark
    sed -i 's/setCharcoalStyle/setCustomDarkStyle/' ./new_style_dark
    sed -i "s:\:/styles/charcoal.css:${THEME_TEMPLATE}:" ./new_style_dark
    echo -e "\n"  >> ${tmpdir}/gns3/style.py
    cat ./new_style_dark >> ${tmpdir}/gns3/style.py

    # light theme
    sed -i 's/setCustomDarkStyle/setCustomLightStyle/' ./new_style_dark
    sed -i 's/charcoal_icons/classic_icons/' ./new_style_dark
    sed -i 's/-1//' ./new_style_dark
    echo -e "\n"  >> ${tmpdir}/gns3/style.py
    cat ./new_style_dark >> ${tmpdir}/gns3/style.py
}

# Install gns3-gui
gns3_gui_install () {
    # perform clean up
    find /usr/lib \( -name "gns3" -o -name "gns3_gui-*.egg" -o -name "gns3_gui-*.egg-info" \) -type d -prune -exec rm -rf "{}" \+
    find /usr/local/lib \( -name "gns3" -o -name "gns3_gui-*.egg" -o -name "gns3_gui-*.egg-info" \) -type d -prune -exec rm -rf "{}" \+
    # copy src to temp
    tmpdir=$(mktemp -d -t gns3theme.XXXXXXXX)
    cp -af ${SRCDIR}/* ${tmpdir}
    cd $tmpdir
    # patch gns3-gui for custom theme
    _custom_style_patch $tmpdir

    # apply full opacity to gns3-gui
    if [ "${opacityFlag}" == true ]; then
        apply_transparency
    fi

    if [ "${schemeFlag}" == true ]; then
        gns3_colorscheme
    fi
    # change link color/width
    change_link_color
    # change grid color
    change_grid_color
    # apply changes and install 
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
linkFlag=false
gridFlag=false
userFlag=false

OPTS="$(getopt -o o:,s:,p:,d:,u:,ihlv --long src:,bg:,bg2:,fg:,fg2:,tbg:,opacity:,sbg:,sfg:,bbg:,bfg:,lw:,lc:,gc:,scheme:,version,help,install -n $0 -- "$@")"
if [ $? -ne 0 ]; then
    echo "Failed parsing options, see '$0 --help' for more info."
    exit 1
fi
while [ $# -gt 0 ] && [ "$1" != "--" ]; do 
    case "$1" in
        -d|--src)
            SRCDIR="${2}"
            shift 2
            ;;
        --bg)
            is_valid_color "#${2}"
            colorscheme[0]="#${2}"
            shift 2
            ;;
        --bg2)
            is_valid_color "#${2}"
            colorscheme[1]="#${2}"
            shift 2
            ;;
        --fg)
            is_valid_color "#${2}"
            colorscheme[2]="#${2}"
            shift 2
            ;;
        --fg2)
            is_valid_color "#${2}"
            colorscheme[3]="#${2}"
            shift 2
            ;;
        --tbg)
            is_valid_color "#${2}"
            colorscheme[4]="#${2}"
            shift 2
            ;;
        --sbg)
            is_valid_color "#${2}"
            colorscheme[5]="#${2}"
            shift 2
            ;;
        --sfg)
            is_valid_color "#${2}"
            colorscheme[6]="#${2}"
            shift 2
            ;;
        --bbg)
            is_valid_color "#${2}"
            colorscheme[7]="#${2}"
            shift 2
            ;;
        --bfg)
            is_valid_color "#${2}"
            colorscheme[8]="#${2}"
            shift 2
            ;;
        --lc)
            linkFlag=true
            is_valid_color "#${2}"
            colorscheme[9]="#${2}"
            shift 2
            ;;
        --lw)
            linkFlag=true
            colorscheme[10]="${2}"
            shift 2
            ;;
        --gc)
            gridFlag=true
            if [ ! ${2} == "default" ]; then
                is_valid_color "#${2}"
                colorscheme[11]="#${2}"
            fi
            shift 2
            ;;
        -o|--opacity)
            is_valid_opacity "${2}"
            opacityvalue="${2:-1}"
            opacityFlag=true
            shift 2
            ;;
        -s|--scheme)
            is_valid_scheme "${2}"
            schemeFlag=true
            shift 2
            ;;
        -u|--user)
            USERNAME="${2}"
            is_valid_user "${USERNAME}"
            set_custom_theme $USERNAME
            userFlag=true
            shift 2
            ;;
        -i|--install)
            installFlag=true
            shift 1
            ;;
        -l|--list-schemes)
            print_colorschemes
            exit 0
            ;;
        -v|--version)
            echo "$0 version 3.0.0"
            exit 0
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *) 
            echo "Unrecognized argument: "$1""
            exit 1
            ;;
    esac
done

#check for any colorscheme changes
for i in "${colorscheme[@]}"; do
    if [ "${i}" != "default" ]; then
        schemeFlag=true
        break
    fi
done
if [ ! "${userFlag}" == true ]; then
    echo "username is required. Please specify username using '-u'."
    exit 1
fi
# applying colorscheme
if [ "${schemeFlag}" == true ] && [ ! "${installFlag}" == true ]; then
    gns3_colorscheme
    echo "Finished applying colorscheme"
fi

# install gns3-gui with custom theme capability
if [ "${installFlag}" == true ]; then
    if [ "${SRCDIR}" == "" ]; then
        echo "Please specify 'gns3-gui-version' source directory, use --src"
        exit 1
    elif [ ! -d "${SRCDIR}" ]; then
        echo "Directory does not exist '${SRCDIR}'" 
        exit 1
    fi
    is_root
    gns3_gui_install
fi
exit 0
