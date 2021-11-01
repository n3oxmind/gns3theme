# custom css style
# shortcut for long dict key

selector00 = 'QWidget'
selector01 = 'QMenuBar::item'
selector02 = 'QDockWidget::title'
selector03 = 'QDockWidget,QMenuBar'
selector04 = "QTextEdit,QPlainTextEdit,QLineEdit,QSpinBox,QComboBox"
selector05 = 'QTextEdit#uiConsoleTextEdit'
selector06 = 'QTabWidget'
selector07 = 'QTabBar::tab'
selector08 = 'QTabBar::tab:selected'
selector09 = 'QGroupBox'
selector10 = 'QMainWindow::separator'
selector11 = 'QComboBox'
selector12 = 'QToolBar'
selector13 = 'QPushButton'
selector14 = 'QToolButton'
selector15 = 'QTreeWidget,QlistWidget'
selector16 = 'QTreeWidget#uiTreeWidget'
selector17 = "QTreeWidget::item:selected,QTreeWidget::item:hover,QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover"
selector18 = 'QMenu'
selector19 = 'QLabel'
selector20 = 'QLabel#uiTitleLabel'
selector21 = 'QAbstractScrollArea'
selector22 = 'QScrollBar::handle:vertical'
selector23 = 'QScrollBar::handle:horizontal'
selector24 = 'QScrollBar::horizontal'
selector25 = 'QScrollBar::vertical'
selector26 = "QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical,QScrollBar::down-arrow:horizontal,QScrollBar::up-arrow:horizontal"
selector27= "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal,QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
selector28 = 'QStatusBar'
selector29 = 'QRadioButton,QCheckBox'
selector30 = "QRadioButton::disabled,QCheckBox::disabled"

custom_style = {
    selector00: {
        'background-color': '#fbf1c7'
    },
    selector01: {
        'background-color': '#fbf1c7'
    },
    selector02: {
        'background': '#d5c4a1',
        'padding-left': '5px'
    },
    selector03: {
        'color': '#282828',
        'font': 'bold 14px'
    },
    selector04: {
        'background-color': '#d5c4a1',
        'color': '#282828'
    },
    selector05: {
        'backgroun-color': '#fbf1c7',
        'color': '#282828',
        'font': 'bold 14px'
    },
    selector06: {
        'font': '14px',
        'border-top': '2px'
    },
    selector07: {
        'background': '#d5c4a1',
        'color': '#282828',
        'min-width': '8ex',
        'padding': '2px',
        'border-top-right-radius': '6px',
        'border-top-left-radius': '6px'
     },
    selector08: {
        'background': '#458588',
        'color': '#ffffff'
    },
    selector09: {
        'color': '#076678',
        'font': '14px',
        'padding': '15px',
        'border-style': 'none'
    },
    selector10: {
        'background': '#d5c4a1',
        'width': '1px',
        'height': '1px'
    },
    selector11: {
        'selection-background-color': '#458588',
        'selection-color': '#ffffff'
    },
    selector12: {
        'background': '#d5c4a1',
        'border': '0px'
    },
    selector13: {
        'background-color': '#d5c4a1',
        'color': '#181818',
        'font': '14px'
    },
    selector14: {
        'background-color': '#d5c4a1',
        'color': '#181818',
        'font': '14px'
    },
    selector15: {
        'background-color': '#fbf1c7',
        'color': '#282828',
        'alternate-background-color': '#d5c4a1',
        'font': '14px'
    },
    selector16: {
        'background-color': '#d5c4a1',
        'color': '#282828',
        'font': 'bold 14px'
    },
    selector17: {
        'background-color': '#458588',
        'color': '#fafafa'
    },
    selector18: {
        'background-color': '#458588',
        'color': '#282828'
    },
    selector19: {
        'font': '14px',
        'color': '#282828'
    },
    selector20: {
        'font': 'bold 16px',
        'color': '#282828'
    },
    selector21: {
        'background': '#fbf1c7'
    },
    selector22: {
        'background': '#d5c4a1',
        'min-width': '20px'
    },
    selector23: {
        'background': '#d5c4a1',
        'min-width': '20px'
    },
    selector24: {
        'height': '6px'
    },
    selector25: {
        'width': '6px'
    },
    selector26: {
        'border': '0px',
        'height': '0px',
        'width': '0px'
    },
    selector27: {
        'background': 'none'
    },
    selector28: {
        'background-color': '#d5c4a1',
        'color': '#282828'
    },
    selector29: {
        'color': '#282828'
    },
    selector30: {
        'color': 'gray'
    }
}
