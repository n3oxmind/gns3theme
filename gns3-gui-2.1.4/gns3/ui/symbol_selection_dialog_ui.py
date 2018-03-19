# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/symbol_selection_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SymbolSelectionDialog(object):
    def setupUi(self, SymbolSelectionDialog):
        SymbolSelectionDialog.setObjectName("SymbolSelectionDialog")
        SymbolSelectionDialog.resize(521, 655)
        SymbolSelectionDialog.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  color: #839496;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QToolButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover, QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #002b36;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 6px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 6px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::down-arrow:horizontal, QScrollBar::up-arrow:horizontal { \n"
"    border: 0px;\n"
"    height: 0px; \n"
"    width: 0px; \n"
"}\n"
"         \n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none\n"
"}\n"
"QStatusBar {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        SymbolSelectionDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SymbolSelectionDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiCustomSymbolRadioButton = QtWidgets.QRadioButton(SymbolSelectionDialog)
        self.uiCustomSymbolRadioButton.setChecked(True)
        self.uiCustomSymbolRadioButton.setObjectName("uiCustomSymbolRadioButton")
        self.horizontalLayout_2.addWidget(self.uiCustomSymbolRadioButton)
        self.uiBuiltInSymbolRadioButton = QtWidgets.QRadioButton(SymbolSelectionDialog)
        self.uiBuiltInSymbolRadioButton.setObjectName("uiBuiltInSymbolRadioButton")
        self.horizontalLayout_2.addWidget(self.uiBuiltInSymbolRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.uiCustomSymbolGroupBox = QtWidgets.QGroupBox(SymbolSelectionDialog)
        self.uiCustomSymbolGroupBox.setObjectName("uiCustomSymbolGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiCustomSymbolGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSymbolLabel = QtWidgets.QLabel(self.uiCustomSymbolGroupBox)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.uiCustomSymbolGroupBox)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.uiCustomSymbolGroupBox)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiCustomSymbolGroupBox)
        self.uiBuiltInGroupBox = QtWidgets.QGroupBox(SymbolSelectionDialog)
        self.uiBuiltInGroupBox.setObjectName("uiBuiltInGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiBuiltInGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiBuiltinSymbolOnlyCheckBox = QtWidgets.QCheckBox(self.uiBuiltInGroupBox)
        self.uiBuiltinSymbolOnlyCheckBox.setObjectName("uiBuiltinSymbolOnlyCheckBox")
        self.verticalLayout.addWidget(self.uiBuiltinSymbolOnlyCheckBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiSearchLabel = QtWidgets.QLabel(self.uiBuiltInGroupBox)
        self.uiSearchLabel.setObjectName("uiSearchLabel")
        self.horizontalLayout_3.addWidget(self.uiSearchLabel)
        self.uiSearchLineEdit = QtWidgets.QLineEdit(self.uiBuiltInGroupBox)
        self.uiSearchLineEdit.setObjectName("uiSearchLineEdit")
        self.horizontalLayout_3.addWidget(self.uiSearchLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.uiSymbolListWidget = QtWidgets.QListWidget(self.uiBuiltInGroupBox)
        self.uiSymbolListWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.uiSymbolListWidget.setObjectName("uiSymbolListWidget")
        self.verticalLayout.addWidget(self.uiSymbolListWidget)
        self.label = QtWidgets.QLabel(self.uiBuiltInGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.uiBuiltInGroupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SymbolSelectionDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uiBuiltInGroupBox.raise_()
        self.uiCustomSymbolGroupBox.raise_()

        self.retranslateUi(SymbolSelectionDialog)
        self.uiButtonBox.accepted.connect(SymbolSelectionDialog.accept)
        self.uiButtonBox.rejected.connect(SymbolSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SymbolSelectionDialog)

    def retranslateUi(self, SymbolSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        SymbolSelectionDialog.setWindowTitle(_translate("SymbolSelectionDialog", "Symbol selection"))
        self.uiCustomSymbolRadioButton.setText(_translate("SymbolSelectionDialog", "Use a custom symbol"))
        self.uiBuiltInSymbolRadioButton.setText(_translate("SymbolSelectionDialog", "Symbols library"))
        self.uiCustomSymbolGroupBox.setTitle(_translate("SymbolSelectionDialog", "Custom symbol"))
        self.uiSymbolLabel.setText(_translate("SymbolSelectionDialog", "Path:"))
        self.uiSymbolToolButton.setText(_translate("SymbolSelectionDialog", "&Browse..."))
        self.uiBuiltInGroupBox.setTitle(_translate("SymbolSelectionDialog", "Symbols"))
        self.uiBuiltinSymbolOnlyCheckBox.setText(_translate("SymbolSelectionDialog", "Show only built-in symbols"))
        self.uiSearchLabel.setText(_translate("SymbolSelectionDialog", "Search:"))
        self.label.setText(_translate("SymbolSelectionDialog", "You can add your own symbols in the symbols directory."))

from . import resources_rc
