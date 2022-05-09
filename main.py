import events
import var
import ventanaRest
import windowaviso
from PyQt5 import QtWidgets
import sys
import conexion

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventanaRest.Ui_Proxecto1()
        var.ui.setupUi(self)



        var.ui.elegirPrecio.buttonClicked.connect(events.selPrecio)
        var.ui.elegirConfianza.buttonClicked.connect(events.selConfianza)
        var.ui.tipoCocina.activated[str].connect(events.selTipoCocina)

        var.ui.altaRest.clicked.connect(events.altaRestaurante)
        var.ui.limpiar.clicked.connect(events.limpiarRest)
        var.ui.eliminar.clicked.connect(events.bajaRest)
        var.ui.modificar.clicked.connect(events.modifRest)
        var.ui.salir_2.clicked.connect(events.salir)

        var.ui.buscarNombre.clicked.connect(conexion.Conexion.buscarNombre)


        conexion.Conexion.db_connect(var.filedb)
        var.ui.buscar.clicked.connect(conexion.Conexion.buscarRest)
        conexion.Conexion.mostrarRest(self)



class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSlr = windowaviso.Ui_Dialog()
        var.dlgSlr.setupUi(self)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir,self).__init__()


if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    var.dlgSlr=DialogSalir()
    window.show()
    sys.exit(app.exec())