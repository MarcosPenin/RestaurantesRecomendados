import printer
import backup
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
        var.filedlgabrir = FileDialogAbrir()

        # Comienzo conectándome a la base de datos
        conexion.Conexion.db_connect(var.filedb)

        # Conecto los Combobox y los RadioButton con sus respectivos eventos
        var.ui.elegirPrecio.buttonClicked.connect(events.selPrecio)
        var.ui.elegirConfianza.buttonClicked.connect(events.selConfianza)
        var.ui.tipoCocina.activated[str].connect(events.selTipoCocina)
        var.ui.tipoCocina2.activated[str].connect(events.selTipoCocina2)

        # Conecto los eventos de los botones de la primera pestaña
        var.ui.buscar.clicked.connect(conexion.Conexion.buscarRest)
        var.ui.altaRest.clicked.connect(events.altaRestaurante)
        var.ui.limpiar.clicked.connect(events.limpiarRest)
        var.ui.eliminar.clicked.connect(events.bajaRest)
        var.ui.modificar.clicked.connect(events.modifRest)
        var.ui.salir_2.clicked.connect(events.salir)

        # Conecto los botones de búsqueda de la segunda pestaña
        var.ui.buscarNombre.clicked.connect(conexion.Conexion.buscarNombre)
        var.ui.buscarTipo.clicked.connect(conexion.Conexion.buscarTipo)
        var.ui.buscarRecomendador.clicked.connect(conexion.Conexion.buscarRecomendador)
        var.ui.verTodo.clicked.connect(conexion.Conexion.mostrarRest)

        # Conecto las acciones del menú de herramientas
        var.ui.actionCrear_Backup.triggered.connect(backup.Backup.crearBackup)
        var.ui.actionRecuperar_Backup.triggered.connect(backup.Backup.recuperarBackup)
        var.ui.actionImportar_Excel.triggered.connect(backup.Backup.recuperarExcel)
        var.ui.actionGenerar_Informe.triggered.connect(printer.Printer.reportRest)


# Defino las ventanas adicionales que necesitaré
class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSlr = windowaviso.Ui_Dialog()
        var.dlgSlr.setupUi(self)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgSlr = DialogSalir()
    window.show()
    sys.exit(app.exec())
