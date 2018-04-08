# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/gns3_vm_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GNS3VMPreferencesPageWidget(object):
    def setupUi(self, GNS3VMPreferencesPageWidget):
        GNS3VMPreferencesPageWidget.setObjectName("GNS3VMPreferencesPageWidget")
        GNS3VMPreferencesPageWidget.resize(476, 517)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GNS3VMPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        GNS3VMPreferencesPageWidget.setSizePolicy(sizePolicy)
        GNS3VMPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        GNS3VMPreferencesPageWidget.setStyleSheet("QWidget{\n"
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
"color: #282828;\n"
" }\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(GNS3VMPreferencesPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiEnableVMCheckBox = QtWidgets.QCheckBox(GNS3VMPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEnableVMCheckBox.sizePolicy().hasHeightForWidth())
        self.uiEnableVMCheckBox.setSizePolicy(sizePolicy)
        self.uiEnableVMCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiEnableVMCheckBox.setChecked(False)
        self.uiEnableVMCheckBox.setObjectName("uiEnableVMCheckBox")
        self.verticalLayout.addWidget(self.uiEnableVMCheckBox)
        self.uiVirtualizationGroupBox = QtWidgets.QGroupBox(GNS3VMPreferencesPageWidget)
        self.uiVirtualizationGroupBox.setStyleSheet("QWidget{\n"
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
        self.uiVirtualizationGroupBox.setObjectName("uiVirtualizationGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiVirtualizationGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiGNS3VMEngineComboBox = QtWidgets.QComboBox(self.uiVirtualizationGroupBox)
        self.uiGNS3VMEngineComboBox.setObjectName("uiGNS3VMEngineComboBox")
        self.verticalLayout_2.addWidget(self.uiGNS3VMEngineComboBox)
        self.uiEngineDescriptionLabel = QtWidgets.QLabel(self.uiVirtualizationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEngineDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.uiEngineDescriptionLabel.setSizePolicy(sizePolicy)
        self.uiEngineDescriptionLabel.setWordWrap(True)
        self.uiEngineDescriptionLabel.setOpenExternalLinks(True)
        self.uiEngineDescriptionLabel.setObjectName("uiEngineDescriptionLabel")
        self.verticalLayout_2.addWidget(self.uiEngineDescriptionLabel)
        self.verticalLayout.addWidget(self.uiVirtualizationGroupBox)
        self.uiGNS3VMSettingsGroupBox = QtWidgets.QGroupBox(GNS3VMPreferencesPageWidget)
        self.uiGNS3VMSettingsGroupBox.setStyleSheet("QWidget{\n"
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
        self.uiGNS3VMSettingsGroupBox.setObjectName("uiGNS3VMSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGNS3VMSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiActionCloseLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiActionCloseLabel.setObjectName("uiActionCloseLabel")
        self.gridLayout.addWidget(self.uiActionCloseLabel, 8, 0, 1, 2)
        self.uiHeadlessCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiHeadlessCheckBox.setObjectName("uiHeadlessCheckBox")
        self.gridLayout.addWidget(self.uiHeadlessCheckBox, 1, 0, 1, 2)
        self.uiWhenExitKeepRadioButton = QtWidgets.QRadioButton(self.uiGNS3VMSettingsGroupBox)
        self.uiWhenExitKeepRadioButton.setObjectName("uiWhenExitKeepRadioButton")
        self.gridLayout.addWidget(self.uiWhenExitKeepRadioButton, 9, 0, 1, 2)
        self.uiWhenExitSuspendRadioButton = QtWidgets.QRadioButton(self.uiGNS3VMSettingsGroupBox)
        self.uiWhenExitSuspendRadioButton.setObjectName("uiWhenExitSuspendRadioButton")
        self.gridLayout.addWidget(self.uiWhenExitSuspendRadioButton, 10, 0, 1, 2)
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.gridLayout.addWidget(self.uiVMNameLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.horizontalLayout.addWidget(self.uiVMListComboBox)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiGNS3VMSettingsGroupBox)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout.addWidget(self.uiRefreshPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.uiWhenExitStopRadioButton = QtWidgets.QRadioButton(self.uiGNS3VMSettingsGroupBox)
        self.uiWhenExitStopRadioButton.setObjectName("uiWhenExitStopRadioButton")
        self.gridLayout.addWidget(self.uiWhenExitStopRadioButton, 11, 0, 1, 2)
        self.uiRamLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout.addWidget(self.uiRamLabel, 4, 0, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.uiGNS3VMSettingsGroupBox)
        self.uiRamSpinBox.setMinimum(512)
        self.uiRamSpinBox.setMaximum(1000000)
        self.uiRamSpinBox.setSingleStep(512)
        self.uiRamSpinBox.setProperty("value", 2048)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout.addWidget(self.uiRamSpinBox, 4, 1, 1, 1)
        self.uiCpuSpinBox = QtWidgets.QSpinBox(self.uiGNS3VMSettingsGroupBox)
        self.uiCpuSpinBox.setMinimum(1)
        self.uiCpuSpinBox.setProperty("value", 1)
        self.uiCpuSpinBox.setObjectName("uiCpuSpinBox")
        self.gridLayout.addWidget(self.uiCpuSpinBox, 5, 1, 1, 1)
        self.uiCpuLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiCpuLabel.setObjectName("uiCpuLabel")
        self.gridLayout.addWidget(self.uiCpuLabel, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiGNS3VMSettingsGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GNS3VMPreferencesPageWidget)
        QtCore.QMetaObject.connectSlotsByName(GNS3VMPreferencesPageWidget)

    def retranslateUi(self, GNS3VMPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        GNS3VMPreferencesPageWidget.setWindowTitle(_translate("GNS3VMPreferencesPageWidget", "GNS3 VM"))
        self.uiEnableVMCheckBox.setText(_translate("GNS3VMPreferencesPageWidget", "Enable the GNS3 VM"))
        self.uiVirtualizationGroupBox.setTitle(_translate("GNS3VMPreferencesPageWidget", "Virtualization engine"))
        self.uiEngineDescriptionLabel.setText(_translate("GNS3VMPreferencesPageWidget", "Description"))
        self.uiGNS3VMSettingsGroupBox.setTitle(_translate("GNS3VMPreferencesPageWidget", "Settings"))
        self.uiActionCloseLabel.setText(_translate("GNS3VMPreferencesPageWidget", "Action when closing GNS3:"))
        self.uiHeadlessCheckBox.setText(_translate("GNS3VMPreferencesPageWidget", "Run the VM in headless mode"))
        self.uiWhenExitKeepRadioButton.setText(_translate("GNS3VMPreferencesPageWidget", "keep the GNS3 VM running"))
        self.uiWhenExitSuspendRadioButton.setText(_translate("GNS3VMPreferencesPageWidget", "suspend the GNS3 VM"))
        self.uiVMNameLabel.setText(_translate("GNS3VMPreferencesPageWidget", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("GNS3VMPreferencesPageWidget", "&Refresh"))
        self.uiWhenExitStopRadioButton.setText(_translate("GNS3VMPreferencesPageWidget", "stop the GNS3 VM"))
        self.uiRamLabel.setText(_translate("GNS3VMPreferencesPageWidget", "RAM:"))
        self.uiRamSpinBox.setSuffix(_translate("GNS3VMPreferencesPageWidget", " MB"))
        self.uiCpuLabel.setText(_translate("GNS3VMPreferencesPageWidget", "vCPUs:"))

