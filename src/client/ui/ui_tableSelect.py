# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tableSelect.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(888, 300)
        Form.setStyleSheet(u"background-color: rgb(182, 182, 182);\n"
"font: 16pt \"Arial\";")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Select = QPushButton(Form)
        self.Select.setObjectName(u"Select")
        self.Select.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.Select.setFont(font)

        self.horizontalLayout.addWidget(self.Select)

        self.Add = QPushButton(Form)
        self.Add.setObjectName(u"Add")
        self.Add.setMinimumSize(QSize(150, 0))
        self.Add.setFont(font)

        self.horizontalLayout.addWidget(self.Add)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Table = QTableWidget(Form)
        self.Table.setObjectName(u"Table")
        self.Table.setFont(font)
        self.Table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.Table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.Table.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.Table.horizontalHeader().setVisible(True)
        self.Table.horizontalHeader().setMinimumSectionSize(60)
        self.Table.horizontalHeader().setDefaultSectionSize(200)
        self.Table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.Table)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Select.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.Add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

