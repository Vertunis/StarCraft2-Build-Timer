# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\Programming\Python\Templates\02_Testprojekte\StarCraft Timer\GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 10, 341, 531))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox_Races = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Races.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_Races.setFont(font)
        self.comboBox_Races.setObjectName("comboBox_Races")
        self.listWidget_builds = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_builds.setGeometry(QtCore.QRect(10, 70, 321, 451))
        self.listWidget_builds.setObjectName("listWidget_builds")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_Timer_Stop = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_Timer_Stop.setEnabled(True)
        self.btn_Timer_Stop.setGeometry(QtCore.QRect(140, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Timer_Stop.setFont(font)
        self.btn_Timer_Stop.setObjectName("btn_Timer_Stop")
        self.btn_Timer_Reset = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_Timer_Reset.setEnabled(True)
        self.btn_Timer_Reset.setGeometry(QtCore.QRect(270, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Timer_Reset.setFont(font)
        self.btn_Timer_Reset.setObjectName("btn_Timer_Reset")
        self.btn_Timer_Start = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_Timer_Start.setGeometry(QtCore.QRect(10, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Timer_Start.setFont(font)
        self.btn_Timer_Start.setObjectName("btn_Timer_Start")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 100, 401, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_2.setGeometry(QtCore.QRect(126, 92, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_object = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_object.setGeometry(QtCore.QRect(10, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_object.setFont(font)
        self.textBrowser_object.setObjectName("textBrowser_object")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox.setGeometry(QtCore.QRect(66, 92, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_probe_nr = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_probe_nr.setGeometry(QtCore.QRect(8, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_probe_nr.setFont(font)
        self.textBrowser_probe_nr.setObjectName("textBrowser_probe_nr")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(6, 92, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_timer = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_timer.setGeometry(QtCore.QRect(4, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_timer.setFont(font)
        self.textBrowser_timer.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser_timer.setObjectName("textBrowser_timer")
        self.progressBar_TimeSinceStart = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_TimeSinceStart.setGeometry(QtCore.QRect(-50, 60, 441, 31))
        self.progressBar_TimeSinceStart.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_TimeSinceStart.setProperty("value", 24)
        self.progressBar_TimeSinceStart.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_TimeSinceStart.setInvertedAppearance(True)
        self.progressBar_TimeSinceStart.setFormat("")
        self.progressBar_TimeSinceStart.setObjectName("progressBar_TimeSinceStart")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_loaded_built = QtWidgets.QLabel(self.groupBox_6)
        self.label_loaded_built.setGeometry(QtCore.QRect(116, 31, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_loaded_built.setFont(font)
        self.label_loaded_built.setObjectName("label_loaded_built")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(149, 65, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_current_time = QtWidgets.QLabel(self.groupBox_6)
        self.label_current_time.setGeometry(QtCore.QRect(187, 65, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_current_time.setFont(font)
        self.label_current_time.setObjectName("label_current_time")
        self.tableView = QtWidgets.QTableView(self.groupBox_6)
        self.tableView.setGeometry(QtCore.QRect(10, 160, 381, 271))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Built Selection"))
        self.comboBox_Races.setToolTip(_translate("MainWindow", "SC2 Race Selection"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Timer Settings"))
        self.btn_Timer_Stop.setText(_translate("MainWindow", " Stop"))
        self.btn_Timer_Reset.setText(_translate("MainWindow", "Reset"))
        self.btn_Timer_Start.setText(_translate("MainWindow", "Timer Start"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Next Build Object"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Next Objekt"))
        self.groupBox.setTitle(_translate("MainWindow", "Probe"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Timer"))
        self.label_5.setText(_translate("MainWindow", "Loaded Build:"))
        self.label_loaded_built.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "TIME"))
        self.label_current_time.setText(_translate("MainWindow", "00:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Timer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Config"))
