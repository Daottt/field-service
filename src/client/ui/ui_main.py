# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateTimeEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 675)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182);\n"
"font: 16pt \"Arial\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navButtons = QWidget(self.centralwidget)
        self.navButtons.setObjectName(u"navButtons")
        self.navButtons.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.navButtons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layouy = QHBoxLayout()
        self.layouy.setObjectName(u"layouy")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layouy.addItem(self.horizontalSpacer_3)

        self.ShowTables = QPushButton(self.navButtons)
        self.ShowTables.setObjectName(u"ShowTables")
        self.ShowTables.setEnabled(False)
        self.ShowTables.setMinimumSize(QSize(250, 0))
        self.ShowTables.setFont(font)

        self.layouy.addWidget(self.ShowTables)

        self.ShowStats = QPushButton(self.navButtons)
        self.ShowStats.setObjectName(u"ShowStats")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowStats.sizePolicy().hasHeightForWidth())
        self.ShowStats.setSizePolicy(sizePolicy)
        self.ShowStats.setMinimumSize(QSize(250, 0))

        self.layouy.addWidget(self.ShowStats)

        self.ShowSettings = QPushButton(self.navButtons)
        self.ShowSettings.setObjectName(u"ShowSettings")
        self.ShowSettings.setEnabled(True)
        self.ShowSettings.setMinimumSize(QSize(250, 0))
        self.ShowSettings.setFont(font)

        self.layouy.addWidget(self.ShowSettings)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layouy.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.layouy)


        self.verticalLayout_2.addWidget(self.navButtons)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.stackedWidget.setFont(font1)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"font: 20pt \"Arial\";")
        self.verticalLayoutWidget_2 = QWidget(self.login)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(380, 170, 321, 231))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"font: 24pt \"Arial\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.loginText = QLineEdit(self.verticalLayoutWidget_2)
        self.loginText.setObjectName(u"loginText")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.loginText.setFont(font3)

        self.verticalLayout_3.addWidget(self.loginText)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.passwordText = QLineEdit(self.verticalLayoutWidget_2)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setFont(font3)

        self.verticalLayout_3.addWidget(self.passwordText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.LoginButton = QPushButton(self.verticalLayoutWidget_2)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet(u"font: 16pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.LoginButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.loginInfo = QLabel(self.verticalLayoutWidget_2)
        self.loginInfo.setObjectName(u"loginInfo")
        self.loginInfo.setFont(font)
        self.loginInfo.setStyleSheet(u"font: 16pt \"Arial\";")
        self.loginInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.loginInfo)

        self.stackedWidget.addWidget(self.login)
        self.Requests = QWidget()
        self.Requests.setObjectName(u"Requests")
        self.Requests.setStyleSheet(u"font: 16pt \"Arial\";")
        self.horizontalLayout_4 = QHBoxLayout(self.Requests)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.task_c_layout = QWidget(self.Requests)
        self.task_c_layout.setObjectName(u"task_c_layout")
        self.horizontalLayout_5 = QHBoxLayout(self.task_c_layout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Layout_t = QVBoxLayout()
        self.Layout_t.setObjectName(u"Layout_t")
        self.label_2 = QLabel(self.task_c_layout)
        self.label_2.setObjectName(u"label_2")

        self.Layout_t.addWidget(self.label_2)

        self.client_data = QPushButton(self.task_c_layout)
        self.client_data.setObjectName(u"client_data")

        self.Layout_t.addWidget(self.client_data)

        self.label_4 = QLabel(self.task_c_layout)
        self.label_4.setObjectName(u"label_4")

        self.Layout_t.addWidget(self.label_4)

        self.personal_box = QComboBox(self.task_c_layout)
        self.personal_box.setObjectName(u"personal_box")

        self.Layout_t.addWidget(self.personal_box)

        self.label_3 = QLabel(self.task_c_layout)
        self.label_3.setObjectName(u"label_3")

        self.Layout_t.addWidget(self.label_3)

        self.start_date = QDateTimeEdit(self.task_c_layout)
        self.start_date.setObjectName(u"start_date")

        self.Layout_t.addWidget(self.start_date)

        self.label_5 = QLabel(self.task_c_layout)
        self.label_5.setObjectName(u"label_5")

        self.Layout_t.addWidget(self.label_5)

        self.type_box = QComboBox(self.task_c_layout)
        self.type_box.setObjectName(u"type_box")

        self.Layout_t.addWidget(self.type_box)

        self.label_6 = QLabel(self.task_c_layout)
        self.label_6.setObjectName(u"label_6")

        self.Layout_t.addWidget(self.label_6)

        self.status_box = QComboBox(self.task_c_layout)
        self.status_box.setObjectName(u"status_box")

        self.Layout_t.addWidget(self.status_box)

        self.create = QPushButton(self.task_c_layout)
        self.create.setObjectName(u"create")

        self.Layout_t.addWidget(self.create)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_t.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.Layout_t)


        self.horizontalLayout_4.addWidget(self.task_c_layout)

        self.verticalLayout_r = QVBoxLayout()
        self.verticalLayout_r.setObjectName(u"verticalLayout_r")
        self.R_buttons = QHBoxLayout()
        self.R_buttons.setObjectName(u"R_buttons")
        self.horizontalSpacer_11 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.R_buttons.addItem(self.horizontalSpacer_11)

        self.Add_R = QPushButton(self.Requests)
        self.Add_R.setObjectName(u"Add_R")
        self.Add_R.setMinimumSize(QSize(200, 0))
        self.Add_R.setFont(font)

        self.R_buttons.addWidget(self.Add_R)

        self.Update_R = QPushButton(self.Requests)
        self.Update_R.setObjectName(u"Update_R")
        self.Update_R.setMinimumSize(QSize(200, 0))
        self.Update_R.setFont(font)

        self.R_buttons.addWidget(self.Update_R)

        self.Delete_R = QPushButton(self.Requests)
        self.Delete_R.setObjectName(u"Delete_R")
        self.Delete_R.setMinimumSize(QSize(200, 0))
        self.Delete_R.setFont(font)

        self.R_buttons.addWidget(self.Delete_R)

        self.horizontalSpacer_12 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.R_buttons.addItem(self.horizontalSpacer_12)


        self.verticalLayout_r.addLayout(self.R_buttons)

        self.RequestsTable = QTableWidget(self.Requests)
        self.RequestsTable.setObjectName(u"RequestsTable")
        self.RequestsTable.setFont(font)
        self.RequestsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.RequestsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.RequestsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.RequestsTable.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.RequestsTable.horizontalHeader().setVisible(True)
        self.RequestsTable.horizontalHeader().setMinimumSectionSize(60)
        self.RequestsTable.horizontalHeader().setDefaultSectionSize(200)
        self.RequestsTable.verticalHeader().setVisible(False)

        self.verticalLayout_r.addWidget(self.RequestsTable)


        self.horizontalLayout_4.addLayout(self.verticalLayout_r)

        self.stackedWidget.addWidget(self.Requests)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.horizontalLayout_3 = QHBoxLayout(self.Settings)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SettingsList = QListWidget(self.Settings)
        self.SettingsList.setObjectName(u"SettingsList")
        self.SettingsList.setMinimumSize(QSize(200, 0))
        self.SettingsList.setMaximumSize(QSize(250, 16777215))
        self.SettingsList.setFont(font)

        self.horizontalLayout_3.addWidget(self.SettingsList)

        self.stacked_Settings = QStackedWidget(self.Settings)
        self.stacked_Settings.setObjectName(u"stacked_Settings")
        self.page_Users = QWidget()
        self.page_Users.setObjectName(u"page_Users")
        self.horizontalLayout = QHBoxLayout(self.page_Users)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_settings_5 = QVBoxLayout()
        self.table_settings_5.setObjectName(u"table_settings_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_15 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_15)

        self.settings_add_5 = QPushButton(self.page_Users)
        self.settings_add_5.setObjectName(u"settings_add_5")
        self.settings_add_5.setMinimumSize(QSize(200, 0))
        self.settings_add_5.setFont(font)

        self.horizontalLayout_9.addWidget(self.settings_add_5)

        self.settings_update_5 = QPushButton(self.page_Users)
        self.settings_update_5.setObjectName(u"settings_update_5")
        self.settings_update_5.setMinimumSize(QSize(200, 0))
        self.settings_update_5.setFont(font)

        self.horizontalLayout_9.addWidget(self.settings_update_5)

        self.settings_delete_5 = QPushButton(self.page_Users)
        self.settings_delete_5.setObjectName(u"settings_delete_5")
        self.settings_delete_5.setMinimumSize(QSize(200, 0))
        self.settings_delete_5.setFont(font)

        self.horizontalLayout_9.addWidget(self.settings_delete_5)

        self.horizontalSpacer_16 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)


        self.table_settings_5.addLayout(self.horizontalLayout_9)

        self.settings_table_5 = QTableWidget(self.page_Users)
        self.settings_table_5.setObjectName(u"settings_table_5")
        self.settings_table_5.setFont(font)
        self.settings_table_5.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_5.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_5.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_5.horizontalHeader().setVisible(True)
        self.settings_table_5.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_5.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_5.verticalHeader().setVisible(False)

        self.table_settings_5.addWidget(self.settings_table_5)


        self.horizontalLayout.addLayout(self.table_settings_5)

        self.stacked_Settings.addWidget(self.page_Users)
        self.page_Personal = QWidget()
        self.page_Personal.setObjectName(u"page_Personal")
        self.horizontalLayout_16 = QHBoxLayout(self.page_Personal)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.table_settings_10 = QVBoxLayout()
        self.table_settings_10.setObjectName(u"table_settings_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_25 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.settings_add_10 = QPushButton(self.page_Personal)
        self.settings_add_10.setObjectName(u"settings_add_10")
        self.settings_add_10.setMinimumSize(QSize(200, 0))
        self.settings_add_10.setFont(font)

        self.horizontalLayout_14.addWidget(self.settings_add_10)

        self.settings_update_10 = QPushButton(self.page_Personal)
        self.settings_update_10.setObjectName(u"settings_update_10")
        self.settings_update_10.setMinimumSize(QSize(200, 0))
        self.settings_update_10.setFont(font)

        self.horizontalLayout_14.addWidget(self.settings_update_10)

        self.settings_delete_10 = QPushButton(self.page_Personal)
        self.settings_delete_10.setObjectName(u"settings_delete_10")
        self.settings_delete_10.setMinimumSize(QSize(200, 0))
        self.settings_delete_10.setFont(font)

        self.horizontalLayout_14.addWidget(self.settings_delete_10)

        self.horizontalSpacer_26 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)


        self.table_settings_10.addLayout(self.horizontalLayout_14)

        self.settings_table_10 = QTableWidget(self.page_Personal)
        self.settings_table_10.setObjectName(u"settings_table_10")
        self.settings_table_10.setFont(font)
        self.settings_table_10.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_10.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_10.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_10.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_10.horizontalHeader().setVisible(True)
        self.settings_table_10.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_10.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_10.verticalHeader().setVisible(False)

        self.table_settings_10.addWidget(self.settings_table_10)


        self.horizontalLayout_16.addLayout(self.table_settings_10)

        self.stacked_Settings.addWidget(self.page_Personal)
        self.page_Type = QWidget()
        self.page_Type.setObjectName(u"page_Type")
        self.horizontalLayout_19 = QHBoxLayout(self.page_Type)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.table_settings_8 = QVBoxLayout()
        self.table_settings_8.setObjectName(u"table_settings_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_21 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)

        self.settings_add_8 = QPushButton(self.page_Type)
        self.settings_add_8.setObjectName(u"settings_add_8")
        self.settings_add_8.setMinimumSize(QSize(200, 0))
        self.settings_add_8.setFont(font)

        self.horizontalLayout_12.addWidget(self.settings_add_8)

        self.settings_update_8 = QPushButton(self.page_Type)
        self.settings_update_8.setObjectName(u"settings_update_8")
        self.settings_update_8.setMinimumSize(QSize(200, 0))
        self.settings_update_8.setFont(font)

        self.horizontalLayout_12.addWidget(self.settings_update_8)

        self.settings_delete_8 = QPushButton(self.page_Type)
        self.settings_delete_8.setObjectName(u"settings_delete_8")
        self.settings_delete_8.setMinimumSize(QSize(200, 0))
        self.settings_delete_8.setFont(font)

        self.horizontalLayout_12.addWidget(self.settings_delete_8)

        self.horizontalSpacer_22 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_22)


        self.table_settings_8.addLayout(self.horizontalLayout_12)

        self.settings_table_8 = QTableWidget(self.page_Type)
        self.settings_table_8.setObjectName(u"settings_table_8")
        self.settings_table_8.setFont(font)
        self.settings_table_8.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_8.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_8.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_8.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_8.horizontalHeader().setVisible(True)
        self.settings_table_8.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_8.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_8.verticalHeader().setVisible(False)

        self.table_settings_8.addWidget(self.settings_table_8)


        self.horizontalLayout_19.addLayout(self.table_settings_8)

        self.stacked_Settings.addWidget(self.page_Type)
        self.page_Status = QWidget()
        self.page_Status.setObjectName(u"page_Status")
        self.horizontalLayout_18 = QHBoxLayout(self.page_Status)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.table_settings_9 = QVBoxLayout()
        self.table_settings_9.setObjectName(u"table_settings_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_23 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.settings_add_9 = QPushButton(self.page_Status)
        self.settings_add_9.setObjectName(u"settings_add_9")
        self.settings_add_9.setMinimumSize(QSize(200, 0))
        self.settings_add_9.setFont(font)

        self.horizontalLayout_13.addWidget(self.settings_add_9)

        self.settings_update_9 = QPushButton(self.page_Status)
        self.settings_update_9.setObjectName(u"settings_update_9")
        self.settings_update_9.setMinimumSize(QSize(200, 0))
        self.settings_update_9.setFont(font)

        self.horizontalLayout_13.addWidget(self.settings_update_9)

        self.settings_delete_9 = QPushButton(self.page_Status)
        self.settings_delete_9.setObjectName(u"settings_delete_9")
        self.settings_delete_9.setMinimumSize(QSize(200, 0))
        self.settings_delete_9.setFont(font)

        self.horizontalLayout_13.addWidget(self.settings_delete_9)

        self.horizontalSpacer_24 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)


        self.table_settings_9.addLayout(self.horizontalLayout_13)

        self.settings_table_9 = QTableWidget(self.page_Status)
        self.settings_table_9.setObjectName(u"settings_table_9")
        self.settings_table_9.setFont(font)
        self.settings_table_9.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_9.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_9.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_9.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_9.horizontalHeader().setVisible(True)
        self.settings_table_9.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_9.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_9.verticalHeader().setVisible(False)

        self.table_settings_9.addWidget(self.settings_table_9)


        self.horizontalLayout_18.addLayout(self.table_settings_9)

        self.stacked_Settings.addWidget(self.page_Status)
        self.page_Post = QWidget()
        self.page_Post.setObjectName(u"page_Post")
        self.horizontalLayout_17 = QHBoxLayout(self.page_Post)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.table_settings_7 = QVBoxLayout()
        self.table_settings_7.setObjectName(u"table_settings_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_19 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_19)

        self.settings_add_7 = QPushButton(self.page_Post)
        self.settings_add_7.setObjectName(u"settings_add_7")
        self.settings_add_7.setMinimumSize(QSize(200, 0))
        self.settings_add_7.setFont(font)

        self.horizontalLayout_11.addWidget(self.settings_add_7)

        self.settings_update_7 = QPushButton(self.page_Post)
        self.settings_update_7.setObjectName(u"settings_update_7")
        self.settings_update_7.setMinimumSize(QSize(200, 0))
        self.settings_update_7.setFont(font)

        self.horizontalLayout_11.addWidget(self.settings_update_7)

        self.settings_delete_7 = QPushButton(self.page_Post)
        self.settings_delete_7.setObjectName(u"settings_delete_7")
        self.settings_delete_7.setMinimumSize(QSize(200, 0))
        self.settings_delete_7.setFont(font)

        self.horizontalLayout_11.addWidget(self.settings_delete_7)

        self.horizontalSpacer_20 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)


        self.table_settings_7.addLayout(self.horizontalLayout_11)

        self.settings_table_7 = QTableWidget(self.page_Post)
        self.settings_table_7.setObjectName(u"settings_table_7")
        self.settings_table_7.setFont(font)
        self.settings_table_7.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_7.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_7.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_7.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_7.horizontalHeader().setVisible(True)
        self.settings_table_7.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_7.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_7.verticalHeader().setVisible(False)

        self.table_settings_7.addWidget(self.settings_table_7)


        self.horizontalLayout_17.addLayout(self.table_settings_7)

        self.stacked_Settings.addWidget(self.page_Post)
        self.page_ClientData = QWidget()
        self.page_ClientData.setObjectName(u"page_ClientData")
        self.horizontalLayout_15 = QHBoxLayout(self.page_ClientData)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.table_settings_6 = QVBoxLayout()
        self.table_settings_6.setObjectName(u"table_settings_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_17 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.settings_add_6 = QPushButton(self.page_ClientData)
        self.settings_add_6.setObjectName(u"settings_add_6")
        self.settings_add_6.setMinimumSize(QSize(200, 0))
        self.settings_add_6.setFont(font)

        self.horizontalLayout_10.addWidget(self.settings_add_6)

        self.settings_update_6 = QPushButton(self.page_ClientData)
        self.settings_update_6.setObjectName(u"settings_update_6")
        self.settings_update_6.setMinimumSize(QSize(200, 0))
        self.settings_update_6.setFont(font)

        self.horizontalLayout_10.addWidget(self.settings_update_6)

        self.settings_delete_6 = QPushButton(self.page_ClientData)
        self.settings_delete_6.setObjectName(u"settings_delete_6")
        self.settings_delete_6.setMinimumSize(QSize(200, 0))
        self.settings_delete_6.setFont(font)

        self.horizontalLayout_10.addWidget(self.settings_delete_6)

        self.horizontalSpacer_18 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)


        self.table_settings_6.addLayout(self.horizontalLayout_10)

        self.settings_table_6 = QTableWidget(self.page_ClientData)
        self.settings_table_6.setObjectName(u"settings_table_6")
        self.settings_table_6.setFont(font)
        self.settings_table_6.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_6.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_6.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_6.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_6.horizontalHeader().setVisible(True)
        self.settings_table_6.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_6.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_6.verticalHeader().setVisible(False)

        self.table_settings_6.addWidget(self.settings_table_6)


        self.horizontalLayout_15.addLayout(self.table_settings_6)

        self.stacked_Settings.addWidget(self.page_ClientData)
        self.page_App = QWidget()
        self.page_App.setObjectName(u"page_App")
        self.Log_out = QPushButton(self.page_App)
        self.Log_out.setObjectName(u"Log_out")
        self.Log_out.setEnabled(True)
        self.Log_out.setGeometry(QRect(40, 20, 250, 31))
        self.Log_out.setMinimumSize(QSize(250, 0))
        self.Log_out.setFont(font)
        self.widget_debug = QWidget(self.page_App)
        self.widget_debug.setObjectName(u"widget_debug")
        self.widget_debug.setGeometry(QRect(20, 60, 1051, 661))
        self.layoutWidget_8 = QWidget(self.widget_debug)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(0, 0, 776, 564))
        self.table_settings_11 = QVBoxLayout(self.layoutWidget_8)
        self.table_settings_11.setObjectName(u"table_settings_11")
        self.table_settings_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_27 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_27)

        self.settings_add_11 = QPushButton(self.layoutWidget_8)
        self.settings_add_11.setObjectName(u"settings_add_11")
        self.settings_add_11.setMinimumSize(QSize(200, 0))
        self.settings_add_11.setFont(font)

        self.horizontalLayout_20.addWidget(self.settings_add_11)

        self.settings_update_11 = QPushButton(self.layoutWidget_8)
        self.settings_update_11.setObjectName(u"settings_update_11")
        self.settings_update_11.setMinimumSize(QSize(200, 0))
        self.settings_update_11.setFont(font)

        self.horizontalLayout_20.addWidget(self.settings_update_11)

        self.settings_delete_11 = QPushButton(self.layoutWidget_8)
        self.settings_delete_11.setObjectName(u"settings_delete_11")
        self.settings_delete_11.setMinimumSize(QSize(200, 0))
        self.settings_delete_11.setFont(font)

        self.horizontalLayout_20.addWidget(self.settings_delete_11)

        self.horizontalSpacer_28 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_28)


        self.table_settings_11.addLayout(self.horizontalLayout_20)

        self.settings_table_11 = QTableWidget(self.layoutWidget_8)
        self.settings_table_11.setObjectName(u"settings_table_11")
        self.settings_table_11.setFont(font)
        self.settings_table_11.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.settings_table_11.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.settings_table_11.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.settings_table_11.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.settings_table_11.horizontalHeader().setVisible(True)
        self.settings_table_11.horizontalHeader().setMinimumSectionSize(60)
        self.settings_table_11.horizontalHeader().setDefaultSectionSize(200)
        self.settings_table_11.verticalHeader().setVisible(False)

        self.table_settings_11.addWidget(self.settings_table_11)

        self.stacked_Settings.addWidget(self.page_App)

        self.horizontalLayout_3.addWidget(self.stacked_Settings)

        self.stackedWidget.addWidget(self.Settings)
        self.Stats = QWidget()
        self.Stats.setObjectName(u"Stats")
        self.gridLayout = QGridLayout(self.Stats)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.Stats)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SumText = QLabel(self.widget)
        self.SumText.setObjectName(u"SumText")

        self.verticalLayout.addWidget(self.SumText)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.TypeText = QLabel(self.widget)
        self.TypeText.setObjectName(u"TypeText")

        self.verticalLayout.addWidget(self.TypeText)

        self.TaskTypes = QListWidget(self.widget)
        self.TaskTypes.setObjectName(u"TaskTypes")

        self.verticalLayout.addWidget(self.TaskTypes)


        self.verticalLayout_5.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.Stats)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stacked_Settings.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShowTables.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.ShowStats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.ShowSettings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.loginText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwordText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.loginInfo.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.client_data.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.Add_R.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Update_R.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete_R.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_10.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_8.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_7.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Log_out.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.settings_add_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_11.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.SumText.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.TypeText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u0437\u0430\u044f\u0432\u043e\u043a", None))
    # retranslateUi

