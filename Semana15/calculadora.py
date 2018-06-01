import sys
from PyQt5 import QtWidgets, uic, QtGui

class MiVentana(QtWidgets.QDialog):

    def operar(self, n1, n2, tipo):
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
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())
            op = self.oper.currentText()
            self.resultado.setText('Resultado: '+
                                   str(self.operar(n1, n2, op)))
        except ValueError:
            self.resultado.setText('Datos no númericos')

    def __init__(self):
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
    app = QtWidgets.QApplication(sys.argv)
    window = MiVentana()
    sys.exit(app.exec_())