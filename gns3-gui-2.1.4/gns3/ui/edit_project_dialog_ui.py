# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/edit_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditProjectDialog(object):
    def setupUi(self, EditProjectDialog):
        EditProjectDialog.setObjectName("EditProjectDialog")
        EditProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditProjectDialog.resize(549, 287)
        EditProjectDialog.setStyleSheet("QWidget{\n"
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
        EditProjectDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(EditProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiProjectNameLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiProjectNameLabel.setObjectName("uiProjectNameLabel")
        self.gridLayout.addWidget(self.uiProjectNameLabel, 0, 0, 1, 1)
        self.uiProjectNameLineEdit = QtWidgets.QLineEdit(EditProjectDialog)
        self.uiProjectNameLineEdit.setObjectName("uiProjectNameLineEdit")
        self.gridLayout.addWidget(self.uiProjectNameLineEdit, 0, 1, 1, 1)
        self.uiProjectAutoCloseCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoCloseCheckBox.setObjectName("uiProjectAutoCloseCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoCloseCheckBox, 5, 0, 1, 3)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(EditProjectDialog)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.gridLayout.addWidget(self.uiSceneHeightSpinBox, 2, 1, 1, 1)
        self.uiProjectAutoOpenCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoOpenCheckBox.setObjectName("uiProjectAutoOpenCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoOpenCheckBox, 3, 0, 1, 3)
        self.uiProjectAutoStartCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoStartCheckBox.setObjectName("uiProjectAutoStartCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoStartCheckBox, 4, 0, 1, 3)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(EditProjectDialog)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.gridLayout.addWidget(self.uiSceneWidthSpinBox, 1, 1, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(EditProjectDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 6, 0, 1, 3)
        self.uiSceneWidthLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.gridLayout.addWidget(self.uiSceneWidthLabel, 1, 0, 1, 1)
        self.uiSceneHeightLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.gridLayout.addWidget(self.uiSceneHeightLabel, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)

        self.retranslateUi(EditProjectDialog)
        self.uiButtonBox.accepted.connect(EditProjectDialog.accept)
        self.uiButtonBox.rejected.connect(EditProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditProjectDialog)

    def retranslateUi(self, EditProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        EditProjectDialog.setWindowTitle(_translate("EditProjectDialog", "Edit project"))
        self.uiProjectNameLabel.setText(_translate("EditProjectDialog", "Project Name:"))
        self.uiProjectAutoCloseCheckBox.setText(_translate("EditProjectDialog", "Leave this project running in the background when closing GNS3"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiProjectAutoOpenCheckBox.setText(_translate("EditProjectDialog", "Open this project in the background when GNS3 server starts"))
        self.uiProjectAutoStartCheckBox.setText(_translate("EditProjectDialog", "Start all nodes when this project is opened"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneWidthLabel.setText(_translate("EditProjectDialog", "Scene width:"))
        self.uiSceneHeightLabel.setText(_translate("EditProjectDialog", "Scene height:"))

