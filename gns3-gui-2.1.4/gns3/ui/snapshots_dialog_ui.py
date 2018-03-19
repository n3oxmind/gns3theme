# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/snapshots_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SnapshotsDialog(object):
    def setupUi(self, SnapshotsDialog):
        SnapshotsDialog.setObjectName("SnapshotsDialog")
        SnapshotsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SnapshotsDialog.resize(496, 288)
        SnapshotsDialog.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(SnapshotsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSnapshotsList = QtWidgets.QListWidget(SnapshotsDialog)
        self.uiSnapshotsList.setObjectName("uiSnapshotsList")
        self.gridLayout.addWidget(self.uiSnapshotsList, 0, 0, 1, 4)
        self.uiCreatePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiCreatePushButton.setObjectName("uiCreatePushButton")
        self.gridLayout.addWidget(self.uiCreatePushButton, 1, 0, 1, 1)
        self.uiRestorePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiRestorePushButton.setEnabled(False)
        self.uiRestorePushButton.setObjectName("uiRestorePushButton")
        self.gridLayout.addWidget(self.uiRestorePushButton, 1, 2, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SnapshotsDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 3, 1, 1)
        self.uiDeletePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.gridLayout.addWidget(self.uiDeletePushButton, 1, 1, 1, 1)

        self.retranslateUi(SnapshotsDialog)
        self.uiButtonBox.accepted.connect(SnapshotsDialog.accept)
        self.uiButtonBox.rejected.connect(SnapshotsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SnapshotsDialog)

    def retranslateUi(self, SnapshotsDialog):
        _translate = QtCore.QCoreApplication.translate
        SnapshotsDialog.setWindowTitle(_translate("SnapshotsDialog", "Snapshots"))
        self.uiCreatePushButton.setText(_translate("SnapshotsDialog", "&Create"))
        self.uiRestorePushButton.setText(_translate("SnapshotsDialog", "&Restore"))
        self.uiDeletePushButton.setText(_translate("SnapshotsDialog", "&Delete"))

