# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/setup_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupWizard(object):
    def setupUi(self, SetupWizard):
        SetupWizard.setObjectName("SetupWizard")
        SetupWizard.resize(1081, 534)
        SetupWizard.setModal(True)
        SetupWizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        SetupWizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMRadioButton.sizePolicy().hasHeightForWidth())
        self.uiVMRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiVMRadioButton.setFont(font)
        self.uiVMRadioButton.setChecked(True)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout_4.addWidget(self.uiVMRadioButton)
        self.label = QtWidgets.QLabel(self.uiServerWizardPage)
        self.label.setIndent(17)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerWizardPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiLocalRadioButton.setFont(font)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout_4.addWidget(self.uiLocalRadioButton)
        self.uiLocalLabel = QtWidgets.QLabel(self.uiServerWizardPage)
        self.uiLocalLabel.setIndent(17)
        self.uiLocalLabel.setObjectName("uiLocalLabel")
        self.verticalLayout_4.addWidget(self.uiLocalLabel)
        self.uiRemoteControllerRadioButton = QtWidgets.QRadioButton(self.uiServerWizardPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiRemoteControllerRadioButton.setFont(font)
        self.uiRemoteControllerRadioButton.setObjectName("uiRemoteControllerRadioButton")
        self.verticalLayout_4.addWidget(self.uiRemoteControllerRadioButton)
        self.label_2 = QtWidgets.QLabel(self.uiServerWizardPage)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(17)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.uiShowCheckBox = QtWidgets.QCheckBox(self.uiServerWizardPage)
        self.uiShowCheckBox.setChecked(True)
        self.uiShowCheckBox.setObjectName("uiShowCheckBox")
        self.verticalLayout_4.addWidget(self.uiShowCheckBox)
        SetupWizard.addPage(self.uiServerWizardPage)
        self.uiLocalServerWizardPage = QtWidgets.QWizardPage()
        self.uiLocalServerWizardPage.setObjectName("uiLocalServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiLocalServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiLocalServerWizardPage)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout_2.addWidget(self.uiLocalServerPathLabel, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiLocalServerWizardPage)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout_3.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiLocalServerWizardPage)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout_3.addWidget(self.uiLocalServerToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiLocalServerWizardPage)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout_2.addWidget(self.uiLocalServerHostLabel, 1, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiLocalServerWizardPage)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout_2.addWidget(self.uiLocalServerHostComboBox, 1, 1, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiLocalServerWizardPage)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout_2.addWidget(self.uiLocalServerPortLabel, 2, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiLocalServerWizardPage)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 3080)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout_2.addWidget(self.uiLocalServerPortSpinBox, 2, 1, 1, 1)
        SetupWizard.addPage(self.uiLocalServerWizardPage)
        self.uiLocalServerStatusWizardPage = QtWidgets.QWizardPage()
        self.uiLocalServerStatusWizardPage.setObjectName("uiLocalServerStatusWizardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiLocalServerStatusWizardPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiLocalServerTextEdit = QtWidgets.QTextEdit(self.uiLocalServerStatusWizardPage)
        self.uiLocalServerTextEdit.setReadOnly(True)
        self.uiLocalServerTextEdit.setObjectName("uiLocalServerTextEdit")
        self.gridLayout_4.addWidget(self.uiLocalServerTextEdit, 0, 0, 1, 1)
        SetupWizard.addPage(self.uiLocalServerStatusWizardPage)
        self.uiVMWizardPage = QtWidgets.QWizardPage()
        self.uiVMWizardPage.setObjectName("uiVMWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiVMWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiVirtualizationSoftwarLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVirtualizationSoftwarLabel.setObjectName("uiVirtualizationSoftwarLabel")
        self.gridLayout_3.addWidget(self.uiVirtualizationSoftwarLabel, 0, 0, 1, 1)
        self.uiVMwareBannerButton = QtWidgets.QPushButton(self.uiVMWizardPage)
        self.uiVMwareBannerButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/vmware_fusion_banner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiVMwareBannerButton.setIcon(icon)
        self.uiVMwareBannerButton.setIconSize(QtCore.QSize(300, 150))
        self.uiVMwareBannerButton.setFlat(True)
        self.uiVMwareBannerButton.setObjectName("uiVMwareBannerButton")
        self.gridLayout_3.addWidget(self.uiVMwareBannerButton, 0, 2, 4, 1)
        self.uiVmwareRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVmwareRadioButton.setChecked(True)
        self.uiVmwareRadioButton.setObjectName("uiVmwareRadioButton")
        self.gridLayout_3.addWidget(self.uiVmwareRadioButton, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(317, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.uiVirtualBoxRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVirtualBoxRadioButton.setObjectName("uiVirtualBoxRadioButton")
        self.gridLayout_3.addWidget(self.uiVirtualBoxRadioButton, 2, 0, 1, 1)
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.gridLayout_3.addWidget(self.uiVMNameLabel, 5, 0, 1, 1)
        self.uiCPULabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiCPULabel.setObjectName("uiCPULabel")
        self.gridLayout_3.addWidget(self.uiCPULabel, 7, 0, 1, 1)
        self.uiRAMLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiRAMLabel.setObjectName("uiRAMLabel")
        self.gridLayout_3.addWidget(self.uiRAMLabel, 9, 0, 1, 1)
        self.uiGNS3VMDownloadLinkUrlLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiGNS3VMDownloadLinkUrlLabel.setOpenExternalLinks(True)
        self.uiGNS3VMDownloadLinkUrlLabel.setObjectName("uiGNS3VMDownloadLinkUrlLabel")
        self.gridLayout_3.addWidget(self.uiGNS3VMDownloadLinkUrlLabel, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiVMWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.horizontalLayout.addWidget(self.uiVMListComboBox)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiVMWizardPage)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout.addWidget(self.uiRefreshPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        self.uiCPUSpinBox = QtWidgets.QSpinBox(self.uiVMWizardPage)
        self.uiCPUSpinBox.setMinimum(1)
        self.uiCPUSpinBox.setMaximum(128)
        self.uiCPUSpinBox.setProperty("value", 1)
        self.uiCPUSpinBox.setObjectName("uiCPUSpinBox")
        self.gridLayout_3.addWidget(self.uiCPUSpinBox, 8, 0, 1, 3)
        self.uiRAMSpinBox = QtWidgets.QSpinBox(self.uiVMWizardPage)
        self.uiRAMSpinBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRAMSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRAMSpinBox.setSizePolicy(sizePolicy)
        self.uiRAMSpinBox.setMinimum(512)
        self.uiRAMSpinBox.setMaximum(1000000000)
        self.uiRAMSpinBox.setSingleStep(512)
        self.uiRAMSpinBox.setProperty("value", 2048)
        self.uiRAMSpinBox.setObjectName("uiRAMSpinBox")
        self.gridLayout_3.addWidget(self.uiRAMSpinBox, 10, 0, 1, 3)
        SetupWizard.addPage(self.uiVMWizardPage)
        self.uiRemoteControllerWizardPage = QtWidgets.QWizardPage()
        self.uiRemoteControllerWizardPage.setObjectName("uiRemoteControllerWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiRemoteControllerWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.uiRemoteControllerWizardPage)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.uiRemoteControllerWizardPage)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.uiRemoteMainServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteControllerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteMainServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteMainServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteMainServerPortSpinBox.setMaximum(65535)
        self.uiRemoteMainServerPortSpinBox.setProperty("value", 3080)
        self.uiRemoteMainServerPortSpinBox.setObjectName("uiRemoteMainServerPortSpinBox")
        self.gridLayout.addWidget(self.uiRemoteMainServerPortSpinBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.uiRemoteControllerWizardPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.uiRemoteMainServerHostLineEdit = QtWidgets.QLineEdit(self.uiRemoteControllerWizardPage)
        self.uiRemoteMainServerHostLineEdit.setObjectName("uiRemoteMainServerHostLineEdit")
        self.gridLayout.addWidget(self.uiRemoteMainServerHostLineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.uiRemoteControllerWizardPage)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.uiRemoteMainServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteControllerWizardPage)
        self.uiRemoteMainServerUserLineEdit.setObjectName("uiRemoteMainServerUserLineEdit")
        self.gridLayout.addWidget(self.uiRemoteMainServerUserLineEdit, 3, 1, 1, 1)
        self.uiRemoteMainServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiRemoteControllerWizardPage)
        self.uiRemoteMainServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiRemoteMainServerPasswordLineEdit.setObjectName("uiRemoteMainServerPasswordLineEdit")
        self.gridLayout.addWidget(self.uiRemoteMainServerPasswordLineEdit, 4, 1, 1, 1)
        self.uiRemoteMainServerAuthCheckBox = QtWidgets.QCheckBox(self.uiRemoteControllerWizardPage)
        self.uiRemoteMainServerAuthCheckBox.setObjectName("uiRemoteMainServerAuthCheckBox")
        self.gridLayout.addWidget(self.uiRemoteMainServerAuthCheckBox, 2, 0, 1, 2)
        SetupWizard.addPage(self.uiRemoteControllerWizardPage)
        self.uiSummaryWizardPage = QtWidgets.QWizardPage()
        self.uiSummaryWizardPage.setObjectName("uiSummaryWizardPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiSummaryWizardPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiSummaryTreeWidget = QtWidgets.QTreeWidget(self.uiSummaryWizardPage)
        self.uiSummaryTreeWidget.setRootIsDecorated(False)
        self.uiSummaryTreeWidget.setObjectName("uiSummaryTreeWidget")
        self.uiSummaryTreeWidget.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.uiSummaryTreeWidget)
        SetupWizard.addPage(self.uiSummaryWizardPage)

        self.retranslateUi(SetupWizard)
        QtCore.QMetaObject.connectSlotsByName(SetupWizard)

    def retranslateUi(self, SetupWizard):
        _translate = QtCore.QCoreApplication.translate
        SetupWizard.setWindowTitle(_translate("SetupWizard", "Setup Wizard"))
        self.uiServerWizardPage.setTitle(_translate("SetupWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("SetupWizard", "Please choose how would like to run your GNS3 network simulations. The GNS3 VM option is strongly recommended on Windows and Mac OS X."))
        self.uiVMRadioButton.setToolTip(_translate("SetupWizard", "Dynamips, IOU, VPCS and Qemu will use this virtual machine."))
        self.uiVMRadioButton.setText(_translate("SetupWizard", "Run appliances in a virtual machine"))
        self.label.setText(_translate("SetupWizard", "Requires to download and install the GNS3 VM (available for free) "))
        self.uiLocalRadioButton.setToolTip(_translate("SetupWizard", "Everything that is supported by your system will run on your computer."))
        self.uiLocalRadioButton.setText(_translate("SetupWizard", "Run appliances on my local computer"))
        self.uiLocalLabel.setText(_translate("SetupWizard", "A limited number of appliances like the Cisco IOS routers <= C7200 can be run"))
        self.uiRemoteControllerRadioButton.setText(_translate("SetupWizard", "Run appliances on a remote server (advanced usage)"))
        self.label_2.setText(_translate("SetupWizard", "The server will be on a remote computer and can be shared with multiple users"))
        self.uiShowCheckBox.setText(_translate("SetupWizard", "Don\'t show this again"))
        self.uiLocalServerWizardPage.setTitle(_translate("SetupWizard", "Local server configuration"))
        self.uiLocalServerWizardPage.setSubTitle(_translate("SetupWizard", "Please configure the following GNS3 local server settings"))
        self.uiLocalServerPathLabel.setText(_translate("SetupWizard", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("SetupWizard", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("SetupWizard", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("SetupWizard", "Port:"))
        self.uiLocalServerStatusWizardPage.setTitle(_translate("SetupWizard", "Local server status"))
        self.uiLocalServerStatusWizardPage.setSubTitle(_translate("SetupWizard", "Validation of the configuration for the local server"))
        self.uiVMWizardPage.setTitle(_translate("SetupWizard", "GNS3 VM"))
        self.uiVMWizardPage.setSubTitle(_translate("SetupWizard", "In order to run the GNS3 VM you must first have VMware or VirtualBox installed and the GNS3 VM.ova imported with one of these software."))
        self.uiVirtualizationSoftwarLabel.setText(_translate("SetupWizard", "Virtualization software:"))
        self.uiVmwareRadioButton.setToolTip(_translate("SetupWizard", "VMware is recommended to run Qemu based appliances (required for KVM)."))
        self.uiVmwareRadioButton.setText(_translate("SetupWizard", "VMware (recommended)"))
        self.uiVirtualBoxRadioButton.setToolTip(_translate("SetupWizard", "Use VirtualBox if you intend to only use Dynamips, IOU or VPCS."))
        self.uiVirtualBoxRadioButton.setText(_translate("SetupWizard", "VirtualBox"))
        self.uiVMNameLabel.setText(_translate("SetupWizard", "VM name:"))
        self.uiCPULabel.setText(_translate("SetupWizard", "vCPU cores:"))
        self.uiRAMLabel.setText(_translate("SetupWizard", "RAM size:"))
        self.uiGNS3VMDownloadLinkUrlLabel.setText(_translate("SetupWizard", "<html><head/><body><p>The GNS3 VM can be <a href=\"https://github.com/GNS3/gns3-gui/releases/download/v1.4.1/GNS3.VM.VMware.Workstation.1.4.1.zip\"><span style=\" text-decoration: underline; color:#0000ff;\">downloaded here</span></a></p></body></html>"))
        self.uiRefreshPushButton.setText(_translate("SetupWizard", "&Refresh"))
        self.uiRAMSpinBox.setSuffix(_translate("SetupWizard", " MB"))
        self.uiRemoteControllerWizardPage.setTitle(_translate("SetupWizard", "Remote server"))
        self.uiRemoteControllerWizardPage.setSubTitle(_translate("SetupWizard", "Everything will run on a remote server. No data will be saved on this computer."))
        self.label_5.setText(_translate("SetupWizard", "User:"))
        self.label_6.setText(_translate("SetupWizard", "Password:"))
        self.uiRemoteMainServerPortSpinBox.setSuffix(_translate("SetupWizard", " TCP"))
        self.label_3.setText(_translate("SetupWizard", "Host:"))
        self.label_4.setText(_translate("SetupWizard", "Port:"))
        self.uiRemoteMainServerAuthCheckBox.setText(_translate("SetupWizard", "Enable authentication"))
        self.uiSummaryWizardPage.setTitle(_translate("SetupWizard", "Summary"))
        self.uiSummaryWizardPage.setSubTitle(_translate("SetupWizard", "The server type has been configured, please see the summary of the settings below"))
        self.uiSummaryTreeWidget.headerItem().setText(0, _translate("SetupWizard", "1"))
        self.uiSummaryTreeWidget.headerItem().setText(1, _translate("SetupWizard", "2"))
from . import resources_rc