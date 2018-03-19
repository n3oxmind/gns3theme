# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectDialog(object):
    def setupUi(self, ProjectDialog):
        ProjectDialog.setObjectName("ProjectDialog")
        ProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ProjectDialog.resize(520, 313)
        ProjectDialog.setStyleSheet("QWidget{\n"
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
        ProjectDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiProjectTabWidget = QtWidgets.QTabWidget(ProjectDialog)
        self.uiProjectTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.uiProjectTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.uiProjectTabWidget.setObjectName("uiProjectTabWidget")
        self.uiNewProjectTab = QtWidgets.QWidget()
        self.uiNewProjectTab.setObjectName("uiNewProjectTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiNewProjectTab)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.uiNewProjectTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiLocationLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiLocationLineEdit.setObjectName("uiLocationLineEdit")
        self.horizontalLayout_3.addWidget(self.uiLocationLineEdit)
        self.uiLocationBrowserToolButton = QtWidgets.QToolButton(self.groupBox)
        self.uiLocationBrowserToolButton.setObjectName("uiLocationBrowserToolButton")
        self.horizontalLayout_3.addWidget(self.uiLocationBrowserToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.uiNameLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNameLabel.sizePolicy().hasHeightForWidth())
        self.uiNameLabel.setSizePolicy(sizePolicy)
        self.uiNameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiLocationLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocationLabel.sizePolicy().hasHeightForWidth())
        self.uiLocationLabel.setSizePolicy(sizePolicy)
        self.uiLocationLabel.setObjectName("uiLocationLabel")
        self.gridLayout.addWidget(self.uiLocationLabel, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.uiOpenProjectGroupBox = QtWidgets.QGroupBox(self.uiNewProjectTab)
        self.uiOpenProjectGroupBox.setObjectName("uiOpenProjectGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiOpenProjectGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiOpenProjectPushButton = QtWidgets.QPushButton(self.uiOpenProjectGroupBox)
        self.uiOpenProjectPushButton.setObjectName("uiOpenProjectPushButton")
        self.horizontalLayout_2.addWidget(self.uiOpenProjectPushButton)
        self.uiRecentProjectsPushButton = QtWidgets.QPushButton(self.uiOpenProjectGroupBox)
        self.uiRecentProjectsPushButton.setObjectName("uiRecentProjectsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRecentProjectsPushButton)
        spacerItem = QtWidgets.QSpacerItem(239, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiOpenProjectGroupBox)
        self.uiProjectTabWidget.addTab(self.uiNewProjectTab, "")
        self.uiProjectsLibraryTab = QtWidgets.QWidget()
        self.uiProjectsLibraryTab.setObjectName("uiProjectsLibraryTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiProjectsLibraryTab)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiProjectsTreeWidget = QtWidgets.QTreeWidget(self.uiProjectsLibraryTab)
        self.uiProjectsTreeWidget.setAlternatingRowColors(True)
        self.uiProjectsTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiProjectsTreeWidget.setObjectName("uiProjectsTreeWidget")
        self.uiProjectsTreeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.uiProjectsTreeWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiDeleteProjectButton = QtWidgets.QPushButton(self.uiProjectsLibraryTab)
        self.uiDeleteProjectButton.setObjectName("uiDeleteProjectButton")
        self.horizontalLayout_4.addWidget(self.uiDeleteProjectButton)
        self.uiDuplicateProjectPushButton = QtWidgets.QPushButton(self.uiProjectsLibraryTab)
        self.uiDuplicateProjectPushButton.setObjectName("uiDuplicateProjectPushButton")
        self.horizontalLayout_4.addWidget(self.uiDuplicateProjectPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.uiRefreshProjectsPushButton = QtWidgets.QPushButton(self.uiProjectsLibraryTab)
        self.uiRefreshProjectsPushButton.setObjectName("uiRefreshProjectsPushButton")
        self.horizontalLayout_4.addWidget(self.uiRefreshProjectsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.uiProjectTabWidget.addTab(self.uiProjectsLibraryTab, "")
        self.verticalLayout.addWidget(self.uiProjectTabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiSettingsPushButton = QtWidgets.QPushButton(ProjectDialog)
        self.uiSettingsPushButton.setObjectName("uiSettingsPushButton")
        self.horizontalLayout.addWidget(self.uiSettingsPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(ProjectDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ProjectDialog)
        self.uiProjectTabWidget.setCurrentIndex(0)
        self.uiButtonBox.accepted.connect(ProjectDialog.accept)
        self.uiButtonBox.rejected.connect(ProjectDialog.reject)
        self.uiNameLineEdit.returnPressed.connect(ProjectDialog.accept)
        self.uiLocationLineEdit.returnPressed.connect(ProjectDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ProjectDialog)

    def retranslateUi(self, ProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ProjectDialog.setWindowTitle(_translate("ProjectDialog", "Project"))
        self.groupBox.setTitle(_translate("ProjectDialog", "New project"))
        self.uiLocationBrowserToolButton.setText(_translate("ProjectDialog", "Browse..."))
        self.uiNameLabel.setText(_translate("ProjectDialog", "Name:"))
        self.uiLocationLabel.setText(_translate("ProjectDialog", "Location:"))
        self.uiOpenProjectGroupBox.setTitle(_translate("ProjectDialog", "Open project"))
        self.uiOpenProjectPushButton.setText(_translate("ProjectDialog", "&Open a project from disk"))
        self.uiRecentProjectsPushButton.setText(_translate("ProjectDialog", "&Recent projects..."))
        self.uiProjectTabWidget.setTabText(self.uiProjectTabWidget.indexOf(self.uiNewProjectTab), _translate("ProjectDialog", "New project"))
        self.uiProjectsTreeWidget.setSortingEnabled(True)
        self.uiProjectsTreeWidget.headerItem().setText(0, _translate("ProjectDialog", "Name"))
        self.uiProjectsTreeWidget.headerItem().setText(1, _translate("ProjectDialog", "Status"))
        self.uiProjectsTreeWidget.headerItem().setText(2, _translate("ProjectDialog", "Path"))
        self.uiDeleteProjectButton.setText(_translate("ProjectDialog", "Delete"))
        self.uiDuplicateProjectPushButton.setText(_translate("ProjectDialog", "Duplicate"))
        self.uiRefreshProjectsPushButton.setText(_translate("ProjectDialog", "Refresh list"))
        self.uiProjectTabWidget.setTabText(self.uiProjectTabWidget.indexOf(self.uiProjectsLibraryTab), _translate("ProjectDialog", "Projects library"))
        self.uiSettingsPushButton.setText(_translate("ProjectDialog", "Settings"))

