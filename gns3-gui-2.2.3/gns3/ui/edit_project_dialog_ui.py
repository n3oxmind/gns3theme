# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/edit_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditProjectDialog(object):
    def setupUi(self, EditProjectDialog):
        EditProjectDialog.setObjectName("EditProjectDialog")
        EditProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditProjectDialog.resize(946, 502)
        EditProjectDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(EditProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(EditProjectDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.uiGeneralTab = QtWidgets.QWidget()
        self.uiGeneralTab.setObjectName("uiGeneralTab")
        self.uiGeneralGrid = QtWidgets.QGridLayout(self.uiGeneralTab)
        self.uiGeneralGrid.setObjectName("uiGeneralGrid")
        self.uiSceneWidthLabel = QtWidgets.QLabel(self.uiGeneralTab)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.uiGeneralGrid.addWidget(self.uiSceneWidthLabel, 2, 0, 1, 1)
        self.uiProjectAutoCloseCheckBox = QtWidgets.QCheckBox(self.uiGeneralTab)
        self.uiProjectAutoCloseCheckBox.setObjectName("uiProjectAutoCloseCheckBox")
        self.uiGeneralGrid.addWidget(self.uiProjectAutoCloseCheckBox, 9, 0, 1, 3)
        self.uiProjectNameLabel = QtWidgets.QLabel(self.uiGeneralTab)
        self.uiProjectNameLabel.setObjectName("uiProjectNameLabel")
        self.uiGeneralGrid.addWidget(self.uiProjectNameLabel, 1, 0, 1, 1)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(self.uiGeneralTab)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.uiGeneralGrid.addWidget(self.uiSceneWidthSpinBox, 2, 1, 1, 1)
        self.uiNodeGridSizeSpinBox = QtWidgets.QSpinBox(self.uiGeneralTab)
        self.uiNodeGridSizeSpinBox.setMinimum(5)
        self.uiNodeGridSizeSpinBox.setMaximum(150)
        self.uiNodeGridSizeSpinBox.setSingleStep(5)
        self.uiNodeGridSizeSpinBox.setProperty("value", 75)
        self.uiNodeGridSizeSpinBox.setObjectName("uiNodeGridSizeSpinBox")
        self.uiGeneralGrid.addWidget(self.uiNodeGridSizeSpinBox, 4, 1, 1, 1)
        self.uiDrawingGridSizeSpinBox = QtWidgets.QSpinBox(self.uiGeneralTab)
        self.uiDrawingGridSizeSpinBox.setMinimum(5)
        self.uiDrawingGridSizeSpinBox.setMaximum(100)
        self.uiDrawingGridSizeSpinBox.setSingleStep(5)
        self.uiDrawingGridSizeSpinBox.setProperty("value", 25)
        self.uiDrawingGridSizeSpinBox.setObjectName("uiDrawingGridSizeSpinBox")
        self.uiGeneralGrid.addWidget(self.uiDrawingGridSizeSpinBox, 5, 1, 1, 1)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(self.uiGeneralTab)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.uiGeneralGrid.addWidget(self.uiSceneHeightSpinBox, 3, 1, 1, 1)
        self.uiSceneHeightLabel = QtWidgets.QLabel(self.uiGeneralTab)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.uiGeneralGrid.addWidget(self.uiSceneHeightLabel, 3, 0, 1, 1)
        self.uiProjectNameLineEdit = QtWidgets.QLineEdit(self.uiGeneralTab)
        self.uiProjectNameLineEdit.setObjectName("uiProjectNameLineEdit")
        self.uiGeneralGrid.addWidget(self.uiProjectNameLineEdit, 1, 1, 1, 1)
        self.uiNodeGridSizeLabel = QtWidgets.QLabel(self.uiGeneralTab)
        self.uiNodeGridSizeLabel.setObjectName("uiNodeGridSizeLabel")
        self.uiGeneralGrid.addWidget(self.uiNodeGridSizeLabel, 4, 0, 1, 1)
        self.uiDrawingGridSizeLabel = QtWidgets.QLabel(self.uiGeneralTab)
        self.uiDrawingGridSizeLabel.setObjectName("uiDrawingGridSizeLabel")
        self.uiGeneralGrid.addWidget(self.uiDrawingGridSizeLabel, 5, 0, 1, 1)
        self.uiProjectAutoOpenCheckBox = QtWidgets.QCheckBox(self.uiGeneralTab)
        self.uiProjectAutoOpenCheckBox.setObjectName("uiProjectAutoOpenCheckBox")
        self.uiGeneralGrid.addWidget(self.uiProjectAutoOpenCheckBox, 7, 0, 1, 3)
        self.uiProjectAutoStartCheckBox = QtWidgets.QCheckBox(self.uiGeneralTab)
        self.uiProjectAutoStartCheckBox.setObjectName("uiProjectAutoStartCheckBox")
        self.uiGeneralGrid.addWidget(self.uiProjectAutoStartCheckBox, 8, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.uiGeneralGrid.addItem(spacerItem, 10, 0, 1, 1)
        self.tabWidget.addTab(self.uiGeneralTab, "")
        self.uiGlobalVariablesTab = QtWidgets.QWidget()
        self.uiGlobalVariablesTab.setObjectName("uiGlobalVariablesTab")
        self.uiGlobalVariablesGrid = QtWidgets.QGridLayout(self.uiGlobalVariablesTab)
        self.uiGlobalVariablesGrid.setObjectName("uiGlobalVariablesGrid")
        self.tabWidget.addTab(self.uiGlobalVariablesTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(EditProjectDialog)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 0, 1, 1)

        self.retranslateUi(EditProjectDialog)
        self.tabWidget.setCurrentIndex(0)
        self.uiButtonBox.accepted.connect(EditProjectDialog.accept)
        self.uiButtonBox.rejected.connect(EditProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditProjectDialog)

    def retranslateUi(self, EditProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        EditProjectDialog.setWindowTitle(_translate("EditProjectDialog", "Edit project"))
        self.uiSceneWidthLabel.setText(_translate("EditProjectDialog", "Scene width:"))
        self.uiProjectAutoCloseCheckBox.setText(_translate("EditProjectDialog", "Leave this project running in the background when closing GNS3"))
        self.uiProjectNameLabel.setText(_translate("EditProjectDialog", "Project Name:"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneHeightLabel.setText(_translate("EditProjectDialog", "Scene height:"))
        self.uiNodeGridSizeLabel.setText(_translate("EditProjectDialog", "Node grid size:"))
        self.uiDrawingGridSizeLabel.setText(_translate("EditProjectDialog", "Drawing grid size:"))
        self.uiProjectAutoOpenCheckBox.setText(_translate("EditProjectDialog", "Open this project in the background when GNS3 server starts"))
        self.uiProjectAutoStartCheckBox.setText(_translate("EditProjectDialog", "Start all nodes when this project is opened"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uiGeneralTab), _translate("EditProjectDialog", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uiGlobalVariablesTab), _translate("EditProjectDialog", "Global variables"))
