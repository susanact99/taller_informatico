# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_agregar_cliente.ui'
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

class Ui_dialogo_agregar_cliente(object):
    def setupUi(self, dialogo_agregar_cliente):
        if not dialogo_agregar_cliente.objectName():
            dialogo_agregar_cliente.setObjectName(u"dialogo_agregar_cliente")
        dialogo_agregar_cliente.resize(358, 216)
        self.formLayout = QFormLayout(dialogo_agregar_cliente)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialogo_agregar_cliente)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.agregar_cliente_id = QLineEdit(dialogo_agregar_cliente)
        self.agregar_cliente_id.setObjectName(u"agregar_cliente_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.agregar_cliente_id)

        self.label_2 = QLabel(dialogo_agregar_cliente)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.agregar_cliente_nombre = QLineEdit(dialogo_agregar_cliente)
        self.agregar_cliente_nombre.setObjectName(u"agregar_cliente_nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.agregar_cliente_nombre)

        self.label_3 = QLabel(dialogo_agregar_cliente)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.agregar_cliente_correo = QLineEdit(dialogo_agregar_cliente)
        self.agregar_cliente_correo.setObjectName(u"agregar_cliente_correo")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.agregar_cliente_correo)

        self.label_4 = QLabel(dialogo_agregar_cliente)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.agregar_cliente_telefono = QLineEdit(dialogo_agregar_cliente)
        self.agregar_cliente_telefono.setObjectName(u"agregar_cliente_telefono")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.agregar_cliente_telefono)

        self.buttonBox = QDialogButtonBox(dialogo_agregar_cliente)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(dialogo_agregar_cliente)
        self.buttonBox.accepted.connect(dialogo_agregar_cliente.accept)
        self.buttonBox.rejected.connect(dialogo_agregar_cliente.reject)

        QMetaObject.connectSlotsByName(dialogo_agregar_cliente)
    # setupUi

    def retranslateUi(self, dialogo_agregar_cliente):
        dialogo_agregar_cliente.setWindowTitle(QCoreApplication.translate("dialogo_agregar_cliente", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialogo_agregar_cliente", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("dialogo_agregar_cliente", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("dialogo_agregar_cliente", u"Correo", None))
        self.label_4.setText(QCoreApplication.translate("dialogo_agregar_cliente", u"Telefono", None))
    # retranslateUi

