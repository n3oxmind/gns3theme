# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/edit_compute_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditComputeDialog(object):
    def setupUi(self, EditComputeDialog):
        EditComputeDialog.setObjectName("EditComputeDialog")
        EditComputeDialog.setWindowModality(QtCore.Qt.WindowModal)
        EditComputeDialog.resize(579, 376)
        EditComputeDialog.setStyleSheet("QWidget{\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(EditComputeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(EditComputeDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiServerNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiServerNameLineEdit.setObjectName("uiServerNameLineEdit")
        self.gridLayout.addWidget(self.uiServerNameLineEdit, 0, 1, 1, 1)
        self.uiServerPortSpinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiServerPortSpinBox.setSuffix(" TCP")
        self.uiServerPortSpinBox.setMaximum(65535)
        self.uiServerPortSpinBox.setProperty("value", 3080)
        self.uiServerPortSpinBox.setObjectName("uiServerPortSpinBox")
        self.gridLayout.addWidget(self.uiServerPortSpinBox, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiServerHostLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiServerHostLineEdit.setObjectName("uiServerHostLineEdit")
        self.gridLayout.addWidget(self.uiServerHostLineEdit, 1, 1, 1, 2)
        self.uiServerHostLabel = QtWidgets.QLabel(self.groupBox)
        self.uiServerHostLabel.setObjectName("uiServerHostLabel")
        self.gridLayout.addWidget(self.uiServerHostLabel, 1, 0, 1, 1)
        self.uiServerPortLabel = QtWidgets.QLabel(self.groupBox)
        self.uiServerPortLabel.setObjectName("uiServerPortLabel")
        self.gridLayout.addWidget(self.uiServerPortLabel, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.uiEnableAuthenticationCheckBox = QtWidgets.QGroupBox(EditComputeDialog)
        self.uiEnableAuthenticationCheckBox.setCheckable(True)
        self.uiEnableAuthenticationCheckBox.setObjectName("uiEnableAuthenticationCheckBox")
        self.formLayout = QtWidgets.QFormLayout(self.uiEnableAuthenticationCheckBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.uiServerUserLabel = QtWidgets.QLabel(self.uiEnableAuthenticationCheckBox)
        self.uiServerUserLabel.setObjectName("uiServerUserLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiServerUserLabel)
        self.uiServerUserLineEdit = QtWidgets.QLineEdit(self.uiEnableAuthenticationCheckBox)
        self.uiServerUserLineEdit.setEnabled(True)
        self.uiServerUserLineEdit.setToolTip("")
        self.uiServerUserLineEdit.setObjectName("uiServerUserLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiServerUserLineEdit)
        self.uiServerPasswordLabel = QtWidgets.QLabel(self.uiEnableAuthenticationCheckBox)
        self.uiServerPasswordLabel.setObjectName("uiServerPasswordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiServerPasswordLabel)
        self.uiServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiEnableAuthenticationCheckBox)
        self.uiServerPasswordLineEdit.setEnabled(True)
        self.uiServerPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.uiServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiServerPasswordLineEdit.setObjectName("uiServerPasswordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiServerPasswordLineEdit)
        self.verticalLayout.addWidget(self.uiEnableAuthenticationCheckBox)
        self.uiWarningLabel = QtWidgets.QLabel(EditComputeDialog)
        self.uiWarningLabel.setWordWrap(True)
        self.uiWarningLabel.setObjectName("uiWarningLabel")
        self.verticalLayout.addWidget(self.uiWarningLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditComputeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditComputeDialog)
        self.buttonBox.accepted.connect(EditComputeDialog.accept)
        self.buttonBox.rejected.connect(EditComputeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditComputeDialog)
        EditComputeDialog.setTabOrder(self.uiServerNameLineEdit, self.uiServerHostLineEdit)
        EditComputeDialog.setTabOrder(self.uiServerHostLineEdit, self.uiServerPortSpinBox)
        EditComputeDialog.setTabOrder(self.uiServerPortSpinBox, self.uiEnableAuthenticationCheckBox)
        EditComputeDialog.setTabOrder(self.uiEnableAuthenticationCheckBox, self.uiServerUserLineEdit)
        EditComputeDialog.setTabOrder(self.uiServerUserLineEdit, self.uiServerPasswordLineEdit)

    def retranslateUi(self, EditComputeDialog):
        _translate = QtCore.QCoreApplication.translate
        EditComputeDialog.setWindowTitle(_translate("EditComputeDialog", "Edit server settings"))
        self.groupBox.setTitle(_translate("EditComputeDialog", "Server settings"))
        self.label.setText(_translate("EditComputeDialog", "Name:"))
        self.uiServerHostLineEdit.setText(_translate("EditComputeDialog", "192.168.56.101"))
        self.uiServerHostLabel.setText(_translate("EditComputeDialog", "Host:"))
        self.uiServerPortLabel.setText(_translate("EditComputeDialog", "Port:"))
        self.uiEnableAuthenticationCheckBox.setTitle(_translate("EditComputeDialog", "Enable authentication"))
        self.uiServerUserLabel.setText(_translate("EditComputeDialog", "User:"))
        self.uiServerPasswordLabel.setText(_translate("EditComputeDialog", "Password:"))
        self.uiWarningLabel.setText(_translate("EditComputeDialog", "<html><head/><body><p><span style=\" font-weight:600;\">WARNING</span>: Changing a server with authentication enabled will reset the password.</p></body></html>"))

