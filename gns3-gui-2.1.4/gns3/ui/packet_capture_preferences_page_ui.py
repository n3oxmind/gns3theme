# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/packet_capture_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PacketCapturePreferencesPageWidget(object):
    def setupUi(self, PacketCapturePreferencesPageWidget):
        PacketCapturePreferencesPageWidget.setObjectName("PacketCapturePreferencesPageWidget")
        PacketCapturePreferencesPageWidget.resize(446, 327)
        PacketCapturePreferencesPageWidget.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(PacketCapturePreferencesPageWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSettingsGroupBox = QtWidgets.QGroupBox(PacketCapturePreferencesPageWidget)
        self.uiSettingsGroupBox.setObjectName("uiSettingsGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.uiSettingsGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.uiCaptureAnalyzerCommandLabel = QtWidgets.QLabel(self.uiSettingsGroupBox)
        self.uiCaptureAnalyzerCommandLabel.setObjectName("uiCaptureAnalyzerCommandLabel")
        self.gridlayout.addWidget(self.uiCaptureAnalyzerCommandLabel, 5, 0, 1, 1)
        self.uiCaptureReaderCommandLabel = QtWidgets.QLabel(self.uiSettingsGroupBox)
        self.uiCaptureReaderCommandLabel.setEnabled(True)
        self.uiCaptureReaderCommandLabel.setObjectName("uiCaptureReaderCommandLabel")
        self.gridlayout.addWidget(self.uiCaptureReaderCommandLabel, 2, 0, 1, 2)
        self.uiCaptureReaderCommandLineEdit = QtWidgets.QLineEdit(self.uiSettingsGroupBox)
        self.uiCaptureReaderCommandLineEdit.setObjectName("uiCaptureReaderCommandLineEdit")
        self.gridlayout.addWidget(self.uiCaptureReaderCommandLineEdit, 3, 0, 1, 2)
        self.uiAutoStartCheckBox = QtWidgets.QCheckBox(self.uiSettingsGroupBox)
        self.uiAutoStartCheckBox.setEnabled(True)
        self.uiAutoStartCheckBox.setChecked(False)
        self.uiAutoStartCheckBox.setObjectName("uiAutoStartCheckBox")
        self.gridlayout.addWidget(self.uiAutoStartCheckBox, 4, 0, 1, 2)
        self.uiPreconfiguredCaptureReaderCommandLabel = QtWidgets.QLabel(self.uiSettingsGroupBox)
        self.uiPreconfiguredCaptureReaderCommandLabel.setObjectName("uiPreconfiguredCaptureReaderCommandLabel")
        self.gridlayout.addWidget(self.uiPreconfiguredCaptureReaderCommandLabel, 0, 0, 1, 2)
        self.uiPreconfiguredCaptureReaderCommandPushButton = QtWidgets.QPushButton(self.uiSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPreconfiguredCaptureReaderCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiPreconfiguredCaptureReaderCommandPushButton.setSizePolicy(sizePolicy)
        self.uiPreconfiguredCaptureReaderCommandPushButton.setObjectName("uiPreconfiguredCaptureReaderCommandPushButton")
        self.gridlayout.addWidget(self.uiPreconfiguredCaptureReaderCommandPushButton, 1, 1, 1, 1)
        self.uiPreconfiguredCaptureReaderCommandComboBox = QtWidgets.QComboBox(self.uiSettingsGroupBox)
        self.uiPreconfiguredCaptureReaderCommandComboBox.setObjectName("uiPreconfiguredCaptureReaderCommandComboBox")
        self.gridlayout.addWidget(self.uiPreconfiguredCaptureReaderCommandComboBox, 1, 0, 1, 1)
        self.uiCaptureAnalyzerCommandLineEdit = QtWidgets.QLineEdit(self.uiSettingsGroupBox)
        self.uiCaptureAnalyzerCommandLineEdit.setObjectName("uiCaptureAnalyzerCommandLineEdit")
        self.gridlayout.addWidget(self.uiCaptureAnalyzerCommandLineEdit, 6, 0, 1, 2)
        self.gridLayout.addWidget(self.uiSettingsGroupBox, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(PacketCapturePreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.gridLayout.addWidget(self.uiRestoreDefaultsPushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)

        self.retranslateUi(PacketCapturePreferencesPageWidget)
        QtCore.QMetaObject.connectSlotsByName(PacketCapturePreferencesPageWidget)

    def retranslateUi(self, PacketCapturePreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        PacketCapturePreferencesPageWidget.setWindowTitle(_translate("PacketCapturePreferencesPageWidget", "Packet capture"))
        self.uiSettingsGroupBox.setTitle(_translate("PacketCapturePreferencesPageWidget", "Settings"))
        self.uiCaptureAnalyzerCommandLabel.setText(_translate("PacketCapturePreferencesPageWidget", "Packet capture analyzer command:"))
        self.uiCaptureReaderCommandLabel.setText(_translate("PacketCapturePreferencesPageWidget", "Packet capture reader command:"))
        self.uiCaptureReaderCommandLineEdit.setToolTip(_translate("PacketCapturePreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%c = capture file (PCAP format)</p></body></html>"))
        self.uiAutoStartCheckBox.setText(_translate("PacketCapturePreferencesPageWidget", "Automatically start the packet capture application"))
        self.uiPreconfiguredCaptureReaderCommandLabel.setText(_translate("PacketCapturePreferencesPageWidget", "Preconfigured packet capture reader commands:"))
        self.uiPreconfiguredCaptureReaderCommandPushButton.setText(_translate("PacketCapturePreferencesPageWidget", "&Set"))
        self.uiRestoreDefaultsPushButton.setText(_translate("PacketCapturePreferencesPageWidget", "Restore defaults"))

