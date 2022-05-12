import os
import var
from reportlab.pdfgen import canvas
from PyQt5 import QtWidgets, QtSql
from datetime import *


class Printer():

    #Crea un informe en PDF con los restaurantes almacenados en la base de datos
    def reportRest(self):
        try:
            var.rep = canvas.Canvas('informes/listadoRestaurantes.pdf')
            var.rep.drawString(220, 800, 'LISTADO DE RESTAURANTES')
            var.rep.line(45, 790, 550, 790)
            Printer.cuerpo(self)
            Printer.pie(self)
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith(".pdf"):
                    os.startfile("%s/%s" % (rootPath, file))
                    cont = cont + 1
        except Exception as error:
            print("Error reporRest %s" % str(error))

    #Agrega una cabecera (no se utiliza en esta versión de la App)
    def cabecera(self):
        try:
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administración')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 820, 525, 820)
            textCif = "B17171717"
            textNom = "RECOMENDACIONES DE RESTAURANTES"
            textDir = "Travesía de Vigo 178"
            textTlf = "986 56 56 56"
            var.rep.drawString(50, 805, textCif)
            var.rep.drawString(50, 790, textNom)
            var.rep.drawString(50, 775, textDir)
            var.rep.drawString(50, 760, textTlf)

        except Exception as error:
            print("Error reporRest %s" % str(error))

    #Agrega el cuerpo principal del informe con los restaurantes recuperados de la base de datos
    def cuerpo(self):
        var.rep.setFont("Helvetica-Bold", size=9)
        itemRest = ["NOMBRE", "TIPO", "PRECIO", "CONFIANZA","DIRECCION","TELEFONO"]
        var.rep.drawString(60, 770, itemRest[0])
        var.rep.drawString(150, 770, itemRest[1])
        var.rep.drawString(210, 770, itemRest[2])
        var.rep.drawString(270, 770, itemRest[3])
        var.rep.drawString(370, 770, itemRest[4])
        var.rep.drawString(480, 770, itemRest[5])
        var.rep.line(45, 760, 550, 760)

        query = QtSql.QSqlQuery()
        query.prepare('select nombre,tipo,precio,confianza,direccion,telefono from restaurantes')
        if query.exec_():
            print("query ejecutada")
            i = 50
            j = 730
            while query.next():
                var.rep.drawString(i, j, str(query.value(0)))
                var.rep.drawString(i + 100, j, str(query.value(1)))
                var.rep.drawString(i + 170, j, str(query.value(2)))
                var.rep.drawString(i + 230, j, str(query.value(3)))
                var.rep.drawString(i + 300, j, str(query.value(4)))
                var.rep.drawString(i + 435, j, str(query.value(5)))
                j = j - 30

    #Añade un pie fijo para el informe
    def pie(self):
        try:
            var.rep.line(50,50,525,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique',size=7)
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275,40,str('Página %s' % var.rep.getPageNumber()))
        except Exception as error:
            print("Error pie del informe %s" % str(error))