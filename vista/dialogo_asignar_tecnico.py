# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_asignar_tecnico.ui'
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

class Ui_Dialog_asignar_tecnico(object):
    def setupUi(self, Dialog_asignar_tecnico):
        if not Dialog_asignar_tecnico.objectName():
            Dialog_asignar_tecnico.setObjectName(u"Dialog_asignar_tecnico")
        Dialog_asignar_tecnico.resize(300, 163)
        self.formLayout = QFormLayout(Dialog_asignar_tecnico)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog_asignar_tecnico)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.asig_tec_id_reparac = QLineEdit(Dialog_asignar_tecnico)
        self.asig_tec_id_reparac.setObjectName(u"asig_tec_id_reparac")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.asig_tec_id_reparac)

        self.label_2 = QLabel(Dialog_asignar_tecnico)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.asig_tec_id_tecnico = QLineEdit(Dialog_asignar_tecnico)
        self.asig_tec_id_tecnico.setObjectName(u"asig_tec_id_tecnico")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.asig_tec_id_tecnico)

        self.buttonBox = QDialogButtonBox(Dialog_asignar_tecnico)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(Dialog_asignar_tecnico)
        self.buttonBox.accepted.connect(Dialog_asignar_tecnico.accept)
        self.buttonBox.rejected.connect(Dialog_asignar_tecnico.reject)

        QMetaObject.connectSlotsByName(Dialog_asignar_tecnico)
    # setupUi

    def retranslateUi(self, Dialog_asignar_tecnico):
        Dialog_asignar_tecnico.setWindowTitle(QCoreApplication.translate("Dialog_asignar_tecnico", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_asignar_tecnico", u"Id de la reparaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_asignar_tecnico", u"Id del t\u00e9cnico", None))
    # retranslateUi

