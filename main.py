SEPARADOR_ELEMENTO = "§§§"
SEPARADOR_TABLA = "¶¶¶"
PROPIEDAD = "§"
TITULO = "¶"

# Constantes
MENU_PRINCIPAL = '''
1. Registrar Cliente
2. Registrar Veterinario
3. Registrar Mascota
4. Registrar Cita
5. Consultar Información de Clientes
6. Consultar Información de Mascotas
7. Consultar Historial de Servicios
8. Consultar Citas
9. Salir
'''

MENU_SERVICIOS = '''
1. Consultar Servicios Disponibles
2. Registrar Servicio
3. Modificar Servicio
4. Eliminar Servicio
'''

MENU_CITAS = '''
1. Registrar Cita
2. Consultar Citas
3. Modificar Cita
4. Cancelar Cita
'''

MENU_CLIENTES_VETERINARIOS = '''
1. Consultar Cliente
2. Consultar Veterinario
3. Modificar Cliente
4. Modificar Veterinario
'''

# Clases
class persona:
    def __init__(self, nombre: str, contacto: str, identidad:str):
        self.nombre = nombre
        self.contacto = contacto
        self.id = identidad


class Cliente(persona):
    def __init__(self, nombre, contacto, identidad, dirección):
        super().__init__(nombre, contacto, identidad)
    pass

class Veterinario(persona):
    def __init__(self, nombre, contacto, identidad, especialidad, licencia, horario):
        super().__init__(nombre, contacto, identidad)
    pass

class Mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueño):
        pass

class Servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        pass

class Cita:
    def __init__(self, fecha, hora, servicio, veterinario, id_mascota):
        pass

def main():

    pass


class Datos:
    use = ""
    tablas: dict[str, list[persona]] = {
        "clientes": [],
        "veterinarios": [],
        "mascotas": [],
        "servicios": [],
    }
    def __init__(self):
        with open("datos.txt", "r") as datos:
            text = datos.read()
            if text != "":
                tablasContenido = text.split(SEPARADOR_TABLA)
                for tabla in tablasContenido:
                    titulo = tabla.split(TITULO)[0]
                    contenidoTexto = tabla.split(TITULO)[1]
                    contenido = contenidoTexto.split(SEPARADOR_ELEMENTO)
                    for elemento in contenido:
                        propiedades = elemento.split(PROPIEDAD)
                        if titulo == "cliente":
                            cliente = Cliente(propiedades[0], propiedades[1], propiedades[2], propiedades[3])
                            self.tablas["clientes"].append(cliente)
                        elif titulo == "veterinario":
                            veterinario = Veterinario(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4], propiedades[5])
                            self.tablas["veterinarios"].append(veterinario)
                        elif titulo == "mascota":
                            mascota = Mascota(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4], propiedades[5])
                            self.tablas["mascotas"].append(mascota)
                        elif titulo == "servicio":
                            servicio = Servicio(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4])
                            self.tablas["servicios"].append(servicio)
                        pass
                    
                    
        pass
    pass

    def obtener(self, id: int):
        result = self.tablas[self.use][id]
        return result
    
    def guardar(self):
        with open("datos.txt", "w") as datos:
            for key in self.tablas:
                texto = key + TITULO
                for elemento in self.tablas[key]:
                    for propiedad in elemento:
                        texto += propiedad + PROPIEDAD
                    pass
                    texto += SEPARADOR_ELEMENTO
                pass
                texto += SEPARADOR_TABLA
                datos.write(texto)
            pass
        pass

    def eliminar(self, id: int):
        self.tablas[self.use].pop(id)
        pass