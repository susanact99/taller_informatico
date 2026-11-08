import sys
from PySide6.QtWidgets import (QMainWindow,QTableWidgetItem,
QDialog,QMessageBox,QApplication)
from vista.dialogo_asignar_tecnico import Ui_Dialog_asignar_tecnico
from vista.dialogo_modificar_coste import Ui_dialogo_modificar_coste
from vista.dialogo_aniadir_reparacion import Ui_dialog_agregar_reparacion
from vista.dialogo_cambiar_estado import Ui_dialogo_cambiar_estado
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
        self.ui.estafos_filtro.currentTextChanged.connect(self.filtrar_reparaciones_estado)

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
        estado_seleccionado = self.ui.estafos_filtro.currentText()

        reparaciones = self.taller.listar_reparaciones()

        reparaciones_filtradas = []

        for reparacion in reparaciones:
            if reparacion.estado == estado_seleccionado:
                reparaciones_filtradas.append(reparacion)

        self.mostrar_reparaciones(reparaciones_filtradas)

def main():
    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()