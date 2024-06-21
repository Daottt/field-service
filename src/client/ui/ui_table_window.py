# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_table_window.ui'
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
        Form.resize(748, 460)
        Form.setStyleSheet(u"background-color: rgb(182, 182, 182);\n"
"font: 16pt \"Arial\";")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Layout_table = QVBoxLayout()
        self.Layout_table.setObjectName(u"Layout_table")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalSpacer_1 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_1)

        self.Add = QPushButton(Form)
        self.Add.setObjectName(u"Add")
        self.Add.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.Add.setFont(font)

        self.horizontalLayout_1.addWidget(self.Add)

        self.Update = QPushButton(Form)
        self.Update.setObjectName(u"Update")
        self.Update.setMinimumSize(QSize(150, 0))
        self.Update.setFont(font)

        self.horizontalLayout_1.addWidget(self.Update)

        self.Delete = QPushButton(Form)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setMinimumSize(QSize(150, 0))
        self.Delete.setFont(font)

        self.horizontalLayout_1.addWidget(self.Delete)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_2)


        self.Layout_table.addLayout(self.horizontalLayout_1)

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

        self.Layout_table.addWidget(self.Table)


        self.verticalLayout.addLayout(self.Layout_table)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Update.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

