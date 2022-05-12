import zipfile
from datetime import datetime

import conexion
import var
from PyQt5 import QtWidgets
import shutil
import os
import xlrd


class Backup():

    #Guarda un zip con una copia de la base de datos en el directorio que seleccione el usuario
    def crearBackup():
        try:
            fecha=datetime.today()
            fecha=fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia= (str(fecha)+'_backup.zip')
            option=QtWidgets.QFileDialog.Options()
            directorio,filename=var.filedlgabrir.getSaveFileName(None,'Guardar Copia',var.copia,'zip',options=option)
            if var.filedlgabrir.Accepted and filename !='':
                fichzip=zipfile.ZipFile(var.copia,'w')
                fichzip.write(var.filedb,os.path.basename(var.filedb),zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.mensajes.setText("Base de datos guardada")
                shutil.move(str(var.copia),str(directorio))
                var.ui.mensajes.setText("BACKUP GUARDADO")
                var.ui.mensajes2.setText("BACKUP GUARDADO")
        except Exception as error:
            print('"Error: %s' % str(error))

    #Sustituye la base de datos actual por una copia de seguridad almacenada anteriormente
    def recuperarBackup(self):
        ventana_restaurar = QtWidgets.QFileDialog
        filename = ventana_restaurar.getOpenFileName(None, 'Restaurar Copia', "Copia de seguridad BD",
                                                     "Archivos Zip (*.zip)")
        var.filedb=shutil.unpack_archive(filename.__getitem__(0))
        var.ui.mensajes.setText("BACKUP RECUPERADO")
        var.ui.mensajes2.setText("BACKUP RECUPERADO")

    #Añade restaurantes a partir de un archivo .xls seleccionado por el usuario
    def recuperarExcel():
        ventana_restaurar = QtWidgets.QFileDialog
        filename = ventana_restaurar.getOpenFileName(None,'Seleccionar excel',"","Archivos xls (*.xls)")
        documento=xlrd.open_workbook(filename.__getitem__(0))
        restaurantesNuevos=documento.sheet_by_index(0)
        filasRestaurantes=restaurantesNuevos.nrows
        fila=0

        while fila < filasRestaurantes:
            nombre=restaurantesNuevos.cell_value(fila,0)
            tipo=restaurantesNuevos.cell_value(fila,1)
            precio=restaurantesNuevos.cell_value(fila,2)
            recomendador=restaurantesNuevos.cell_value(fila,3)
            confianza=restaurantesNuevos.cell_value(fila,4)
            direccion = restaurantesNuevos.cell_value(fila, 5)
            telefono=restaurantesNuevos.cell_value(fila,6)
            rest=[nombre,tipo,precio,recomendador,confianza,direccion,telefono]
            fila+=1
            conexion.Conexion.cargarRest(rest)

