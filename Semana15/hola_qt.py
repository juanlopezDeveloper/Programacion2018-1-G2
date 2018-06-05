import sys
from PyQt5 import QtWidgets

def window():
    """
    Función de ventana con interfaz y datos de su parte grafica.
    :return: Interfaz grafica conocida como ventana
    """
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QLabel(w)
    b.setText("Hola Qt")
    w.setGeometry(500, 500, 300, 100)
    b.move(110, 40)
    w.setWindowTitle('Mi primer qt')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    """Ruta para visualizar ventana"""
    window()
