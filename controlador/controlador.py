import sys
from PySide6.QtWidgets import (QMainWindow,QTableWidgetItem,
QDialog,QMessageBox,QApplication)
from PySide6.QtWidgets import QMessageBox
from vista.dialogo_asignar_tecnico import Ui_Dialog_asignar_tecnico
from vista.dialogo_modificar_coste import Ui_dialogo_modificar_coste
from vista.dialogo_aniadir_reparacion import Ui_dialog_agregar_reparacion
from vista.dialogo_cambiar_estado import Ui_dialogo_cambiar_estado
from vista.dialogo_agregar_cliente import Ui_dialogo_agregar_cliente
from vista.dialogo_agregar_tecnico import Ui_dialogo_agregar_tecnico
from vista.ventana_principal import Ui_MainWindow
from modelos.cliente import Cliente
from modelos.tecnico import Tecnico
from modelos.reparacion import Reparacion
from persistencia import actualizar_taller, guardar_taller


class Controlador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.taller = actualizar_taller()
        self.conectar_eventos()

    def conectar_eventos(self):
        self.ui.aniadir_reparacion.clicked.connect(self.abrir_dialogo_reparacion)
        self.ui.listar_reparaciones.clicked.connect(self.listar_todas_reparaciones)
        self.ui.asignar_tecnico.clicked.connect(self.abrir_dialogo_asignar_tecnico)
        self.ui.modificar_coste.clicked.connect(self.abrir_dialogo_modificar_coste)
        self.ui.cambiar_estado.clicked.connect(self.abrir_dialogo_cambiar_estado)
        self.ui.estados_filtro.currentTextChanged.connect(self.filtrar_reparaciones_estado)
        self.ui.listar_clientes.clicked.connect(self.listar_todos_clientes)
        self.ui.aniadir_cliente.clicked.connect(self.abrir_dialogo_agregar_cliente)
        self.ui.buscar_nombre_client.clicked.connect(self.buscar_cliente_nombre)
        self.ui.buscar_tec_nombre.clicked.connect(self.buscar_tecnico_nombre)
        self.ui.listar_tecnicos.clicked.connect(self.listar_todos_tecnicos)
        self.ui.agregar_tecnico.clicked.connect(self.abrir_dialogo_agregar_tecnico)
        self.ui.filt_cliente_id.textChanged.connect(self.filtrar_reparaciones_cliente_id)
        self.ui.filt_tecnico_id.textChanged.connect(self.filtrar_reparaciones_tecnico_id)
        self.ui.facturacion_boton.clicked.connect(self.mostrar_facturacion)
        self.ui.estadisticas_boton.clicked.connect(self.mostrar_estadisticas)

    def filtrar_reparaciones_tecnico_id(self):
        self.ui.filt_cliente_id.setText("")
        self.ui.estados_filtro.setCurrentIndex(0)
        id_seleccionado = self.ui.filt_tecnico_id.text()
        reparaciones_filtradas = []
        reparaciones = self.taller.listar_reparaciones()

        for reparacion in reparaciones:
            if id_seleccionado == str(reparacion.tecnico.id):
                reparaciones_filtradas.append(reparacion)

        self.ui.reparaciones_tabla.setRowCount(len(reparaciones_filtradas))
        for fila, reparacion in enumerate(reparaciones_filtradas):
            self.ui.reparaciones_tabla.setItem(fila, 0, QTableWidgetItem(str(reparacion.id)))
            self.ui.reparaciones_tabla.setItem(fila, 1, QTableWidgetItem(reparacion.cliente.id))
            self.ui.reparaciones_tabla.setItem(fila, 2, QTableWidgetItem(reparacion.tecnico.id))
            self.ui.reparaciones_tabla.setItem(fila, 3, QTableWidgetItem(reparacion.equipo))
            self.ui.reparaciones_tabla.setItem(fila, 4, QTableWidgetItem(reparacion.descripcion))
            self.ui.reparaciones_tabla.setItem(fila, 5, QTableWidgetItem(reparacion.estado))
            self.ui.reparaciones_tabla.setItem(fila, 6, QTableWidgetItem(reparacion.coste))

    def filtrar_reparaciones_cliente_id(self):
        id_seleccionado = self.ui.filt_cliente_id.text()
        reparaciones_filtradas = []
        reparaciones = self.taller.listar_reparaciones()
        self.ui.filt_tecnico_id.setText("")
        self.ui.estados_filtro.setCurrentIndex(0)

        for reparacion in reparaciones:
            if id_seleccionado == str(reparacion.cliente.id):
                reparaciones_filtradas.append(reparacion)

        self.ui.reparaciones_tabla.setRowCount(len(reparaciones_filtradas))
        for fila, reparacion in enumerate(reparaciones_filtradas):
            self.ui.reparaciones_tabla.setItem(fila,0,QTableWidgetItem(str(reparacion.id)))
            self.ui.reparaciones_tabla.setItem(fila,1,QTableWidgetItem(reparacion.cliente.id))
            self.ui.reparaciones_tabla.setItem(fila, 2, QTableWidgetItem(reparacion.tecnico.id))
            self.ui.reparaciones_tabla.setItem(fila,3,QTableWidgetItem(reparacion.equipo))
            self.ui.reparaciones_tabla.setItem(fila, 4, QTableWidgetItem(reparacion.descripcion))
            self.ui.reparaciones_tabla.setItem(fila, 5, QTableWidgetItem(reparacion.estado))
            self.ui.reparaciones_tabla.setItem(fila, 6, QTableWidgetItem(reparacion.coste))

    def abrir_dialogo_reparacion(self):
        dialogo = QDialog(self)
        ui = Ui_dialog_agregar_reparacion()
        ui.setupUi(dialogo)

        reparaciones = self.taller.listar_reparaciones()
        ids = []

        for reparacion in reparaciones:
            try:
                ids.append(int(reparacion.id))
            except ValueError:
                pass

        if len(ids) > 0:
            nuevo_id = max(ids) + 1
        else:
            nuevo_id = 1

        ui.id_reparacion.setText(str(nuevo_id))

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:
            id_reparacion = ui.id_reparacion.text().strip()
            id_cliente = ui.reparacion_cliente_id.text().strip()
            id_tecnico = ui.reparacion_tecnico_id.text().strip()
            equipo = ui.reparacion_equipo.text().strip()
            coste_texto = ui.reparacion_coste.text().strip()
            estado = ui.reparacion_estado.text().strip()
            descripcion = ui.textEdit.toPlainText().strip()

            if (
                    id_reparacion == ""
                    or id_cliente == ""
                    or equipo == ""
                    or coste_texto == ""
                    or descripcion == ""
            ):
                QMessageBox.warning(self,"Error",
                    "Debes rellenar los campos obligatorios.")
                return

            cliente_encontrado = None

            for cliente in self.taller.clientes:
                if str(cliente.id) == id_cliente:
                    cliente_encontrado = cliente
                    break

            # Comprobar si existe el cliente
            if cliente_encontrado is None:
                QMessageBox.warning(self,"Error",
                    "No existe ningún cliente con ese ID.")
                return

            # Buscar el técnico por su ID
            tecnico_encontrado = None

            if id_tecnico != "":
                for tecnico in self.taller.tecnicos:
                    if str(tecnico.id) == id_tecnico:
                        tecnico_encontrado = tecnico
                        break

                # Comprobar si existe el técnico
                if tecnico_encontrado is None:
                    QMessageBox.warning(self,"Error",
                                        "No existe ningún técnico con ese ID.")
                    return

            try:
                coste = float(coste_texto.replace(",", "."))
            except ValueError:
                QMessageBox.warning(self,"Error","El coste debe ser un número.")
                return

            if estado == "":
                estado = "pendiente"

            reparacion = Reparacion(id_reparacion,cliente_encontrado,
                equipo,descripcion,tecnico_encontrado,estado,coste)

            self.taller.alta_reparacion(reparacion)

            guardar_taller(self.taller)

            QMessageBox.information(self,"Reparación añadida",
                                    "La reparación se ha añadido correctamente.")

            self.listar_todas_reparaciones()

    def listar_todas_reparaciones(self):
        reparaciones = self.taller.listar_reparaciones()
        tabla = self.ui.reparaciones_tabla
        tabla.setRowCount(len(reparaciones))

        for fila, reparacion in enumerate(reparaciones):
            cliente_id = reparacion.cliente.id
            if reparacion.tecnico is not None:
                tecnico_id = reparacion.tecnico.id
            else:
                tecnico_id = ""

            coste = reparacion.coste

            tabla.setItem(fila, 0,QTableWidgetItem(str(reparacion.id)))
            tabla.setItem(fila, 1,QTableWidgetItem(str(cliente_id)))
            tabla.setItem(fila, 2,QTableWidgetItem(str(tecnico_id)))
            tabla.setItem(fila, 3,QTableWidgetItem(reparacion.equipo))
            tabla.setItem(fila, 4,QTableWidgetItem(reparacion.descripcion))
            tabla.setItem(fila, 5,QTableWidgetItem(reparacion.estado))
            tabla.setItem(fila, 6,QTableWidgetItem(str(coste)))

    def abrir_dialogo_asignar_tecnico(self):
        dialogo = QDialog(self)
        ui = Ui_Dialog_asignar_tecnico()
        ui.setupUi(dialogo)

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:
            id_reparacion = ui.asig_tec_id_reparac.text().strip()
            id_tecnico = ui.asig_tec_id_tecnico.text().strip()

            if id_reparacion == "" or id_tecnico == "":
                QMessageBox.warning(
                    self,"Error","Debes rellenar los dos campos.")
                return

            reparacion_encontrada = None

            for reparacion in self.taller.listar_reparaciones():
                if str(reparacion.id) == id_reparacion:
                    reparacion_encontrada = reparacion
                    break

            if reparacion_encontrada is None:
                QMessageBox.warning(self,"Error","No existe ninguna reparación con ese ID.")
                return

            tecnico_encontrado = None

            for tecnico in self.taller.tecnicos:
                if str(tecnico.id) == id_tecnico:
                    tecnico_encontrado = tecnico
                    break

            if tecnico_encontrado is None:
                QMessageBox.warning(self,"Error","No existe ningún técnico con ese ID.")
                return

            reparacion_encontrada.tecnico = tecnico_encontrado

            guardar_taller(self.taller)

            QMessageBox.information(self,"Técnico asignado",
                "El técnico se ha asignado correctamente.")

            self.listar_todas_reparaciones()

    def abrir_dialogo_modificar_coste(self):
        dialogo = QDialog(self)
        ui = Ui_dialogo_modificar_coste()
        ui.setupUi(dialogo)

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:

            id_reparacion = ui.mod_coste.text().strip()
            nuevo_coste_texto = ui.lineEdit_2.text().strip()

            if id_reparacion == "" or nuevo_coste_texto == "":
                QMessageBox.warning(self,"Error",
                                    "Debes rellenar los dos campos.")
                return

            reparacion_encontrada = None

            for reparacion in self.taller.listar_reparaciones():
                if str(reparacion.id) == id_reparacion:
                    reparacion_encontrada = reparacion
                    break

            if reparacion_encontrada is None:
                QMessageBox.warning(self,"Error",
                    "No existe ninguna reparación con ese ID.")
                return

            try:
                nuevo_coste = float(nuevo_coste_texto.replace(",", "."))

                if nuevo_coste < 0:
                    QMessageBox.warning(
                        self,
                        "Error",
                        "El coste no puede ser negativo."
                    )
                    return

            except ValueError:
                QMessageBox.warning(self,"Error",
                    "El coste debe ser un número válido.")
                return

            reparacion_encontrada.coste = nuevo_coste

            guardar_taller(self.taller)

            QMessageBox.information(self,"Coste modificado",
                "El coste se ha modificado correctamente.")

            self.listar_todas_reparaciones()

    def abrir_dialogo_cambiar_estado(self):
        dialogo = QDialog(self)
        ui = Ui_dialogo_cambiar_estado()
        ui.setupUi(dialogo)

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:
            id_reparacion = ui.camb_estado_id_reparacion.text().strip()
            nuevo_estado = ui.cambiar_estado_combo_box.currentText()

            if id_reparacion == "":
                QMessageBox.warning(self,"Error",
                    "Debes introducir el ID de la reparación.")
                return

            if nuevo_estado == "" or nuevo_estado == "Nuevo elemento":
                QMessageBox.warning(self,"Error",
                    "Debes seleccionar un estado válido.")
                return

            reparacion_encontrada = None
            for reparacion in self.taller.listar_reparaciones():
                if str(reparacion.id) == id_reparacion:
                    reparacion_encontrada = reparacion
                    break

            if reparacion_encontrada is None:
                QMessageBox.warning(self,"Error",
                                    "No existe ninguna reparación con ese ID.")
                return

            reparacion_encontrada.estado = nuevo_estado

            guardar_taller(self.taller)

            QMessageBox.information(self,
                "Estado modificado",
                                    "El estado se ha cambiado correctamente.")

            self.listar_todas_reparaciones()

    def filtrar_reparaciones_estado(self):
        estado_seleccionado = self.ui.estados_filtro.currentText()
        reparaciones = self.taller.listar_reparaciones()
        self.ui.filt_cliente_id.setText("")
        self.ui.filt_tecnico_id.setText("")

        reparaciones_filtradas = []

        for reparacion in reparaciones:
            if reparacion.estado == estado_seleccionado:
                reparaciones_filtradas.append(reparacion)

        self.ui.reparaciones_tabla.setRowCount(len(reparaciones_filtradas))
        for fila, reparacion in enumerate(reparaciones_filtradas):
            self.ui.reparaciones_tabla.setItem(fila, 0, QTableWidgetItem(str(reparacion.id)))
            self.ui.reparaciones_tabla.setItem(fila, 1, QTableWidgetItem(reparacion.cliente.id))
            self.ui.reparaciones_tabla.setItem(fila, 2, QTableWidgetItem(reparacion.tecnico.id))
            self.ui.reparaciones_tabla.setItem(fila, 3, QTableWidgetItem(reparacion.equipo))
            self.ui.reparaciones_tabla.setItem(fila, 4, QTableWidgetItem(reparacion.descripcion))
            self.ui.reparaciones_tabla.setItem(fila, 5, QTableWidgetItem(reparacion.estado))
            self.ui.reparaciones_tabla.setItem(fila, 6, QTableWidgetItem(reparacion.coste))

    def listar_todos_clientes(self):
        clientes = self.taller.listar_clientes()
        tabla = self.ui.tabla_clientes

        tabla.setRowCount(len(clientes))

        for fila, cliente in enumerate(clientes):
            tabla.setItem(fila, 0,QTableWidgetItem(str(cliente.id)))
            tabla.setItem(fila, 1,QTableWidgetItem(cliente.nombre))
            tabla.setItem(fila, 2,QTableWidgetItem(cliente.correo))
            tabla.setItem(fila, 3,QTableWidgetItem(cliente.telefono))

    def abrir_dialogo_agregar_cliente(self):
        dialogo = QDialog(self)
        ui = Ui_dialogo_agregar_cliente()
        ui.setupUi(dialogo)

        clientes = self.taller.listar_clientes()

        ids = []
        for cliente in clientes:
            try:
                ids.append(int(cliente.id))
            except ValueError:
                pass

        if len(ids) > 0:
            nuevo_id = max(ids) + 1
        else:
            nuevo_id = 1

        ui.agregar_cliente_id.setText(str(nuevo_id))

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:
            id_cliente = ui.agregar_cliente_id.text().strip()
            nombre = ui.agregar_cliente_nombre.text().strip()
            correo = ui.agregar_cliente_correo.text().strip()
            telefono = ui.agregar_cliente_telefono.text().strip()
            if (
                    id_cliente == ""
                    or nombre == ""
                    or correo == ""
                    or telefono == ""
            ):
                QMessageBox.warning(self,"Error",
                    "Debes rellenar todos los campos.")
                return

            try:
                id_cliente = int(id_cliente)
            except ValueError:
                QMessageBox.warning(self,"Error",
                    "El ID debe ser un número entero.")
                return

            for cliente in self.taller.listar_clientes():
                if cliente.id == id_cliente:
                    QMessageBox.warning(self,"Error",
                        "Ya existe un cliente con ese ID.")
                    return

            cliente = Cliente(id_cliente,nombre,correo,telefono)

            self.taller.alta_cliente(cliente)

            guardar_taller(self.taller)

            QMessageBox.information(self,"Cliente añadido",
                "El cliente se ha añadido correctamente.")

            self.listar_todos_clientes()

    def buscar_cliente_nombre(self):
        nombre_buscar = self.ui.nombre_client_filtro.text().strip().lower()

        if nombre_buscar == "":
            QMessageBox.warning(self,"Error",
                "Debes introducir un nombre para buscar.")
            return

        clientes = self.taller.listar_clientes()
        clientes_encontrados = []

        for cliente in clientes:
            if nombre_buscar in cliente.nombre.lower():
                clientes_encontrados.append(cliente)

        tabla = self.ui.tabla_clientes
        tabla.setRowCount(len(clientes_encontrados))

        for fila, cliente in enumerate(clientes_encontrados):
            tabla.setItem(fila, 0,QTableWidgetItem(str(cliente.id)))
            tabla.setItem(fila, 1,QTableWidgetItem(cliente.nombre))
            tabla.setItem(fila, 2,QTableWidgetItem(cliente.correo))
            tabla.setItem(fila, 3,QTableWidgetItem(cliente.telefono))

        if len(clientes_encontrados) == 0:
            QMessageBox.information(self,"Búsqueda",
                                    "No se encontraron clientes con ese nombre.")

    def listar_todos_tecnicos(self):
        tecnicos = self.taller.listar_tecnicos()
        tabla = self.ui.tabla_tecnicos

        tabla.setRowCount(len(tecnicos))
        for fila, tecnico in enumerate(tecnicos):
            tabla.setItem(fila, 0,QTableWidgetItem(str(tecnico.id)))
            tabla.setItem(fila, 1,QTableWidgetItem(tecnico.nombre))
            tabla.setItem(fila, 2,QTableWidgetItem(tecnico.especialidad))

    def buscar_tecnico_nombre(self):
        nombre_buscar = self.ui.input_busc_nom_tec.text().strip().lower()
        if nombre_buscar == "":
            QMessageBox.warning(self,"Error",
                "Debes introducir un nombre para buscar.")
            return

        tecnicos = self.taller.listar_tecnicos()

        tecnicos_encontrados = []

        for tecnico in tecnicos:
            if nombre_buscar in tecnico.nombre.lower():
                tecnicos_encontrados.append(tecnico)

        tabla = self.ui.tabla_tecnicos

        tabla.setRowCount(len(tecnicos_encontrados))

        for fila, tecnico in enumerate(tecnicos_encontrados):
            tabla.setItem(fila, 0,QTableWidgetItem(str(tecnico.id)))
            tabla.setItem(fila, 1,QTableWidgetItem(tecnico.nombre))
            tabla.setItem(fila, 2,QTableWidgetItem(tecnico.especialidad))

        if len(tecnicos_encontrados) == 0:
            QMessageBox.information(self,"Búsqueda",
                "No se encontraron técnicos con ese nombre.")

    def abrir_dialogo_agregar_tecnico(self):
        dialogo = QDialog(self)
        ui = Ui_dialogo_agregar_tecnico()
        ui.setupUi(dialogo)

        tecnicos = self.taller.listar_tecnicos()

        ids = []

        for tecnico in tecnicos:
            try:
                ids.append(int(tecnico.id))
            except ValueError:
                pass

        if len(ids) > 0:
            nuevo_id = max(ids) + 1
        else:
            nuevo_id = 1

        ui.agregar_tec_id.setText(str(nuevo_id))

        resultado = dialogo.exec()

        if resultado == QDialog.DialogCode.Accepted:
            id_tecnico = ui.agregar_tec_id.text().strip()
            nombre = ui.agregar_tec_nombre.text().strip()
            especialidad = ui.agregar_tec_especialidad.text().strip()

            if id_tecnico == "" or nombre == "" or especialidad == "":
                QMessageBox.warning(self,"Error",
                    "Debes rellenar todos los campos.")
                return

            for tecnico in self.taller.listar_tecnicos():
                if str(tecnico.id) == id_tecnico:
                    QMessageBox.warning(self,
                        "Error","Ya existe un técnico con ese ID.")
                    return

            tecnico = Tecnico(id_tecnico,nombre,especialidad)

            try:
                self.taller.alta_tecnico(tecnico)

            except ValueError:
                QMessageBox.warning(self,"Error",
                                    "El técnico ya existe.")
                return

            guardar_taller(self.taller)

            QMessageBox.information(
                self,"Técnico añadido",
                "El técnico se ha añadido correctamente.")

            self.listar_todos_tecnicos()

def main():
    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()