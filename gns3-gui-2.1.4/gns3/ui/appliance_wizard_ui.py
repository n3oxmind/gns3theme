# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/appliance_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplianceWizard(object):
    def setupUi(self, ApplianceWizard):
        ApplianceWizard.setObjectName("ApplianceWizard")
        ApplianceWizard.resize(684, 458)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ApplianceWizard.sizePolicy().hasHeightForWidth())
        ApplianceWizard.setSizePolicy(sizePolicy)
        ApplianceWizard.setMaximumSize(QtCore.QSize(2000, 2000))
        ApplianceWizard.setStyleSheet("QWidget{\n"
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
        ApplianceWizard.setModal(True)
        ApplianceWizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        ApplianceWizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage)
        self.uiInfoWizardPage = QtWidgets.QWizardPage()
        self.uiInfoWizardPage.setSubTitle("")
        self.uiInfoWizardPage.setObjectName("uiInfoWizardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiInfoWizardPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiInfoTreeWidget = QtWidgets.QTreeWidget(self.uiInfoWizardPage)
        self.uiInfoTreeWidget.setAlternatingRowColors(False)
        self.uiInfoTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.uiInfoTreeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.uiInfoTreeWidget.setRootIsDecorated(False)
        self.uiInfoTreeWidget.setWordWrap(False)
        self.uiInfoTreeWidget.setHeaderHidden(True)
        self.uiInfoTreeWidget.setObjectName("uiInfoTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        self.uiInfoTreeWidget.header().setVisible(False)
        self.gridLayout_4.addWidget(self.uiInfoTreeWidget, 1, 0, 1, 1)
        self.uiDescriptionLabel = QtWidgets.QLabel(self.uiInfoWizardPage)
        self.uiDescriptionLabel.setScaledContents(False)
        self.uiDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiDescriptionLabel.setWordWrap(True)
        self.uiDescriptionLabel.setObjectName("uiDescriptionLabel")
        self.gridLayout_4.addWidget(self.uiDescriptionLabel, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiInfoWizardPage)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.uiServerWizardPage)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerTypeGroupBox.sizePolicy().hasHeightForWidth())
        self.uiServerTypeGroupBox.setSizePolicy(sizePolicy)
        self.uiServerTypeGroupBox.setMinimumSize(QtCore.QSize(0, 161))
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 17))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteRadioButton.sizePolicy().hasHeightForWidth())
        self.uiRemoteRadioButton.setSizePolicy(sizePolicy)
        self.uiRemoteRadioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout_4.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMRadioButton.sizePolicy().hasHeightForWidth())
        self.uiVMRadioButton.setSizePolicy(sizePolicy)
        self.uiVMRadioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout_4.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalRadioButton.sizePolicy().hasHeightForWidth())
        self.uiLocalRadioButton.setSizePolicy(sizePolicy)
        self.uiLocalRadioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout_4.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersGroupBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersGroupBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 1, 1, 1, 1)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.uiRemoteServersGroupBox)
        ApplianceWizard.addPage(self.uiServerWizardPage)
        self.uiCheckServerWizardPage = QtWidgets.QWizardPage()
        self.uiCheckServerWizardPage.setObjectName("uiCheckServerWizardPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiCheckServerWizardPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiCheckServerLabel = QtWidgets.QLabel(self.uiCheckServerWizardPage)
        self.uiCheckServerLabel.setWordWrap(True)
        self.uiCheckServerLabel.setObjectName("uiCheckServerLabel")
        self.verticalLayout_3.addWidget(self.uiCheckServerLabel)
        ApplianceWizard.addPage(self.uiCheckServerWizardPage)
        self.uiFilesWizardPage = QtWidgets.QWizardPage()
        self.uiFilesWizardPage.setObjectName("uiFilesWizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiFilesWizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.uiFilesWizardPage)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.uiApplianceVersionTreeWidget = QtWidgets.QTreeWidget(self.uiFilesWizardPage)
        self.uiApplianceVersionTreeWidget.setIndentation(20)
        self.uiApplianceVersionTreeWidget.setObjectName("uiApplianceVersionTreeWidget")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiApplianceVersionTreeWidget.headerItem().setFont(0, font)
        self.uiApplianceVersionTreeWidget.header().setDefaultSectionSize(120)
        self.uiApplianceVersionTreeWidget.header().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.uiApplianceVersionTreeWidget)
        self.uiExplainDownloadLabel = QtWidgets.QLabel(self.uiFilesWizardPage)
        self.uiExplainDownloadLabel.setWordWrap(True)
        self.uiExplainDownloadLabel.setObjectName("uiExplainDownloadLabel")
        self.verticalLayout.addWidget(self.uiExplainDownloadLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiImportPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiImportPushButton.setObjectName("uiImportPushButton")
        self.horizontalLayout.addWidget(self.uiImportPushButton)
        self.uiDownloadPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiDownloadPushButton.setObjectName("uiDownloadPushButton")
        self.horizontalLayout.addWidget(self.uiDownloadPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.uiCreateVersionPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiCreateVersionPushButton.setObjectName("uiCreateVersionPushButton")
        self.horizontalLayout.addWidget(self.uiCreateVersionPushButton)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout.addWidget(self.uiRefreshPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ApplianceWizard.addPage(self.uiFilesWizardPage)
        self.uiQemuWizardPage = QtWidgets.QWizardPage()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuWizardPage.sizePolicy().hasHeightForWidth())
        self.uiQemuWizardPage.setSizePolicy(sizePolicy)
        self.uiQemuWizardPage.setObjectName("uiQemuWizardPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uiQemuWizardPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiQemuListLabel = QtWidgets.QLabel(self.uiQemuWizardPage)
        self.uiQemuListLabel.setObjectName("uiQemuListLabel")
        self.horizontalLayout_2.addWidget(self.uiQemuListLabel)
        self.uiQemuListComboBox = QtWidgets.QComboBox(self.uiQemuWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName("uiQemuListComboBox")
        self.horizontalLayout_2.addWidget(self.uiQemuListComboBox)
        ApplianceWizard.addPage(self.uiQemuWizardPage)
        self.uiSummaryWizardPage = QtWidgets.QWizardPage()
        self.uiSummaryWizardPage.setObjectName("uiSummaryWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiSummaryWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiSummaryTreeWidget = QtWidgets.QTreeWidget(self.uiSummaryWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSummaryTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiSummaryTreeWidget.setSizePolicy(sizePolicy)
        self.uiSummaryTreeWidget.setAlternatingRowColors(False)
        self.uiSummaryTreeWidget.setRootIsDecorated(False)
        self.uiSummaryTreeWidget.setUniformRowHeights(False)
        self.uiSummaryTreeWidget.setItemsExpandable(False)
        self.uiSummaryTreeWidget.setAnimated(False)
        self.uiSummaryTreeWidget.setAllColumnsShowFocus(False)
        self.uiSummaryTreeWidget.setWordWrap(False)
        self.uiSummaryTreeWidget.setHeaderHidden(True)
        self.uiSummaryTreeWidget.setColumnCount(2)
        self.uiSummaryTreeWidget.setObjectName("uiSummaryTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        self.uiSummaryTreeWidget.header().setDefaultSectionSize(150)
        self.uiSummaryTreeWidget.header().setMinimumSectionSize(20)
        self.uiSummaryTreeWidget.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.uiSummaryTreeWidget, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiSummaryWizardPage)
        self.uiUsageWizardPage = QtWidgets.QWizardPage()
        self.uiUsageWizardPage.setObjectName("uiUsageWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiUsageWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiUsageTextEdit = QtWidgets.QTextEdit(self.uiUsageWizardPage)
        self.uiUsageTextEdit.setObjectName("uiUsageTextEdit")
        self.gridLayout_3.addWidget(self.uiUsageTextEdit, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiUsageWizardPage)

        self.retranslateUi(ApplianceWizard)
        QtCore.QMetaObject.connectSlotsByName(ApplianceWizard)

    def retranslateUi(self, ApplianceWizard):
        _translate = QtCore.QCoreApplication.translate
        ApplianceWizard.setWindowTitle(_translate("ApplianceWizard", "Add appliance"))
        self.uiInfoWizardPage.setTitle(_translate("ApplianceWizard", "Cisco NX-OSv"))
        self.uiInfoTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "1"))
        self.uiInfoTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "2"))
        __sortingEnabled = self.uiInfoTreeWidget.isSortingEnabled()
        self.uiInfoTreeWidget.setSortingEnabled(False)
        self.uiInfoTreeWidget.topLevelItem(0).setText(0, _translate("ApplianceWizard", "Category:"))
        self.uiInfoTreeWidget.topLevelItem(0).setText(1, _translate("ApplianceWizard", "router"))
        self.uiInfoTreeWidget.topLevelItem(1).setText(0, _translate("ApplianceWizard", "Product:"))
        self.uiInfoTreeWidget.topLevelItem(1).setText(1, _translate("ApplianceWizard", "NX-OSv"))
        self.uiInfoTreeWidget.topLevelItem(2).setText(0, _translate("ApplianceWizard", "Vendor:"))
        self.uiInfoTreeWidget.topLevelItem(2).setText(1, _translate("ApplianceWizard", "Cisco"))
        self.uiInfoTreeWidget.topLevelItem(3).setText(0, _translate("ApplianceWizard", "Status:"))
        self.uiInfoTreeWidget.topLevelItem(3).setText(1, _translate("ApplianceWizard", "stable"))
        self.uiInfoTreeWidget.topLevelItem(4).setText(0, _translate("ApplianceWizard", "Maintainer:"))
        self.uiInfoTreeWidget.topLevelItem(4).setText(1, _translate("ApplianceWizard", "The GNS3 team"))
        self.uiInfoTreeWidget.setSortingEnabled(__sortingEnabled)
        self.uiDescriptionLabel.setText(_translate("ApplianceWizard", "NX-OSv is a reference platform for an implementation of the Cisco Nexus operating system, based on the Nexus 7000-series platforms, running as a full virtual machine on a compute."))
        self.uiServerWizardPage.setTitle(_translate("ApplianceWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("ApplianceWizard", "Please choose a server type to run your new Appliance."))
        self.uiServerTypeGroupBox.setTitle(_translate("ApplianceWizard", "Server type"))
        self.label_2.setText(_translate("ApplianceWizard", "The grayed server types are not supported or configured."))
        self.uiRemoteRadioButton.setText(_translate("ApplianceWizard", "Run the appliance on a remote server"))
        self.uiVMRadioButton.setText(_translate("ApplianceWizard", "Run the appliance on the GNS3 VM (recommended)"))
        self.uiLocalRadioButton.setText(_translate("ApplianceWizard", "Run the appliance on your local computer"))
        self.uiRemoteServersGroupBox.setTitle(_translate("ApplianceWizard", "Remote server"))
        self.uiRemoteServersLabel.setText(_translate("ApplianceWizard", "Run on:"))
        self.uiCheckServerLabel.setText(_translate("ApplianceWizard", "Please wait while checking server capacities..."))
        self.uiFilesWizardPage.setTitle(_translate("ApplianceWizard", "Required files"))
        self.uiFilesWizardPage.setSubTitle(_translate("ApplianceWizard", "The following files are required to install the appliance"))
        self.label_3.setText(_translate("ApplianceWizard", "<html><head/><body><p>Click on a version to see the required files and import the file from your computer.<br/>GNS3 is looking for files in your downloads directory and in the GNS3 images directory.</p></body></html>"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "Version"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "Filename"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(2, _translate("ApplianceWizard", "Size"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(3, _translate("ApplianceWizard", "Status"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(4, _translate("ApplianceWizard", "File version"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(5, _translate("ApplianceWizard", "MD5"))
        self.uiExplainDownloadLabel.setText(_translate("ApplianceWizard", "Click on a the download button to access to a location where you can download the file."))
        self.uiImportPushButton.setText(_translate("ApplianceWizard", "&Import"))
        self.uiDownloadPushButton.setText(_translate("ApplianceWizard", "&Download"))
        self.uiCreateVersionPushButton.setText(_translate("ApplianceWizard", "Create a new version"))
        self.uiRefreshPushButton.setText(_translate("ApplianceWizard", "Refresh"))
        self.uiQemuWizardPage.setTitle(_translate("ApplianceWizard", "Qemu settings"))
        self.uiQemuWizardPage.setSubTitle(_translate("ApplianceWizard", "Please choose the qemu binary that we will use for running this appliance."))
        self.uiQemuListLabel.setText(_translate("ApplianceWizard", "Qemu binary:"))
        self.uiSummaryWizardPage.setTitle(_translate("ApplianceWizard", "Summary"))
        self.uiSummaryWizardPage.setSubTitle(_translate("ApplianceWizard", "The following settings are going to be used."))
        self.uiSummaryTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "1"))
        self.uiSummaryTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "2"))
        __sortingEnabled = self.uiSummaryTreeWidget.isSortingEnabled()
        self.uiSummaryTreeWidget.setSortingEnabled(False)
        self.uiSummaryTreeWidget.topLevelItem(0).setText(0, _translate("ApplianceWizard", "adapter_type"))
        self.uiSummaryTreeWidget.topLevelItem(0).setText(1, _translate("ApplianceWizard", "e1000"))
        self.uiSummaryTreeWidget.topLevelItem(1).setText(0, _translate("ApplianceWizard", "console_type"))
        self.uiSummaryTreeWidget.topLevelItem(1).setText(1, _translate("ApplianceWizard", "telnet"))
        self.uiSummaryTreeWidget.topLevelItem(2).setText(0, _translate("ApplianceWizard", "ram"))
        self.uiSummaryTreeWidget.topLevelItem(2).setText(1, _translate("ApplianceWizard", "3072"))
        self.uiSummaryTreeWidget.topLevelItem(3).setText(0, _translate("ApplianceWizard", "arch"))
        self.uiSummaryTreeWidget.topLevelItem(3).setText(1, _translate("ApplianceWizard", "x68_64"))
        self.uiSummaryTreeWidget.topLevelItem(4).setText(0, _translate("ApplianceWizard", "adapters"))
        self.uiSummaryTreeWidget.topLevelItem(4).setText(1, _translate("ApplianceWizard", "16"))
        self.uiSummaryTreeWidget.topLevelItem(5).setText(0, _translate("ApplianceWizard", "kernel command line"))
        self.uiSummaryTreeWidget.topLevelItem(5).setText(1, _translate("ApplianceWizard", "user=gns3"))
        self.uiSummaryTreeWidget.setSortingEnabled(__sortingEnabled)
        self.uiUsageWizardPage.setTitle(_translate("ApplianceWizard", "Usage"))
        self.uiUsageWizardPage.setSubTitle(_translate("ApplianceWizard", "Please read the following instructions in order to use your new appliance."))
        self.uiUsageTextEdit.setHtml(_translate("ApplianceWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">The default username/password is admin/admin. A default configuration is present.</span></p></body></html>"))

from . import resources_rc
