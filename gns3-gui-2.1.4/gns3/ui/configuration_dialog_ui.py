# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/configuration_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configurationDialog(object):
    def setupUi(self, configurationDialog):
        configurationDialog.setObjectName("configurationDialog")
        configurationDialog.resize(585, 454)
        configurationDialog.setStyleSheet("QWidget{\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QDockWidget::title{\n"
"    background: #d5c4a1;\n"
"    padding-left: 5px;\n"
"}\n"
"QDockWidget, QMenuBar{\n"
"    color: #282828;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #d5c4a1;\n"
"  font: 13px;\n"
"  color: #282828;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #fbf1c7;\n"
"  color: #282828;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #d5c4a1;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #458588;\n"
"    color: #FFFFFF;\n"
"}\n"
"QGroupBox {\n"
"    color: #076678;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #d5c4a1;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #458588;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #d5c4a1;\n"
"    border: 0px;\n"
"}\n"
" QPushButton {\n"
"    background-color: #d79921;\n"
"    font: 14px;\n"
"}\n"
"QToolButton {\n"
"    /*background-color: transparent; mainwindowonly*/\n"
"    background-color: #d79921;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #fbf1c7;\n"
"    color: #282828;\n"
"    font: 14px;\n"
"    /*font: 12px; for mainwindow*/\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #d5c4a1;\n"
"    color: #282828;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover, QMenu::item:selected,QToolButton::hover,QPushButton::hover {\n"
"    background-color: #458588;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QLabel {\n"
"    color: #282828;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #282828;\n"
"    font: bold 16px;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #fbf1c7;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #d5c4a1;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #d5c4a1;\n"
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
"    background-color: #d5c4a1;\n"
"    color: #282828;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #282828;\n"
"}\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        configurationDialog.setModal(True)
        self.gridlayout = QtWidgets.QGridLayout(configurationDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.splitter = QtWidgets.QSplitter(configurationDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayout = QtWidgets.QWidget(self.splitter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiTitleLabel = QtWidgets.QLabel(self.verticalLayout)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.uiTitleLabel.setFont(font)
        self.uiTitleLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.uiTitleLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uiTitleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.uiTitleLabel.setObjectName("uiTitleLabel")
        self.vboxlayout.addWidget(self.uiTitleLabel)
        self.uiConfigStackedWidget = QtWidgets.QStackedWidget(self.verticalLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiConfigStackedWidget.sizePolicy().hasHeightForWidth())
        self.uiConfigStackedWidget.setSizePolicy(sizePolicy)
        self.uiConfigStackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.uiConfigStackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uiConfigStackedWidget.setObjectName("uiConfigStackedWidget")
        self.uiEmptyPageWidget = QtWidgets.QWidget()
        self.uiEmptyPageWidget.setObjectName("uiEmptyPageWidget")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.uiEmptyPageWidget)
        self.vboxlayout1.setContentsMargins(0, 4, 0, 0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.uiConfigStackedWidget.addWidget(self.uiEmptyPageWidget)
        self.vboxlayout.addWidget(self.uiConfigStackedWidget)
        self.gridlayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(configurationDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridlayout.addWidget(self.uiButtonBox, 1, 0, 1, 1)

        self.retranslateUi(configurationDialog)
        self.uiConfigStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(configurationDialog)

    def retranslateUi(self, configurationDialog):
        _translate = QtCore.QCoreApplication.translate
        configurationDialog.setWindowTitle(_translate("configurationDialog", "Configuration"))
        self.uiTitleLabel.setText(_translate("configurationDialog", "Configuration"))

from . import resources_rc
