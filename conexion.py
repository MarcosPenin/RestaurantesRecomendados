from PyQt5 import QtWidgets, QtSql

import events
import var



class Conexion():

    # Conecta la aplicación con la base de datos
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos,'
                                                 'No se puede establecer conexion.\n Haz Click para Cancelar',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion establecida')
        return True

    #Carga un restaurante en la base de datos. Recibe un array con los diversos campos
    #y compone una insert con ella. Si tiene éxito limpia el formulario e informa al usuario. Si no
    #emite un aviso
    def cargarRest(restaurante):
        query = QtSql.QSqlQuery()
        query.prepare('insert into restaurantes(nombre,tipo,precio,recomendador,confianza,direccion,telefono)'
                      'VALUES(:nombre,:tipo,:precio,:recomendador,:confianza,:direccion,:telefono)')
        query.bindValue(':nombre', str(restaurante[0]))
        query.bindValue(':tipo', str(restaurante[1]))
        query.bindValue(':precio', str(restaurante[2]))
        query.bindValue(':recomendador', str(restaurante[3]))
        query.bindValue(':confianza', str(restaurante[4]))
        query.bindValue(':direccion', str(restaurante[5]))
        query.bindValue(':telefono', str(restaurante[6]))

        if query.exec_():
            var.ui.mensajes.setText('RESTAURANTE GUARDADO')
            events.limpiarRest(self=var.ui)
        else:
            var.ui.mensajes.setText('YA EXISTE UN RESTAURANTE CON ESE NOMBRE')
            print("Error: ", query.lastError().text())


    #Busca un restaurante en la base de datosa partir de su nombre.
    #Si encuentra una coincidencia actualiza los campos de la interfaz.
    def buscarRest(self):
        nombre = var.ui.nombre.text()
        query = QtSql.QSqlQuery()
        query.prepare(
            'select tipo,precio,recomendador,confianza,direccion,telefono from restaurantes where nombre= :nombre')
        query.bindValue(':nombre', nombre)

        flag = False
        if query.exec_():
            while query.next():
                flag = True
                tipo = query.value(0)
                precio = query.value(1)
                recomendador = query.value(2)
                confianza = query.value(3)
                direccion = query.value(4)
                telefono = query.value(5)

                var.ui.recomienda.setText(recomendador)
                var.ui.direccion.setText(direccion)
                var.ui.telefono.setText(telefono)

                if tipo == "Tradicional":
                    var.ui.tipoCocina.setCurrentIndex(0)
                if tipo == "Fusión":
                    var.ui.tipoCocina.setCurrentIndex(1)
                if tipo == "Alta cocina":
                    var.ui.tipoCocina.setCurrentIndex(2)
                if tipo == "Asiática":
                    var.ui.tipoCocina.setCurrentIndex(3)
                if tipo == "Italiana":
                    var.ui.tipoCocina.setCurrentIndex(4)
                if tipo == "Mexicana":
                    var.ui.tipoCocina.setCurrentIndex(5)

                if precio == "Barato":
                    var.ui.precioBarato.toggle()
                    var.precio = "Barato"
                if precio == "Medio":
                    var.ui.precioMedio.toggle()
                    var.precio = "Medio"
                if precio == "Caro":
                    var.ui.precioCaro.toggle()
                    var.precio = "Caro"
                if precio == "Muy caro":
                    var.ui.precioMuyCaro.toggle()
                    var.precio = "Muy caro"

                if confianza == "Baja":
                    var.ui.confBaja.toggle()
                    var.confianza = "Baja"
                if confianza == "Media":
                    var.ui.confMedia.toggle()
                    var.confianza = "Media"
                if confianza == "Alta":
                    var.ui.confAlta.toggle()
                    var.confianza = "Alta"
                if confianza == "Absoluta":
                    var.ui.confAbsoluta.toggle()
                    var.confianza = "Absoluta"
                var.ui.mensajes.setText("")
            if flag == False:
                var.ui.mensajes.setText('RESTAURANTE NO ENCONTRADO')
                events.limpiarRest(self=var.ui)


    #Busca un restaurante a partir de su nombre y lo elimina de la base de datos
    #si lo encuentra
    def bajaRest(nombre):
        query = QtSql.QSqlQuery()
        query.prepare('delete from restaurantes where nombre = :nombre')
        query.bindValue(':nombre', nombre)
        if query.exec_():
            if (nombre != ""):
                var.ui.mensajes.setText('Restaurante ' + nombre + ' eliminado')
                events.limpiarRest(self=var.ui)
            else:
                var.ui.mensajes.setText("NO SE HA PODIDO BORRAR")
        else:
            print("Error eliminar clientes: ", query.lastError().text())

    #Busca un restaurante a partir de su nombre y actualiza sus campos con
    #los que ha introducido el usuario si encuetntra una coincidencia
    def modifRest(nombre, rest):
        query = QtSql.QSqlQuery()
        query.prepare(
            'update restaurantes set tipo=:tipo,precio=:precio,recomendador=:recomendador,confianza=:confianza,direccion=:direccion,telefono=:telefono '
            'where nombre=:nombre')
        query.bindValue(':nombre', nombre)
        query.bindValue(':tipo', str(rest[0]))
        query.bindValue(':precio', str(rest[1]))
        query.bindValue(':recomendador', str(rest[2]))
        query.bindValue(':confianza', str(rest[3]))
        query.bindValue(':direccion', str(rest[4]))
        query.bindValue(':telefono', str(rest[5]))

        if query.exec_():
            var.ui.mensajes.setText('RESTAURANTE ' + nombre + ' modificado')
        else:
            print("Error al modificar restaurante: ", query.lastError().text())
            var.ui.mensajes.setText('FALTAN DATOS')

    #Muestra una tabla con todos los restaurantes guardados
    #en la base de datos
    def mostrarRest(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select nombre,tipo,precio,recomendador, confianza, direccion, telefono from restaurantes')
        if query.exec_():
            while query.next():
                var.ui.tablaRestaurantes.setRowCount(index + 1)
                var.ui.tablaRestaurantes.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tablaRestaurantes.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tablaRestaurantes.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tablaRestaurantes.setItem(index, 3, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tablaRestaurantes.setItem(index, 4, QtWidgets.QTableWidgetItem(query.value(4)))
                var.ui.tablaRestaurantes.setItem(index, 5, QtWidgets.QTableWidgetItem(query.value(5)))
                var.ui.tablaRestaurantes.setItem(index, 6, QtWidgets.QTableWidgetItem(query.value(6)))
                index += 1
        else:
            print("Error mostrar restaurantes: ", query.lastError().text())

    # Muestra el restaurante que coincida con el nombre introducido por el usuario
    def buscarNombre(self):
        nombre = var.ui.nombre2.text()
        query = QtSql.QSqlQuery()
        query.prepare(
            'select tipo,precio,recomendador, confianza, direccion, telefono from restaurantes where nombre= :nombre')
        query.bindValue(':nombre', nombre)

        if query.exec_():
            flag = False
            while (query.next()):
                flag = True
                var.ui.tablaRestaurantes.setRowCount(1)
                var.ui.tablaRestaurantes.setItem(0, 0, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaRestaurantes.setItem(0, 1, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tablaRestaurantes.setItem(0, 2, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tablaRestaurantes.setItem(0, 3, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tablaRestaurantes.setItem(0, 4, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tablaRestaurantes.setItem(0, 5, QtWidgets.QTableWidgetItem(query.value(4)))
                var.ui.tablaRestaurantes.setItem(0, 6, QtWidgets.QTableWidgetItem(query.value(5)))
                var.ui.mensajes2.setText("")
            if flag == False:
                var.ui.mensajes2.setText("NO EXISTE")
        else:
            print("Error de búsqueda: ", query.lastError().text())

    #Muestra una tabla con los restaurantes almacenados cuyo tipo coincida con
    #el seleccionado por el usuario
    def buscarTipo(self):
        index = 0
        tipo = var.tipoCocina2
        query = QtSql.QSqlQuery()
        query.prepare(
            'select nombre,precio,recomendador, confianza, direccion, telefono from restaurantes where tipo= :tipo')
        query.bindValue(':tipo', tipo)

        if query.exec_():
            flag = False
            while query.next():
                flag = True
                var.ui.tablaRestaurantes.setRowCount(index + 1)
                var.ui.tablaRestaurantes.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tablaRestaurantes.setItem(index, 1, QtWidgets.QTableWidgetItem(tipo))
                var.ui.tablaRestaurantes.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tablaRestaurantes.setItem(index, 3, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tablaRestaurantes.setItem(index, 4, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tablaRestaurantes.setItem(index, 5, QtWidgets.QTableWidgetItem(query.value(4)))
                var.ui.tablaRestaurantes.setItem(index, 6, QtWidgets.QTableWidgetItem(query.value(5)))
                index += 1
                var.ui.mensajes2.setText("")
            if flag == False:
                var.ui.mensajes2.setText("NO EXISTE NINGUNO")

        else:
            print("Error de búsqueda: ", query.lastError().text())

    # Muestra una tabla con los restaurantes almacenados cuyo recomendador coincida con
    # el introducido por el usuario
    def buscarRecomendador(self):
        recomendador = var.ui.recomendador2.text()
        query = QtSql.QSqlQuery()
        query.prepare(
            'select nombre,tipo,precio,confianza,direccion,telefono from restaurantes where recomendador= :recomendador')
        query.bindValue(':recomendador', recomendador)

        if query.exec_():
            flag = False
            while query.next():
                flag = True
                var.ui.tablaRestaurantes.setRowCount(1)
                var.ui.tablaRestaurantes.setItem(0, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tablaRestaurantes.setItem(0, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tablaRestaurantes.setItem(0, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tablaRestaurantes.setItem(0, 3, QtWidgets.QTableWidgetItem(recomendador))
                var.ui.tablaRestaurantes.setItem(0, 4, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tablaRestaurantes.setItem(0, 5, QtWidgets.QTableWidgetItem(query.value(4)))
                var.ui.tablaRestaurantes.setItem(0, 6, QtWidgets.QTableWidgetItem(query.value(5)))
                var.ui.mensajes2.setText("")
            if flag == False:
                var.ui.mensajes2.setText("NO EXISTE NINGUNO")

        else:
            print("Error de búsqueda: ", query.lastError().text())
