import var


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
        if var.ui.confMedia.isChecked():
            var.confianza = "Media"
        if var.ui.confAlta.isChecked():
            var.confianza = "Alta"
        if var.ui.confAbsoluta.isChecked():
            var.confianza = "Absoluta"
    except Exception as error:
        print("Error en módulo de selección nivel de confianza:", error)

def selTipoCocina(cocina):
        try:
            var.tipoCocina=cocina
            print(var.tipoCocina)
        except Exception as error:
            print("Error en módulo de selección de tipo de cocina:", error)