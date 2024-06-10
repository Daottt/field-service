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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(346, 486)
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182);\n"
"font: 16pt \"Arial\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 234, 405))
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
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.task_data)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.AddressText = QLabel(self.task_data)
        self.AddressText.setObjectName(u"AddressText")
        self.AddressText.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.AddressText)

        self.ShowOnMap = QPushButton(self.task_data)
        self.ShowOnMap.setObjectName(u"ShowOnMap")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowOnMap.sizePolicy().hasHeightForWidth())
        self.ShowOnMap.setSizePolicy(sizePolicy)
        self.ShowOnMap.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.ShowOnMap)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.task_data)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.ClientText = QLabel(self.task_data)
        self.ClientText.setObjectName(u"ClientText")
        self.ClientText.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout_4.addWidget(self.ClientText)

        self.CallClient = QPushButton(self.task_data)
        self.CallClient.setObjectName(u"CallClient")
        sizePolicy.setHeightForWidth(self.CallClient.sizePolicy().hasHeightForWidth())
        self.CallClient.setSizePolicy(sizePolicy)
        self.CallClient.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_4.addWidget(self.CallClient)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Back = QPushButton(self.task_data)
        self.Back.setObjectName(u"Back")
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setStyleSheet(u"font: 14pt \"Arial\";")

        self.horizontalLayout.addWidget(self.Back)

        self.Complete = QPushButton(self.task_data)
        self.Complete.setObjectName(u"Complete")
        sizePolicy.setHeightForWidth(self.Complete.sizePolicy().hasHeightForWidth())
        self.Complete.setSizePolicy(sizePolicy)
        self.Complete.setStyleSheet(u"font: 14pt \"Arial\";")

        self.horizontalLayout.addWidget(self.Complete)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Start = QPushButton(self.task_data)
        self.Start.setObjectName(u"Start")
        sizePolicy.setHeightForWidth(self.Start.sizePolicy().hasHeightForWidth())
        self.Start.setSizePolicy(sizePolicy)
        self.Start.setStyleSheet(u"font: 14pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.Start)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.task_data)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.AddressText.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.ShowOnMap.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u043a\u0430\u0440\u0442\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.ClientText.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.CallClient.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.Complete.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

