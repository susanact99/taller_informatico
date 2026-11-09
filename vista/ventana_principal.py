# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 481)
        palette = QPalette()
        brush = QBrush(QColor(241, 245, 249, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"\n"
"/* FONDO GENERAL */\n"
"QMainWindow {\n"
"    background-color: #F1F5F9;\n"
"}\n"
"\n"
"/* PESTA\u00d1AS */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #CBD5E1;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #E2E8F0;\n"
"    color: #334155;\n"
"    padding: 12px 20px;\n"
"    margin-right: 3px;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #2563EB;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #93C5FD;\n"
"    color: #1E293B;\n"
"}\n"
"\n"
"/* BOTONES */\n"
"QPushButton {\n"
"    background-color: #1E293B;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 9px 14px;\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #334155;\n"
"}\n"
"\n"
"QPushButton:"
                        "pressed {\n"
"    background-color: #0F172A;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #94A3B8;\n"
"    color: #E2E8F0;\n"
"}\n"
"\n"
"\n"
"/* CAMPOS DE TEXTO */\n"
"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    color: #1E293B;\n"
"    border: 1px solid #CBD5E1;\n"
"    border-radius: 5px;\n"
"    padding: 7px;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QLineEdit:focus, QComboBox:focus {\n"
"    border: 2px solid #2563EB;\n"
"}\n"
"\n"
"/* TABLAS */\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    alternate-background-color: #F8FAFC;\n"
"    color: #334155;\n"
"    gridline-color: #E2E8F0;\n"
"    border: 1px solid #CBD5E1;\n"
"    border-radius: 6px;\n"
"    font-size: 9pt;\n"
"    selection-background-color: #DBEAFE;\n"
"    selection-color: #1E293B;\n"
"}\n"
"\n"
"/* CABECERAS DE TABLAS */\n"
"QHeaderView::section {\n"
"    background-color: #1E293B;\n"
"    color: white;\n"
"    padding: 9px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* E"
                        "TIQUETAS */\n"
"QLabel {\n"
"    color: #334155;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"/* BARRA DE ESTADO */\n"
"QStatusBar {\n"
"    background-color: #E2E8F0;\n"
"    color: #334155;\n"
"    border-top: 1px solid #CBD5E1;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.paginas = QTabWidget(self.centralwidget)
        self.paginas.setObjectName(u"paginas")
        self.TallerInformatico = QWidget()
        self.TallerInformatico.setObjectName(u"TallerInformatico")
        self.verticalLayout_5 = QVBoxLayout(self.TallerInformatico)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.TallerInformatico)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.TallerInformatico)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.TallerInformatico)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.TallerInformatico)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.paginas.addTab(self.TallerInformatico, "")
        self.reparaciones_tab = QWidget()
        self.reparaciones_tab.setObjectName(u"reparaciones_tab")
        self.reparaciones_tab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout = QVBoxLayout(self.reparaciones_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.reparaciones_tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.estados_filtro = QComboBox(self.reparaciones_tab)
        self.estados_filtro.addItem("")
        self.estados_filtro.addItem("")
        self.estados_filtro.addItem("")
        self.estados_filtro.addItem("")
        self.estados_filtro.setObjectName(u"estados_filtro")

        self.horizontalLayout.addWidget(self.estados_filtro)

        self.label_2 = QLabel(self.reparaciones_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.filt_cliente_id = QLineEdit(self.reparaciones_tab)
        self.filt_cliente_id.setObjectName(u"filt_cliente_id")

        self.horizontalLayout.addWidget(self.filt_cliente_id)

        self.label_3 = QLabel(self.reparaciones_tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.filt_tecnico_id = QLineEdit(self.reparaciones_tab)
        self.filt_tecnico_id.setObjectName(u"filt_tecnico_id")

        self.horizontalLayout.addWidget(self.filt_tecnico_id)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.reparaciones_tabla = QTableWidget(self.reparaciones_tab)
        self.reparaciones_tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if (self.reparaciones_tabla.columnCount() < 7):
            self.reparaciones_tabla.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.reparaciones_tabla.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.reparaciones_tabla.setObjectName(u"reparaciones_tabla")
        self.reparaciones_tabla.setAlternatingRowColors(True)
        self.reparaciones_tabla.horizontalHeader().setCascadingSectionResizes(False)
        self.reparaciones_tabla.verticalHeader().setVisible(False)
        self.reparaciones_tabla.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.reparaciones_tabla)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listar_reparaciones = QPushButton(self.reparaciones_tab)
        self.listar_reparaciones.setObjectName(u"listar_reparaciones")

        self.horizontalLayout_2.addWidget(self.listar_reparaciones)

        self.aniadir_reparacion = QPushButton(self.reparaciones_tab)
        self.aniadir_reparacion.setObjectName(u"aniadir_reparacion")
        self.aniadir_reparacion.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.aniadir_reparacion)

        self.asignar_tecnico = QPushButton(self.reparaciones_tab)
        self.asignar_tecnico.setObjectName(u"asignar_tecnico")

        self.horizontalLayout_2.addWidget(self.asignar_tecnico)

        self.modificar_coste = QPushButton(self.reparaciones_tab)
        self.modificar_coste.setObjectName(u"modificar_coste")

        self.horizontalLayout_2.addWidget(self.modificar_coste)

        self.cambiar_estado = QPushButton(self.reparaciones_tab)
        self.cambiar_estado.setObjectName(u"cambiar_estado")

        self.horizontalLayout_2.addWidget(self.cambiar_estado)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.facturacion_boton = QPushButton(self.reparaciones_tab)
        self.facturacion_boton.setObjectName(u"facturacion_boton")

        self.horizontalLayout_6.addWidget(self.facturacion_boton)

        self.estadisticas_boton = QPushButton(self.reparaciones_tab)
        self.estadisticas_boton.setObjectName(u"estadisticas_boton")

        self.horizontalLayout_6.addWidget(self.estadisticas_boton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.paginas.addTab(self.reparaciones_tab, "")
        self.clientes_tab = QWidget()
        self.clientes_tab.setObjectName(u"clientes_tab")
        self.verticalLayout_2 = QVBoxLayout(self.clientes_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.clientes_tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.nombre_client_filtro = QLineEdit(self.clientes_tab)
        self.nombre_client_filtro.setObjectName(u"nombre_client_filtro")

        self.horizontalLayout_3.addWidget(self.nombre_client_filtro)

        self.buscar_nombre_client = QPushButton(self.clientes_tab)
        self.buscar_nombre_client.setObjectName(u"buscar_nombre_client")

        self.horizontalLayout_3.addWidget(self.buscar_nombre_client)

        self.listar_clientes = QPushButton(self.clientes_tab)
        self.listar_clientes.setObjectName(u"listar_clientes")

        self.horizontalLayout_3.addWidget(self.listar_clientes)

        self.aniadir_cliente = QPushButton(self.clientes_tab)
        self.aniadir_cliente.setObjectName(u"aniadir_cliente")

        self.horizontalLayout_3.addWidget(self.aniadir_cliente)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabla_clientes = QTableWidget(self.clientes_tab)
        self.tabla_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if (self.tabla_clientes.columnCount() < 4):
            self.tabla_clientes.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tabla_clientes.setObjectName(u"tabla_clientes")
        self.tabla_clientes.setTabKeyNavigation(True)
        self.tabla_clientes.verticalHeader().setVisible(False)
        self.tabla_clientes.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.tabla_clientes)

        self.paginas.addTab(self.clientes_tab, "")
        self.tecnicos_tab = QWidget()
        self.tecnicos_tab.setObjectName(u"tecnicos_tab")
        self.verticalLayout_3 = QVBoxLayout(self.tecnicos_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.tecnicos_tab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.input_busc_nom_tec = QLineEdit(self.tecnicos_tab)
        self.input_busc_nom_tec.setObjectName(u"input_busc_nom_tec")

        self.horizontalLayout_4.addWidget(self.input_busc_nom_tec)

        self.buscar_tec_nombre = QPushButton(self.tecnicos_tab)
        self.buscar_tec_nombre.setObjectName(u"buscar_tec_nombre")

        self.horizontalLayout_4.addWidget(self.buscar_tec_nombre)

        self.agregar_tecnico = QPushButton(self.tecnicos_tab)
        self.agregar_tecnico.setObjectName(u"agregar_tecnico")

        self.horizontalLayout_4.addWidget(self.agregar_tecnico)

        self.listar_tecnicos = QPushButton(self.tecnicos_tab)
        self.listar_tecnicos.setObjectName(u"listar_tecnicos")

        self.horizontalLayout_4.addWidget(self.listar_tecnicos)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabla_tecnicos = QTableWidget(self.tecnicos_tab)
        self.tabla_tecnicos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if (self.tabla_tecnicos.columnCount() < 3):
            self.tabla_tecnicos.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_tecnicos.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_tecnicos.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_tecnicos.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.tabla_tecnicos.setObjectName(u"tabla_tecnicos")
        self.tabla_tecnicos.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tabla_tecnicos)

        self.paginas.addTab(self.tecnicos_tab, "")

        self.verticalLayout_4.addWidget(self.paginas)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.paginas.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#000000;\">Gesti\u00f3n del Taller</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">\U0001f5a8</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">\U0001f4bb</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">\u2328</span></p></body></html>", None))
        self.paginas.setTabText(self.paginas.indexOf(self.TallerInformatico), QCoreApplication.translate("MainWindow", u"Taller\U0001f4bb", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filtrar por estados", None))
        self.estados_filtro.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.estados_filtro.setItemText(1, QCoreApplication.translate("MainWindow", u"pendiente", None))
        self.estados_filtro.setItemText(2, QCoreApplication.translate("MainWindow", u"en proceso", None))
        self.estados_filtro.setItemText(3, QCoreApplication.translate("MainWindow", u"finalizada", None))

        self.estados_filtro.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filtrar por id_cliente:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filtrar por id_tecnico:", None))
        ___qtablewidgetitem = self.reparaciones_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem1 = self.reparaciones_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"cliente_id", None))
        ___qtablewidgetitem2 = self.reparaciones_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"tecnico_id", None))
        ___qtablewidgetitem3 = self.reparaciones_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"equipo", None))
        ___qtablewidgetitem4 = self.reparaciones_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"descripcion", None))
        ___qtablewidgetitem5 = self.reparaciones_tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"estado", None))
        ___qtablewidgetitem6 = self.reparaciones_tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"coste", None))
        self.listar_reparaciones.setText(QCoreApplication.translate("MainWindow", u"Listar reparaciones", None))
        self.aniadir_reparacion.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir reparaci\u00f3n", None))
        self.asignar_tecnico.setText(QCoreApplication.translate("MainWindow", u"Asignar t\u00e9cnico", None))
        self.modificar_coste.setText(QCoreApplication.translate("MainWindow", u"Modificar coste", None))
        self.cambiar_estado.setText(QCoreApplication.translate("MainWindow", u"Cambiar estado", None))
        self.facturacion_boton.setText(QCoreApplication.translate("MainWindow", u"Facturaci\u00f3n", None))
        self.estadisticas_boton.setText(QCoreApplication.translate("MainWindow", u"Estad\u00edsticas", None))
        self.paginas.setTabText(self.paginas.indexOf(self.reparaciones_tab), QCoreApplication.translate("MainWindow", u"Reparaciones \U0001f6e0", None))
#if QT_CONFIG(tooltip)
        self.clientes_tab.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Clientes</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.buscar_nombre_client.setText(QCoreApplication.translate("MainWindow", u"Buscar \U0001f50d", None))
        self.listar_clientes.setText(QCoreApplication.translate("MainWindow", u"Listar clientes", None))
        self.aniadir_cliente.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir cliente", None))
        ___qtablewidgetitem7 = self.tabla_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem8 = self.tabla_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"nombre", None))
        ___qtablewidgetitem9 = self.tabla_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"correo", None))
        ___qtablewidgetitem10 = self.tabla_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"telefono", None))
        self.paginas.setTabText(self.paginas.indexOf(self.clientes_tab), QCoreApplication.translate("MainWindow", u"Clientes \U0001f64d\U0001f3fb\U0000200d\U00002642\U0000fe0f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.buscar_tec_nombre.setText(QCoreApplication.translate("MainWindow", u"Buscar \U0001f50d", None))
        self.agregar_tecnico.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir t\u00e9cnico", None))
        self.listar_tecnicos.setText(QCoreApplication.translate("MainWindow", u"Listar t\u00e9cnicos", None))
        ___qtablewidgetitem11 = self.tabla_tecnicos.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem12 = self.tabla_tecnicos.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"nombre", None))
        ___qtablewidgetitem13 = self.tabla_tecnicos.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"especialidad", None))
        self.paginas.setTabText(self.paginas.indexOf(self.tecnicos_tab), QCoreApplication.translate("MainWindow", u"T\U000000e9cnicos \U0001f477\U0001f3fb\U0000200d\U00002642\U0000fe0f", None))
    # retranslateUi

