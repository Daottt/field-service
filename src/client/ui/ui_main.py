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
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 676)
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
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.navButtons = QWidget(self.centralwidget)
        self.navButtons.setObjectName(u"navButtons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navButtons.sizePolicy().hasHeightForWidth())
        self.navButtons.setSizePolicy(sizePolicy)
        self.navButtons.setMinimumSize(QSize(140, 0))
        self.navButtons.setStyleSheet(u"QWidget#navButtons{\n"
"	border: 1px solid rgb(130,135,144);\n"
"	alignment: center;\n"
"};")
        self.verticalLayout_nav = QVBoxLayout(self.navButtons)
        self.verticalLayout_nav.setObjectName(u"verticalLayout_nav")
        self.verticalLayout_nav.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_nav.setContentsMargins(10, 10, -1, -1)
        self.ShowTables = QPushButton(self.navButtons)
        self.ShowTables.setObjectName(u"ShowTables")
        self.ShowTables.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ShowTables.sizePolicy().hasHeightForWidth())
        self.ShowTables.setSizePolicy(sizePolicy1)
        self.ShowTables.setMinimumSize(QSize(120, 0))
        self.ShowTables.setFont(font)
        self.ShowTables.setFlat(False)

        self.verticalLayout_nav.addWidget(self.ShowTables)

        self.ShowClietns = QPushButton(self.navButtons)
        self.ShowClietns.setObjectName(u"ShowClietns")
        sizePolicy1.setHeightForWidth(self.ShowClietns.sizePolicy().hasHeightForWidth())
        self.ShowClietns.setSizePolicy(sizePolicy1)
        self.ShowClietns.setMinimumSize(QSize(120, 0))

        self.verticalLayout_nav.addWidget(self.ShowClietns)

        self.ShowPersonal = QPushButton(self.navButtons)
        self.ShowPersonal.setObjectName(u"ShowPersonal")
        sizePolicy1.setHeightForWidth(self.ShowPersonal.sizePolicy().hasHeightForWidth())
        self.ShowPersonal.setSizePolicy(sizePolicy1)
        self.ShowPersonal.setMinimumSize(QSize(120, 0))

        self.verticalLayout_nav.addWidget(self.ShowPersonal)

        self.ShowStats = QPushButton(self.navButtons)
        self.ShowStats.setObjectName(u"ShowStats")
        sizePolicy1.setHeightForWidth(self.ShowStats.sizePolicy().hasHeightForWidth())
        self.ShowStats.setSizePolicy(sizePolicy1)
        self.ShowStats.setMinimumSize(QSize(120, 0))

        self.verticalLayout_nav.addWidget(self.ShowStats)

        self.ShowSettings = QPushButton(self.navButtons)
        self.ShowSettings.setObjectName(u"ShowSettings")
        self.ShowSettings.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ShowSettings.sizePolicy().hasHeightForWidth())
        self.ShowSettings.setSizePolicy(sizePolicy1)
        self.ShowSettings.setMinimumSize(QSize(120, 0))
        self.ShowSettings.setFont(font)

        self.verticalLayout_nav.addWidget(self.ShowSettings)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_nav.addItem(self.verticalSpacer_6)


        self.horizontalLayout_6.addWidget(self.navButtons)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.personal_box.sizePolicy().hasHeightForWidth())
        self.personal_box.setSizePolicy(sizePolicy2)

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
        sizePolicy2.setHeightForWidth(self.type_box.sizePolicy().hasHeightForWidth())
        self.type_box.setSizePolicy(sizePolicy2)

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
        self.Add_R.setMinimumSize(QSize(150, 0))
        self.Add_R.setFont(font)

        self.R_buttons.addWidget(self.Add_R)

        self.Update_R = QPushButton(self.Requests)
        self.Update_R.setObjectName(u"Update_R")
        self.Update_R.setMinimumSize(QSize(150, 0))
        self.Update_R.setFont(font)

        self.R_buttons.addWidget(self.Update_R)

        self.Delete_R = QPushButton(self.Requests)
        self.Delete_R.setObjectName(u"Delete_R")
        self.Delete_R.setMinimumSize(QSize(150, 0))
        self.Delete_R.setFont(font)

        self.R_buttons.addWidget(self.Delete_R)

        self.com_R = QPushButton(self.Requests)
        self.com_R.setObjectName(u"com_R")
        self.com_R.setMinimumSize(QSize(140, 0))

        self.R_buttons.addWidget(self.com_R)

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
        self.stacked_Settings.addWidget(self.page_ClientData)
        self.page_App = QWidget()
        self.page_App.setObjectName(u"page_App")
        self.Log_out = QPushButton(self.page_App)
        self.Log_out.setObjectName(u"Log_out")
        self.Log_out.setEnabled(True)
        self.Log_out.setGeometry(QRect(210, 40, 250, 31))
        self.Log_out.setMinimumSize(QSize(250, 0))
        self.Log_out.setFont(font)
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
        self.Clients = QWidget()
        self.Clients.setObjectName(u"Clients")
        self.verticalLayout_2 = QVBoxLayout(self.Clients)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_clients = QVBoxLayout()
        self.layout_clients.setObjectName(u"layout_clients")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_17 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.client_story = QPushButton(self.Clients)
        self.client_story.setObjectName(u"client_story")
        self.client_story.setMinimumSize(QSize(150, 0))
        self.client_story.setFont(font)

        self.horizontalLayout_10.addWidget(self.client_story)

        self.client_add = QPushButton(self.Clients)
        self.client_add.setObjectName(u"client_add")
        self.client_add.setMinimumSize(QSize(150, 0))
        self.client_add.setFont(font)

        self.horizontalLayout_10.addWidget(self.client_add)

        self.client_update = QPushButton(self.Clients)
        self.client_update.setObjectName(u"client_update")
        self.client_update.setMinimumSize(QSize(150, 0))
        self.client_update.setFont(font)

        self.horizontalLayout_10.addWidget(self.client_update)

        self.client_delete = QPushButton(self.Clients)
        self.client_delete.setObjectName(u"client_delete")
        self.client_delete.setMinimumSize(QSize(150, 0))
        self.client_delete.setFont(font)

        self.horizontalLayout_10.addWidget(self.client_delete)

        self.horizontalSpacer_18 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)


        self.layout_clients.addLayout(self.horizontalLayout_10)

        self.client_table = QTableWidget(self.Clients)
        self.client_table.setObjectName(u"client_table")
        self.client_table.setFont(font)
        self.client_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.client_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.client_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.client_table.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.client_table.horizontalHeader().setVisible(True)
        self.client_table.horizontalHeader().setMinimumSectionSize(60)
        self.client_table.horizontalHeader().setDefaultSectionSize(200)
        self.client_table.verticalHeader().setVisible(False)

        self.layout_clients.addWidget(self.client_table)


        self.verticalLayout_2.addLayout(self.layout_clients)

        self.stackedWidget.addWidget(self.Clients)
        self.Personal = QWidget()
        self.Personal.setObjectName(u"Personal")
        self.verticalLayout_4 = QVBoxLayout(self.Personal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pers_layout = QVBoxLayout()
        self.pers_layout.setObjectName(u"pers_layout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_25 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.personal_rew = QPushButton(self.Personal)
        self.personal_rew.setObjectName(u"personal_rew")
        self.personal_rew.setMinimumSize(QSize(150, 0))
        self.personal_rew.setFont(font)

        self.horizontalLayout_14.addWidget(self.personal_rew)

        self.personal_add = QPushButton(self.Personal)
        self.personal_add.setObjectName(u"personal_add")
        self.personal_add.setMinimumSize(QSize(150, 0))
        self.personal_add.setFont(font)

        self.horizontalLayout_14.addWidget(self.personal_add)

        self.personal_update = QPushButton(self.Personal)
        self.personal_update.setObjectName(u"personal_update")
        self.personal_update.setMinimumSize(QSize(150, 0))
        self.personal_update.setFont(font)

        self.horizontalLayout_14.addWidget(self.personal_update)

        self.personal_delete = QPushButton(self.Personal)
        self.personal_delete.setObjectName(u"personal_delete")
        self.personal_delete.setMinimumSize(QSize(150, 0))
        self.personal_delete.setFont(font)

        self.horizontalLayout_14.addWidget(self.personal_delete)

        self.horizontalSpacer_26 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)


        self.pers_layout.addLayout(self.horizontalLayout_14)

        self.personal_table = QTableWidget(self.Personal)
        self.personal_table.setObjectName(u"personal_table")
        self.personal_table.setFont(font)
        self.personal_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.personal_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.personal_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.personal_table.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.personal_table.horizontalHeader().setVisible(True)
        self.personal_table.horizontalHeader().setMinimumSectionSize(60)
        self.personal_table.horizontalHeader().setDefaultSectionSize(200)
        self.personal_table.verticalHeader().setVisible(False)

        self.pers_layout.addWidget(self.personal_table)


        self.verticalLayout_4.addLayout(self.pers_layout)

        self.stackedWidget.addWidget(self.Personal)

        self.horizontalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ShowTables.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)
        self.stacked_Settings.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShowTables.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.ShowClietns.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.ShowPersonal.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
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
        self.com_R.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438", None))
        self.settings_add_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_8.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.settings_add_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.settings_update_7.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.settings_delete_7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Log_out.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.SumText.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.TypeText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.client_story.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.client_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.client_update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.client_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.personal_rew.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u044b\u0432\u044b", None))
        self.personal_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.personal_update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.personal_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

