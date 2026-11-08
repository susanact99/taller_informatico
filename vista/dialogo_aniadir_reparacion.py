# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_aniadir_reparacion.ui'
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
    QTextEdit, QWidget)

class Ui_dialog_agregar_reparacion(object):
    def setupUi(self, dialog_agregar_reparacion):
        if not dialog_agregar_reparacion.objectName():
            dialog_agregar_reparacion.setObjectName(u"dialog_agregar_reparacion")
        dialog_agregar_reparacion.resize(441, 561)
        self.formLayout = QFormLayout(dialog_agregar_reparacion)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialog_agregar_reparacion)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.id_reparacion = QLineEdit(dialog_agregar_reparacion)
        self.id_reparacion.setObjectName(u"id_reparacion")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_reparacion)

        self.label_2 = QLabel(dialog_agregar_reparacion)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.label_2)

        self.reparacion_cliente_id = QLineEdit(dialog_agregar_reparacion)
        self.reparacion_cliente_id.setObjectName(u"reparacion_cliente_id")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.reparacion_cliente_id)

        self.label_3 = QLabel(dialog_agregar_reparacion)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.label_3)

        self.reparacion_tecnico_id = QLineEdit(dialog_agregar_reparacion)
        self.reparacion_tecnico_id.setObjectName(u"reparacion_tecnico_id")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.reparacion_tecnico_id)

        self.label_4 = QLabel(dialog_agregar_reparacion)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.label_4)

        self.reparacion_equipo = QLineEdit(dialog_agregar_reparacion)
        self.reparacion_equipo.setObjectName(u"reparacion_equipo")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.reparacion_equipo)

        self.label_7 = QLabel(dialog_agregar_reparacion)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.SpanningRole, self.label_7)

        self.reparacion_coste = QLineEdit(dialog_agregar_reparacion)
        self.reparacion_coste.setObjectName(u"reparacion_coste")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.reparacion_coste)

        self.label_6 = QLabel(dialog_agregar_reparacion)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.SpanningRole, self.label_6)

        self.reparacion_estado = QLineEdit(dialog_agregar_reparacion)
        self.reparacion_estado.setObjectName(u"reparacion_estado")

        self.formLayout.setWidget(15, QFormLayout.ItemRole.FieldRole, self.reparacion_estado)

        self.label_5 = QLabel(dialog_agregar_reparacion)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(17, QFormLayout.ItemRole.SpanningRole, self.label_5)

        self.textEdit = QTextEdit(dialog_agregar_reparacion)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(19, QFormLayout.ItemRole.FieldRole, self.textEdit)

        self.buttonBox = QDialogButtonBox(dialog_agregar_reparacion)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(20, QFormLayout.ItemRole.SpanningRole, self.buttonBox)


        self.retranslateUi(dialog_agregar_reparacion)
        self.buttonBox.accepted.connect(dialog_agregar_reparacion.accept)
        self.buttonBox.rejected.connect(dialog_agregar_reparacion.reject)

        QMetaObject.connectSlotsByName(dialog_agregar_reparacion)
    # setupUi

    def retranslateUi(self, dialog_agregar_reparacion):
        dialog_agregar_reparacion.setWindowTitle(QCoreApplication.translate("dialog_agregar_reparacion", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Cliente id", None))
        self.label_3.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Tecnico id", None))
        self.label_4.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Equipo", None))
        self.label_7.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Coste", None))
        self.label_6.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Estado", None))
        self.label_5.setText(QCoreApplication.translate("dialog_agregar_reparacion", u"Descripcion", None))
    # retranslateUi

