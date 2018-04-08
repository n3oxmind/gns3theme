# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/setup_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupWizard(object):
    def setupUi(self, SetupWizard):
        SetupWizard.setObjectName("SetupWizard")
        SetupWizard.resize(754, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetupWizard.sizePolicy().hasHeightForWidth())
        SetupWizard.setSizePolicy(sizePolicy)
        SetupWizard.setMaximumSize(QtCore.QSize(775, 563))
        SetupWizard.setStyleSheet("QWidget{\n"
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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.uiLocalServerStatusWizardPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.uiLocalServerStatusLabel = QtWidgets.QLabel(self.uiLocalServerStatusWizardPage)
        self.uiLocalServerStatusLabel.setWordWrap(True)
        self.uiLocalServerStatusLabel.setObjectName("uiLocalServerStatusLabel")
        self.verticalLayout_7.addWidget(self.uiLocalServerStatusLabel)
        SetupWizard.addPage(self.uiLocalServerStatusWizardPage)
        self.uiVMWizardPage = QtWidgets.QWizardPage()
        self.uiVMWizardPage.setObjectName("uiVMWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiVMWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiVirtualizationSoftwarLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVirtualizationSoftwarLabel.setObjectName("uiVirtualizationSoftwarLabel")
        self.verticalLayout.addWidget(self.uiVirtualizationSoftwarLabel)
        self.uiVmwareRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVmwareRadioButton.setChecked(True)
        self.uiVmwareRadioButton.setObjectName("uiVmwareRadioButton")
        self.verticalLayout.addWidget(self.uiVmwareRadioButton)
        self.uiVirtualBoxRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVirtualBoxRadioButton.setObjectName("uiVirtualBoxRadioButton")
        self.verticalLayout.addWidget(self.uiVirtualBoxRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.uiVMwareBannerButton = QtWidgets.QPushButton(self.uiVMWizardPage)
        self.uiVMwareBannerButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/vmware_fusion_banner.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.uiVMwareBannerButton.setIcon(icon)
        self.uiVMwareBannerButton.setIconSize(QtCore.QSize(454, 150))
        self.uiVMwareBannerButton.setFlat(True)
        self.uiVMwareBannerButton.setObjectName("uiVMwareBannerButton")
        self.horizontalLayout_2.addWidget(self.uiVMwareBannerButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.uiGNS3VMDownloadLinkUrlLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiGNS3VMDownloadLinkUrlLabel.setOpenExternalLinks(True)
        self.uiGNS3VMDownloadLinkUrlLabel.setObjectName("uiGNS3VMDownloadLinkUrlLabel")
        self.verticalLayout_2.addWidget(self.uiGNS3VMDownloadLinkUrlLabel)
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.verticalLayout_2.addWidget(self.uiVMNameLabel)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uiCPULabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiCPULabel.setObjectName("uiCPULabel")
        self.verticalLayout_2.addWidget(self.uiCPULabel)
        self.uiCPUSpinBox = QtWidgets.QSpinBox(self.uiVMWizardPage)
        self.uiCPUSpinBox.setMinimum(1)
        self.uiCPUSpinBox.setMaximum(128)
        self.uiCPUSpinBox.setProperty("value", 1)
        self.uiCPUSpinBox.setObjectName("uiCPUSpinBox")
        self.verticalLayout_2.addWidget(self.uiCPUSpinBox)
        self.uiRAMLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiRAMLabel.setObjectName("uiRAMLabel")
        self.verticalLayout_2.addWidget(self.uiRAMLabel)
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
        self.verticalLayout_2.addWidget(self.uiRAMSpinBox)
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
        self.uiServerWizardPage.setSubTitle(_translate("SetupWizard", "Please choose a server type to run your GNS3 network simulations. The GNS3 VM is strongly recommended on Windows and Mac OS X."))
        self.uiVMRadioButton.setToolTip(_translate("SetupWizard", "Dynamips, IOU, VPCS and Qemu will use this virtual machine."))
        self.uiVMRadioButton.setText(_translate("SetupWizard", "Run modern IOS (IOSv or IOU), ASA and appliances from non Cisco manufacturers. "))
        self.label.setText(_translate("SetupWizard", "This will require an additional VM (the GNS3 VM is available for free) ."))
        self.uiLocalRadioButton.setToolTip(_translate("SetupWizard", "Eveything that is supported by your system will run on your computer."))
        self.uiLocalRadioButton.setText(_translate("SetupWizard", "Run only legacy IOS on my computer"))
        self.uiLocalLabel.setText(_translate("SetupWizard", "Requires IOS images <= C7200"))
        self.uiRemoteControllerRadioButton.setText(_translate("SetupWizard", "Run everything on a remote server (advanced usage)"))
        self.label_2.setText(_translate("SetupWizard", "The server will be on a remote computer and can be shared with multiple users."))
        self.uiShowCheckBox.setText(_translate("SetupWizard", "Don\'t show this again"))
        self.uiLocalServerWizardPage.setTitle(_translate("SetupWizard", "Local server configuration"))
        self.uiLocalServerWizardPage.setSubTitle(_translate("SetupWizard", "Please configure the following GNS3 local server settings"))
        self.uiLocalServerPathLabel.setText(_translate("SetupWizard", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("SetupWizard", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("SetupWizard", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("SetupWizard", "Port:"))
        self.uiLocalServerStatusWizardPage.setTitle(_translate("SetupWizard", "Local server status"))
        self.uiLocalServerStatusWizardPage.setSubTitle(_translate("SetupWizard", "Validation of the configuration of the local server"))
        self.uiLocalServerStatusLabel.setText(_translate("SetupWizard", "Local server status"))
        self.uiVMWizardPage.setTitle(_translate("SetupWizard", "GNS3 VM"))
        self.uiVMWizardPage.setSubTitle(_translate("SetupWizard", "In order to run the GNS3 VM you must first have VMware or VirtualBox installed and the GNS3 VM.ova imported with one of these software."))
        self.uiVirtualizationSoftwarLabel.setText(_translate("SetupWizard", "Virtualization software:"))
        self.uiVmwareRadioButton.setToolTip(_translate("SetupWizard", "VMware is recommended to run Qemu based appliances (required for KVM)."))
        self.uiVmwareRadioButton.setText(_translate("SetupWizard", "VMware (recommended)"))
        self.uiVirtualBoxRadioButton.setToolTip(_translate("SetupWizard", "Use VirtualBox if you intend to only use Dynamips, IOU or VPCS."))
        self.uiVirtualBoxRadioButton.setText(_translate("SetupWizard", "VirtualBox"))
        self.uiGNS3VMDownloadLinkUrlLabel.setText(_translate("SetupWizard", "<html><head/><body><p>The GNS3 VM can be <a href=\"https://github.com/GNS3/gns3-gui/releases/download/v1.4.1/GNS3.VM.VMware.Workstation.1.4.1.zip\"><span style=\" text-decoration: underline; color:#0000ff;\">downloaded here</span></a>. Import the VM in your virtualization software and hit refresh.</p></body></html>"))
        self.uiVMNameLabel.setText(_translate("SetupWizard", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("SetupWizard", "&Refresh"))
        self.uiCPULabel.setText(_translate("SetupWizard", "vCPU cores:"))
        self.uiRAMLabel.setText(_translate("SetupWizard", "RAM size:"))
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
