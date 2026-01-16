# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(466, 368)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.startkey = QLineEdit(Form)
        self.startkey.setObjectName(u"startkey")

        self.verticalLayout.addWidget(self.startkey)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.stopkey = QLineEdit(Form)
        self.stopkey.setObjectName(u"stopkey")

        self.verticalLayout_2.addWidget(self.stopkey)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.enter = QPushButton(Form)
        self.enter.setObjectName(u"enter")

        self.verticalLayout_3.addWidget(self.enter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.cps = QLineEdit(Form)
        self.cps.setObjectName(u"cps")

        self.horizontalLayout_2.addWidget(self.cps)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start = QPushButton(Form)
        self.start.setObjectName(u"start")

        self.horizontalLayout.addWidget(self.start)

        self.stop = QPushButton(Form)
        self.stop.setObjectName(u"stop")

        self.horizontalLayout.addWidget(self.stop)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(3, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Auto Clicker", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"    QWidget {\n"
"        background-color: #181818;\n"
"        color: #f2f2f2;\n"
"        font-size: 13px;\n"
"    }\n"
"\n"
"    QLabel {\n"
"        color: #ffb366;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QLineEdit {\n"
"        background-color: #1f1f1f;\n"
"        border: 2px solid #ff8c1a;\n"
"        border-radius: 8px;\n"
"        padding: 6px;\n"
"        color: #ffffff;\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        border-color: #ffa94d;\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        border-color: #ff6f00;\n"
"        background-color: #242424;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #ff8c1a;\n"
"        color: #1a1a1a;\n"
"        border: none;\n"
"        border-radius: 12px;\n"
"        padding: 10px 18px;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #ffa94d;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #e67300;\n"
"    "
                        "}\n"
"   ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<p align=\"center\">\uc2dc\uc791 \ud0a4</p>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<p align=\"center\">\ub05d \ud0a4</p>", None))
        self.enter.setText(QCoreApplication.translate("Form", u"\uc801\uc6a9", None))
        self.label.setText(QCoreApplication.translate("Form", u"CPS (\ucd08\ub2f9 \ud074\ub9ad\uc218)", None))
        self.start.setText(QCoreApplication.translate("Form", u"\u25b6 \uc2dc\uc791", None))
        self.stop.setText(QCoreApplication.translate("Form", u"\u25a0 \uc815\uc9c0", None))
    # retranslateUi

