# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/capture_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureDialog(object):
    def setupUi(self, CaptureDialog):
        CaptureDialog.setObjectName("CaptureDialog")
        CaptureDialog.setWindowModality(QtCore.Qt.WindowModal)
        CaptureDialog.resize(500, 147)
        CaptureDialog.setMaximumSize(QtCore.QSize(500, 147))
        CaptureDialog.setStyleSheet("QWidget{\n"
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
        CaptureDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(CaptureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLinkTypeLabel = QtWidgets.QLabel(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinkTypeLabel.sizePolicy().hasHeightForWidth())
        self.uiLinkTypeLabel.setSizePolicy(sizePolicy)
        self.uiLinkTypeLabel.setScaledContents(False)
        self.uiLinkTypeLabel.setObjectName("uiLinkTypeLabel")
        self.gridLayout.addWidget(self.uiLinkTypeLabel, 0, 0, 1, 1)
        self.uiDataLinkTypeComboBox = QtWidgets.QComboBox(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDataLinkTypeComboBox.sizePolicy().hasHeightForWidth())
        self.uiDataLinkTypeComboBox.setSizePolicy(sizePolicy)
        self.uiDataLinkTypeComboBox.setObjectName("uiDataLinkTypeComboBox")
        self.gridLayout.addWidget(self.uiDataLinkTypeComboBox, 0, 1, 1, 1)
        self.uiFileNameLabel = QtWidgets.QLabel(CaptureDialog)
        self.uiFileNameLabel.setObjectName("uiFileNameLabel")
        self.gridLayout.addWidget(self.uiFileNameLabel, 1, 0, 1, 1)
        self.uiCaptureFileNameLineEdit = QtWidgets.QLineEdit(CaptureDialog)
        self.uiCaptureFileNameLineEdit.setObjectName("uiCaptureFileNameLineEdit")
        self.gridLayout.addWidget(self.uiCaptureFileNameLineEdit, 1, 1, 1, 1)
        self.uiStartCommandCheckBox = QtWidgets.QCheckBox(CaptureDialog)
        self.uiStartCommandCheckBox.setChecked(True)
        self.uiStartCommandCheckBox.setObjectName("uiStartCommandCheckBox")
        self.gridLayout.addWidget(self.uiStartCommandCheckBox, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiButtonBox.sizePolicy().hasHeightForWidth())
        self.uiButtonBox.setSizePolicy(sizePolicy)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 244, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(CaptureDialog)
        QtCore.QMetaObject.connectSlotsByName(CaptureDialog)

    def retranslateUi(self, CaptureDialog):
        _translate = QtCore.QCoreApplication.translate
        CaptureDialog.setWindowTitle(_translate("CaptureDialog", "Packet capture"))
        self.uiLinkTypeLabel.setText(_translate("CaptureDialog", "Link type:"))
        self.uiFileNameLabel.setText(_translate("CaptureDialog", "File name:"))
        self.uiStartCommandCheckBox.setText(_translate("CaptureDialog", "Start the capture visualization program"))

from . import resources_rc
