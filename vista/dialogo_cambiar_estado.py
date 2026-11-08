# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_cambiar_estado.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_dialogo_cambiar_estado(object):
    def setupUi(self, dialogo_cambiar_estado):
        if not dialogo_cambiar_estado.objectName():
            dialogo_cambiar_estado.setObjectName(u"dialogo_cambiar_estado")
        dialogo_cambiar_estado.resize(303, 185)
        self.formLayout = QFormLayout(dialogo_cambiar_estado)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialogo_cambiar_estado)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.camb_estado_id_reparacion = QLineEdit(dialogo_cambiar_estado)
        self.camb_estado_id_reparacion.setObjectName(u"camb_estado_id_reparacion")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.camb_estado_id_reparacion)

        self.label_2 = QLabel(dialogo_cambiar_estado)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.buttonBox = QDialogButtonBox(dialogo_cambiar_estado)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.cambiar_estado_combo_box = QComboBox(dialogo_cambiar_estado)
        self.cambiar_estado_combo_box.addItem("")
        self.cambiar_estado_combo_box.addItem("")
        self.cambiar_estado_combo_box.addItem("")
        self.cambiar_estado_combo_box.addItem("")
        self.cambiar_estado_combo_box.setObjectName(u"cambiar_estado_combo_box")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cambiar_estado_combo_box)


        self.retranslateUi(dialogo_cambiar_estado)
        self.buttonBox.accepted.connect(dialogo_cambiar_estado.accept)
        self.buttonBox.rejected.connect(dialogo_cambiar_estado.reject)

        QMetaObject.connectSlotsByName(dialogo_cambiar_estado)
    # setupUi

    def retranslateUi(self, dialogo_cambiar_estado):
        dialogo_cambiar_estado.setWindowTitle(QCoreApplication.translate("dialogo_cambiar_estado", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialogo_cambiar_estado", u"Id reparaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("dialogo_cambiar_estado", u"Nuevo estado", None))
        self.cambiar_estado_combo_box.setItemText(0, QCoreApplication.translate("dialogo_cambiar_estado", u"Nuevo elemento", None))
        self.cambiar_estado_combo_box.setItemText(1, QCoreApplication.translate("dialogo_cambiar_estado", u"pendiente", None))
        self.cambiar_estado_combo_box.setItemText(2, QCoreApplication.translate("dialogo_cambiar_estado", u"en proceso", None))
        self.cambiar_estado_combo_box.setItemText(3, QCoreApplication.translate("dialogo_cambiar_estado", u"finalizada", None))

    # retranslateUi

