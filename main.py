SEPARADOR_ELEMENTO = "§§§"
SEPARADOR_TABLA = "¶¶¶"
PROPIEDAD = "§"
TITULO = "¶"

class Datos:
    use = ""
    tablas = {}
    def __init__(self):
        with open("datos.txt", "r") as datos:
            text = datos.read()
            if text != "":
                tablasContenido = text.split(SEPARADOR_TABLA)
                for i in range(len(tablasContenido)):
                    tabla = tablasContenido[i]
                    titulo = tabla
        pass
    pass