import conexion
import var
import sys

def salir(self):
    try:
        var.dlgSlr.show()
        if var.dlgSlr.exec():
            sys.exit()
        else:
            var.dlgSlr.hide()
    except Exception as error:
        print("Error: %s", str(error))


def selPrecio(self):
    try:
        if var.ui.precioBarato.isChecked():
            var.precio = "Barato"
        if var.ui.precioMedio.isChecked():
            var.precio = "Medio"
        if var.ui.precioCaro.isChecked():
            var.precio = "Caro"
        if var.ui.precioMuyCaro.isChecked():
            var.precio = "Muy caro"
    except Exception as error:
        print("Error en módulo de selección de precio:", error)

def selConfianza(self):
    try:
        if var.ui.confBaja.isChecked():
            var.confianza = "Baja"
            print(var.confianza)
        if var.ui.confMedia.isChecked():
            var.confianza = "Media"
            print(var.confianza)
        if var.ui.confAlta.isChecked():
            var.confianza = "Alta"
            print(var.confianza)
        if var.ui.confAbsoluta.isChecked():
            var.confianza = "Absoluta"
            print(var.confianza)
    except Exception as error:
        print("Error en módulo de selección nivel de confianza:", error)

def selTipoCocina(cocina):
        try:
            var.tipoCocina=cocina
            print(var.tipoCocina)
        except Exception as error:
            print("Error en módulo de selección de tipo de cocina:", error)


def altaRestaurante():
    try:
        if var.ui.nombre.text() == "":
            var.ui.mensajes.setText("ES NECESARIO UN NOMBRE")
        else:
            rest = [var.ui.nombre.text(), var.tipoCocina, var.precio, var.ui.recomienda.text(),var.confianza,var.ui.direccion.text(),var.ui.telefono.text()]
            conexion.Conexion.cargarRest(rest)
    except Exception:
        var.ui.mensajes.setText("DATOS INSUFICIENTES")

def limpiarRest(self):
    var.ui.nombre.setText("")
    var.ui.tipoCocina.setCurrentIndex(0)
    var.tipoCocina="Tradicional"
    var.ui.recomienda.setText("")
    var.ui.direccion.setText("")
    var.ui.telefono.setText("")

def bajaRest(self):
    try:
        nombre=var.ui.nombre.text()
        conexion.Conexion.bajaRest(nombre)
    except Exception as error:
        print("Error cargar rest: %s " % str(error))


def modifRest(self):
        try:
            nombre=var.ui.nombre.text()
            if nombre == "":
                var.ui.mensajes.setText("ES NECESARIO UN NOMBRE")
            else:
                rest = [var.tipoCocina, var.precio, var.ui.recomienda.text(), var.confianza,
                        var.ui.direccion.text(), var.ui.telefono.text()]
                conexion.Conexion.modifRest(nombre,rest)
        except Exception as error:
            print("Error modificar clientes: %s " % str(error))
            var.ui.mensajes.setText('ERROR AL MODIFICAR')

