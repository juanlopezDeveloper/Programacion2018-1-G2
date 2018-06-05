import sys
from PyQt5 import QtWidgets

def window():
    """
    Función que muestra graficamente la interfaz
    :return: Interfaz grafica
    """
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    etiquetas = [[]]
    for i in range(0,10):
        etiquetas.append([])
        for j in range(0, 10):
            etiquetas[i].append(QtWidgets.QLabel(w))
            etiquetas[i][j].setText(str(i)+','+ str(j))
            etiquetas[i][j].move(110+i*30,40+30*j)
    w.setGeometry(500, 500, 300, 100)
    # b.move(110, 40)
    w.setWindowTitle('Mi primer qt')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    """Ruta para mostrar la ventana"""
    window()
