# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mobile_task_data.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(179, 136)
        Form.setStyleSheet(u"background-color: rgb(142, 142, 142);\n"
"font: 16pt \"Arial\";")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TaskTime = QLabel(Form)
        self.TaskTime.setObjectName(u"TaskTime")
        self.TaskTime.setStyleSheet(u"font: 12pt \"Arial\";")

        self.horizontalLayout.addWidget(self.TaskTime)

        self.Status = QLabel(Form)
        self.Status.setObjectName(u"Status")

        self.horizontalLayout.addWidget(self.Status)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TaskType = QLabel(Form)
        self.TaskType.setObjectName(u"TaskType")

        self.horizontalLayout_2.addWidget(self.TaskType)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Address = QLabel(Form)
        self.Address.setObjectName(u"Address")
        self.Address.setStyleSheet(u"font: 12pt \"Arial\";")

        self.horizontalLayout_3.addWidget(self.Address)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TaskTime.setText(QCoreApplication.translate("Form", u"10:10 - 12:12", None))
        self.Status.setText(QCoreApplication.translate("Form", u"Status", None))
        self.TaskType.setText(QCoreApplication.translate("Form", u"TaskType", None))
        self.Address.setText(QCoreApplication.translate("Form", u"Address", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

