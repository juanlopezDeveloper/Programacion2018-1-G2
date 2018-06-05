# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

#Importamos las aplicaciones PyQt5, QtCore, QtGui, QtWidgets y sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    """Clase para representar algo grafico"""
    def setupUi(self, Dialog):
        """
        Instancia para crear una ventana grafica.
        :param Dialog: La ventana interfaz
        :return: Una ventana gráfica
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 223)
        self.opButton = QtWidgets.QPushButton(Dialog)
        self.opButton.setGeometry(QtCore.QRect(11, 120, 381, 29))
        self.opButton.setObjectName("opButton")
        self.resultado = QtWidgets.QLabel(Dialog)
        self.resultado.setGeometry(QtCore.QRect(10, 170, 371, 31))
        self.resultado.setObjectName("resultado")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 381, 101))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.num1 = QtWidgets.QLineEdit(self.widget1)
        self.num1.setObjectName("num1")
        self.verticalLayout_2.addWidget(self.num1)
        self.num2 = QtWidgets.QLineEdit(self.widget1)
        self.num2.setObjectName("num2")
        self.verticalLayout_2.addWidget(self.num2)
        self.oper = QtWidgets.QComboBox(self.widget1)
        self.oper.setObjectName("oper")
        self.verticalLayout_2.addWidget(self.oper)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """
        Función que contiene atributos de texto de las etiquetas de la interfaz.
        :param Dialog: Interfaz con texto.
        :return: Etiquetas con texto de la interfaz.
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculadora"))
        self.opButton.setText(_translate("Dialog", "Operar"))
        self.resultado.setText(_translate("Dialog", "Resultado: "))
        self.label.setText(_translate("Dialog", "Numero 1:"))
        self.label_2.setText(_translate("Dialog", "Numero 2: "))
        self.label_3.setText(_translate("Dialog", "Operación: "))
