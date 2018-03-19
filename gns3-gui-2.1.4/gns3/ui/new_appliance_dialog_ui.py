# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/new_appliance_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewApplianceDialog(object):
    def setupUi(self, NewApplianceDialog):
        NewApplianceDialog.setObjectName("NewApplianceDialog")
        NewApplianceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        NewApplianceDialog.resize(483, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewApplianceDialog.sizePolicy().hasHeightForWidth())
        NewApplianceDialog.setSizePolicy(sizePolicy)
        NewApplianceDialog.setStyleSheet("QWidget{\n"
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
        NewApplianceDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewApplianceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiImportApplianceTemplatePushButton = QtWidgets.QPushButton(NewApplianceDialog)
        self.uiImportApplianceTemplatePushButton.setObjectName("uiImportApplianceTemplatePushButton")
        self.verticalLayout.addWidget(self.uiImportApplianceTemplatePushButton)
        self.label = QtWidgets.QLabel(NewApplianceDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uiAddIOSRouterRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddIOSRouterRadioButton.setObjectName("uiAddIOSRouterRadioButton")
        self.verticalLayout.addWidget(self.uiAddIOSRouterRadioButton)
        self.uiAddIOUDeviceRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddIOUDeviceRadioButton.setObjectName("uiAddIOUDeviceRadioButton")
        self.verticalLayout.addWidget(self.uiAddIOUDeviceRadioButton)
        self.uiAddQemuVMRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddQemuVMRadioButton.setObjectName("uiAddQemuVMRadioButton")
        self.verticalLayout.addWidget(self.uiAddQemuVMRadioButton)
        self.uiAddVirtualBoxVMRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddVirtualBoxVMRadioButton.setObjectName("uiAddVirtualBoxVMRadioButton")
        self.verticalLayout.addWidget(self.uiAddVirtualBoxVMRadioButton)
        self.uiAddVMwareVMRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddVMwareVMRadioButton.setObjectName("uiAddVMwareVMRadioButton")
        self.verticalLayout.addWidget(self.uiAddVMwareVMRadioButton)
        self.uiAddDockerVMRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddDockerVMRadioButton.setObjectName("uiAddDockerVMRadioButton")
        self.verticalLayout.addWidget(self.uiAddDockerVMRadioButton)
        self.uiAddVPCSRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddVPCSRadioButton.setObjectName("uiAddVPCSRadioButton")
        self.verticalLayout.addWidget(self.uiAddVPCSRadioButton)
        self.uiAddCloudRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddCloudRadioButton.setObjectName("uiAddCloudRadioButton")
        self.verticalLayout.addWidget(self.uiAddCloudRadioButton)
        self.uiAddEthernetHubRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddEthernetHubRadioButton.setObjectName("uiAddEthernetHubRadioButton")
        self.verticalLayout.addWidget(self.uiAddEthernetHubRadioButton)
        self.uiAddEthernetSwitchRadioButton = QtWidgets.QRadioButton(NewApplianceDialog)
        self.uiAddEthernetSwitchRadioButton.setObjectName("uiAddEthernetSwitchRadioButton")
        self.verticalLayout.addWidget(self.uiAddEthernetSwitchRadioButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(NewApplianceDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewApplianceDialog)
        QtCore.QMetaObject.connectSlotsByName(NewApplianceDialog)

    def retranslateUi(self, NewApplianceDialog):
        _translate = QtCore.QCoreApplication.translate
        NewApplianceDialog.setWindowTitle(_translate("NewApplianceDialog", "New appliance template"))
        self.uiImportApplianceTemplatePushButton.setText(_translate("NewApplianceDialog", "Import an appliance template file"))
        self.label.setText(_translate("NewApplianceDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:x-large; font-weight:600;\">OR</span></p></body></html>"))
        self.uiAddIOSRouterRadioButton.setText(_translate("NewApplianceDialog", "&Add an IOS router using a real IOS image (supported by Dynamips)"))
        self.uiAddIOUDeviceRadioButton.setText(_translate("NewApplianceDialog", "&Add an IOU (IOS on UNIX) device using a L3 or L2 IOU image"))
        self.uiAddQemuVMRadioButton.setText(_translate("NewApplianceDialog", "&Add a Qemu virtual machine"))
        self.uiAddVirtualBoxVMRadioButton.setText(_translate("NewApplianceDialog", "&Add a VirtualBox virtual machine"))
        self.uiAddVMwareVMRadioButton.setText(_translate("NewApplianceDialog", "&Add a VMware virtual machine"))
        self.uiAddDockerVMRadioButton.setText(_translate("NewApplianceDialog", "&Add a Docker container"))
        self.uiAddVPCSRadioButton.setText(_translate("NewApplianceDialog", "Add a VPCS"))
        self.uiAddCloudRadioButton.setText(_translate("NewApplianceDialog", "Add a cloud"))
        self.uiAddEthernetHubRadioButton.setText(_translate("NewApplianceDialog", "Add a generic ethernet hub"))
        self.uiAddEthernetSwitchRadioButton.setText(_translate("NewApplianceDialog", "Add a generic ethernet switch"))

from . import resources_rc
