import sys
from controlador.controlador import Controlador
from PySide6.QtWidgets import QApplication
def main():
    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()