# Importamos las aplicaciones sys, PyQt5, QtWidgets, Uic y QtGui
import sys
from PyQt5 import QtWidgets, uic, QtGui

class MiVentana(QtWidgets.QDialog):
    """ Esta clase es de una interfaz que tiene atributos para ser una calculadora"""

    def operar(self, n1, n2, tipo):
        """
        int -> int
        Función para realizar operaciones básicas de calculadora.
        
        :param n1: Número entero
        :param n2: Número entero
        :param tipo: booleano
        :return: Nḿuero entero
        """
        if tipo == 'Suma':
            return n1 + n2
        elif tipo == 'Resta':
            return n1 - n2
        elif tipo == 'Producto':
            return n1 * n2
        elif tipo == 'Division':
            if n2 == 0:
                return 'No dividiras por 0'
            return n1 / n2

    def btn_operar(self):
        """
        Permite digitar números decimales.
        :return: Número decimal.
        """
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())
            op = self.oper.currentText()
            self.resultado.setText('Resultado: '+
                                   str(self.operar(n1, n2, op)))
        except ValueError:
            self.resultado.setText('Datos no númericos')

    def __init__(self):
        """Instancia que importa interfaz de PyQt5 con forma de calculadora"""
        super(MiVentana, self).__init__()
        uic.loadUi('calculadora.ui',self)
        self.oper.addItems([
            'Suma',
            'Resta',
            'Producto',
            'Division'
        ])
        self.opButton.clicked.connect(self.btn_operar)
        self.show()

if __name__ == '__main__':
    """Importa las graficas de la calculadora"""
    app = QtWidgets.QApplication(sys.argv)
    window = MiVentana()
    sys.exit(app.exec_())
