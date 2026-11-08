# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_modificar_coste.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_dialogo_modificar_coste(object):
    def setupUi(self, dialogo_modificar_coste):
        if not dialogo_modificar_coste.objectName():
            dialogo_modificar_coste.setObjectName(u"dialogo_modificar_coste")
        dialogo_modificar_coste.resize(318, 172)
        self.formLayout = QFormLayout(dialogo_modificar_coste)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialogo_modificar_coste)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.mod_coste = QLineEdit(dialogo_modificar_coste)
        self.mod_coste.setObjectName(u"mod_coste")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.mod_coste)

        self.label_2 = QLabel(dialogo_modificar_coste)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(dialogo_modificar_coste)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.buttonBox = QDialogButtonBox(dialogo_modificar_coste)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(dialogo_modificar_coste)
        self.buttonBox.accepted.connect(dialogo_modificar_coste.accept)
        self.buttonBox.rejected.connect(dialogo_modificar_coste.reject)

        QMetaObject.connectSlotsByName(dialogo_modificar_coste)
    # setupUi

    def retranslateUi(self, dialogo_modificar_coste):
        dialogo_modificar_coste.setWindowTitle(QCoreApplication.translate("dialogo_modificar_coste", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialogo_modificar_coste", u"Id de la reparacion", None))
        self.label_2.setText(QCoreApplication.translate("dialogo_modificar_coste", u"Nuevo coste", None))
    # retranslateUi

