# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mobile.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(356, 486)
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182);\n"
"font: 16pt \"Arial\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_verticalLayout = QVBoxLayout()
        self.main_verticalLayout.setObjectName(u"main_verticalLayout")
        self.Buttons = QHBoxLayout()
        self.Buttons.setObjectName(u"Buttons")
        self.pushButton = QPushButton(self.main)
        self.pushButton.setObjectName(u"pushButton")

        self.Buttons.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.main)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.Buttons.addWidget(self.pushButton_2)


        self.main_verticalLayout.addLayout(self.Buttons)

        self.scroll_verticalLayout = QVBoxLayout()
        self.scroll_verticalLayout.setObjectName(u"scroll_verticalLayout")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 262, 405))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scroll_verticalLayout.addWidget(self.scrollArea)


        self.main_verticalLayout.addLayout(self.scroll_verticalLayout)


        self.verticalLayout.addLayout(self.main_verticalLayout)

        self.stackedWidget.addWidget(self.main)
        self.task_data = QWidget()
        self.task_data.setObjectName(u"task_data")
        self.verticalLayout_5 = QVBoxLayout(self.task_data)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.task_data)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(142, 142, 142);")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.AddressText = QLabel(self.widget)
        self.AddressText.setObjectName(u"AddressText")
        sizePolicy.setHeightForWidth(self.AddressText.sizePolicy().hasHeightForWidth())
        self.AddressText.setSizePolicy(sizePolicy)
        self.AddressText.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.AddressText)

        self.time_text = QLabel(self.widget)
        self.time_text.setObjectName(u"time_text")
        sizePolicy.setHeightForWidth(self.time_text.sizePolicy().hasHeightForWidth())
        self.time_text.setSizePolicy(sizePolicy)
        self.time_text.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.time_text)

        self.ShowOnMap = QPushButton(self.widget)
        self.ShowOnMap.setObjectName(u"ShowOnMap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ShowOnMap.sizePolicy().hasHeightForWidth())
        self.ShowOnMap.setSizePolicy(sizePolicy1)
        self.ShowOnMap.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.ShowOnMap)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_2)

        self.ClientText = QLabel(self.widget)
        self.ClientText.setObjectName(u"ClientText")
        sizePolicy.setHeightForWidth(self.ClientText.sizePolicy().hasHeightForWidth())
        self.ClientText.setSizePolicy(sizePolicy)
        self.ClientText.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_4.addWidget(self.ClientText)

        self.CallClient = QLabel(self.widget)
        self.CallClient.setObjectName(u"CallClient")
        self.CallClient.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_4.addWidget(self.CallClient)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Type = QLabel(self.widget)
        self.Type.setObjectName(u"Type")
        sizePolicy.setHeightForWidth(self.Type.sizePolicy().hasHeightForWidth())
        self.Type.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.Type)

        self.Status = QLabel(self.widget)
        self.Status.setObjectName(u"Status")
        sizePolicy.setHeightForWidth(self.Status.sizePolicy().hasHeightForWidth())
        self.Status.setSizePolicy(sizePolicy)
        self.Status.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.Status)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.add_comment = QPushButton(self.widget)
        self.add_comment.setObjectName(u"add_comment")

        self.verticalLayout_8.addWidget(self.add_comment)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Back = QPushButton(self.widget)
        self.Back.setObjectName(u"Back")
        sizePolicy1.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy1)
        self.Back.setStyleSheet(u"font: 14pt \"Arial\";")

        self.horizontalLayout.addWidget(self.Back)

        self.Start_Complete = QPushButton(self.widget)
        self.Start_Complete.setObjectName(u"Start_Complete")
        sizePolicy1.setHeightForWidth(self.Start_Complete.sizePolicy().hasHeightForWidth())
        self.Start_Complete.setSizePolicy(sizePolicy1)
        self.Start_Complete.setStyleSheet(u"font: 14pt \"Arial\";")

        self.horizontalLayout.addWidget(self.Start_Complete)


        self.verticalLayout_8.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget.addWidget(self.task_data)
        self.comment = QWidget()
        self.comment.setObjectName(u"comment")
        self.verticalLayout_6 = QVBoxLayout(self.comment)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.com_text = QLineEdit(self.comment)
        self.com_text.setObjectName(u"com_text")

        self.verticalLayout_6.addWidget(self.com_text)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.com_back = QPushButton(self.comment)
        self.com_back.setObjectName(u"com_back")

        self.horizontalLayout_3.addWidget(self.com_back)

        self.com_send = QPushButton(self.comment)
        self.com_send.setObjectName(u"com_send")

        self.horizontalLayout_3.addWidget(self.com_send)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.comment)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.AddressText.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.time_text.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.ShowOnMap.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u043a\u0430\u0440\u0442\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.ClientText.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.CallClient.setText(QCoreApplication.translate("MainWindow", u"number", None))
        self.Type.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.add_comment.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.Start_Complete.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.com_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.com_back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.com_send.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

