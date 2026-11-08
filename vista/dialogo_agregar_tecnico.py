# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_agregar_tecnico.ui'
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

class Ui_dialogo_agregar_tecnico(object):
    def setupUi(self, dialogo_agregar_tecnico):
        if not dialogo_agregar_tecnico.objectName():
            dialogo_agregar_tecnico.setObjectName(u"dialogo_agregar_tecnico")
        dialogo_agregar_tecnico.resize(289, 144)
        self.formLayout = QFormLayout(dialogo_agregar_tecnico)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialogo_agregar_tecnico)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.agregar_tec_id = QLineEdit(dialogo_agregar_tecnico)
        self.agregar_tec_id.setObjectName(u"agregar_tec_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.agregar_tec_id)

        self.buttonBox = QDialogButtonBox(dialogo_agregar_tecnico)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.buttonBox)

        self.agregar_tec_nombre = QLineEdit(dialogo_agregar_tecnico)
        self.agregar_tec_nombre.setObjectName(u"agregar_tec_nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.agregar_tec_nombre)

        self.label_2 = QLabel(dialogo_agregar_tecnico)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(dialogo_agregar_tecnico)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.agregar_tec_especialidad = QLineEdit(dialogo_agregar_tecnico)
        self.agregar_tec_especialidad.setObjectName(u"agregar_tec_especialidad")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.agregar_tec_especialidad)


        self.retranslateUi(dialogo_agregar_tecnico)
        self.buttonBox.accepted.connect(dialogo_agregar_tecnico.accept)
        self.buttonBox.rejected.connect(dialogo_agregar_tecnico.reject)

        QMetaObject.connectSlotsByName(dialogo_agregar_tecnico)
    # setupUi

    def retranslateUi(self, dialogo_agregar_tecnico):
        dialogo_agregar_tecnico.setWindowTitle(QCoreApplication.translate("dialogo_agregar_tecnico", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialogo_agregar_tecnico", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("dialogo_agregar_tecnico", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("dialogo_agregar_tecnico", u"Especialidad", None))
    # retranslateUi

