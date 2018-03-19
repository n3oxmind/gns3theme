# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/style_editor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StyleEditorDialog(object):
    def setupUi(self, StyleEditorDialog):
        StyleEditorDialog.setObjectName("StyleEditorDialog")
        StyleEditorDialog.resize(328, 288)
        StyleEditorDialog.setStyleSheet("QWidget{\n"
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
        StyleEditorDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(StyleEditorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiStyleSettingsGroupBox = QtWidgets.QGroupBox(StyleEditorDialog)
        self.uiStyleSettingsGroupBox.setObjectName("uiStyleSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiStyleSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiColorLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiColorLabel.setObjectName("uiColorLabel")
        self.gridLayout.addWidget(self.uiColorLabel, 0, 0, 1, 1)
        self.uiColorPushButton = QtWidgets.QPushButton(self.uiStyleSettingsGroupBox)
        self.uiColorPushButton.setText("")
        self.uiColorPushButton.setObjectName("uiColorPushButton")
        self.gridLayout.addWidget(self.uiColorPushButton, 0, 1, 1, 1)
        self.uiBorderColorLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderColorLabel.setObjectName("uiBorderColorLabel")
        self.gridLayout.addWidget(self.uiBorderColorLabel, 1, 0, 1, 1)
        self.uiBorderColorPushButton = QtWidgets.QPushButton(self.uiStyleSettingsGroupBox)
        self.uiBorderColorPushButton.setText("")
        self.uiBorderColorPushButton.setObjectName("uiBorderColorPushButton")
        self.gridLayout.addWidget(self.uiBorderColorPushButton, 1, 1, 1, 1)
        self.uiBorderWidthLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderWidthLabel.setObjectName("uiBorderWidthLabel")
        self.gridLayout.addWidget(self.uiBorderWidthLabel, 2, 0, 1, 1)
        self.uiBorderWidthSpinBox = QtWidgets.QSpinBox(self.uiStyleSettingsGroupBox)
        self.uiBorderWidthSpinBox.setMinimum(1)
        self.uiBorderWidthSpinBox.setMaximum(100)
        self.uiBorderWidthSpinBox.setProperty("value", 2)
        self.uiBorderWidthSpinBox.setObjectName("uiBorderWidthSpinBox")
        self.gridLayout.addWidget(self.uiBorderWidthSpinBox, 2, 1, 1, 1)
        self.uiBorderStyleLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderStyleLabel.setObjectName("uiBorderStyleLabel")
        self.gridLayout.addWidget(self.uiBorderStyleLabel, 3, 0, 1, 1)
        self.uiBorderStyleComboBox = QtWidgets.QComboBox(self.uiStyleSettingsGroupBox)
        self.uiBorderStyleComboBox.setObjectName("uiBorderStyleComboBox")
        self.gridLayout.addWidget(self.uiBorderStyleComboBox, 3, 1, 1, 1)
        self.uiRotationLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiRotationLabel.setObjectName("uiRotationLabel")
        self.gridLayout.addWidget(self.uiRotationLabel, 4, 0, 1, 1)
        self.uiRotationSpinBox = QtWidgets.QSpinBox(self.uiStyleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRotationSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRotationSpinBox.setSizePolicy(sizePolicy)
        self.uiRotationSpinBox.setMinimum(-360)
        self.uiRotationSpinBox.setMaximum(360)
        self.uiRotationSpinBox.setObjectName("uiRotationSpinBox")
        self.gridLayout.addWidget(self.uiRotationSpinBox, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiStyleSettingsGroupBox)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(StyleEditorDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(StyleEditorDialog)
        self.uiButtonBox.accepted.connect(StyleEditorDialog.accept)
        self.uiButtonBox.rejected.connect(StyleEditorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StyleEditorDialog)

    def retranslateUi(self, StyleEditorDialog):
        _translate = QtCore.QCoreApplication.translate
        StyleEditorDialog.setWindowTitle(_translate("StyleEditorDialog", "Style editor"))
        self.uiStyleSettingsGroupBox.setTitle(_translate("StyleEditorDialog", "Style settings"))
        self.uiColorLabel.setText(_translate("StyleEditorDialog", "Fill color:"))
        self.uiBorderColorLabel.setText(_translate("StyleEditorDialog", "Border color:"))
        self.uiBorderWidthLabel.setText(_translate("StyleEditorDialog", "Border width:"))
        self.uiBorderWidthSpinBox.setSuffix(_translate("StyleEditorDialog", " px"))
        self.uiBorderStyleLabel.setText(_translate("StyleEditorDialog", "Border style:"))
        self.uiRotationLabel.setText(_translate("StyleEditorDialog", "Rotation:"))
        self.uiRotationSpinBox.setToolTip(_translate("StyleEditorDialog", "Rotation can be ajusted on the scene for a selected item while\n"
"editing (notes only) with ALT and \'+\' (or P) / ALT and \'-\' (or M)"))
        self.uiRotationSpinBox.setSuffix(_translate("StyleEditorDialog", "°"))

from . import resources_rc
