SEPARADOR_ELEMENTO = "§§§"
SEPARADOR_TABLA = "¶¶¶"
PROPIEDAD = "§"
TITULO = "¶"

# Constantes
MENU_PRINCIPAL = '''
====Bienvenido a Huella Feliz====
1. Clientes
2. Veterinarios
3. Mascotas
4. Servicios
5. Agendar citas
6. Historial de citas (General)
7. Salir
'''

MENU_CLIENTE = '''
===Cliente===
1. Registrar cliente
2. Modificar cliente
3. Consultar clientes
4. Eliminar cliente
'''

MENU_VETERINARIO = '''
===Veterinario===
1. Registrar veterinario
2. Modificar veterinario
3. Consultar veterinarios
4. Eliminar veterinario
'''

MENU_MASCOTA = '''
===Mascota===
1. Registrar mascota
2. Modificar mascota
3. Consultar mascotas
4. Eliminar mascota
'''

MENU_SERVICIOS = '''
1. Ver servicios
2. Registrar Servicio
3. Modificar Servicio
4. Eliminar Servicio
'''

# Clases
class Persona:
    def __init__(self, nombre, contacto, identidad):
        self.nombre = nombre
        self.contacto = contacto
        self.id = identidad


class Cliente(Persona):
    def __init__(self, nombre, contacto, identidad, direccion):
        super().__init__(nombre, contacto, identidad)
        self.direccion = direccion


class Veterinario(Persona):
    def __init__(self, nombre, contacto, identidad, especialidad, licencia, horario):
        super().__init__(nombre, contacto, identidad)
        self.especialidad = especialidad
        self.licencia = licencia
        self.horario = horario


class Mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.identidad = identidad
        self.dueño = dueño


class Servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        self.tipo = tipo
        self.descripcion = descripcion
        self.duracion = duracion
        self.costo = costo
        self.frecuencia = frecuencia


class Cita:
    def __init__(self, fecha, hora, servicio, veterinario, id_mascota):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
        self.id_mascota = id_mascota

class Datos:
    use = ""
    tablas: dict[str, list[Persona]] = {
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
                    texto += SEPARADOR_ELEMENTO
                texto += SEPARADOR_TABLA
                datos.write(texto)

    def eliminar(self, id: int):
        self.tablas[self.use].pop(id)

# Main Programa
def main():
    while True:
        print(MENU_PRINCIPAL)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Clientes")
            pass
        elif opcion == "2":
            print("Veterinarios")
            pass
        elif opcion == "3":
            print("Mascotas")
            pass
        elif opcion == "4":
            print("Servicios")
            pass
        elif opcion == "5":
            print("Agendar citas")
            pass
        elif opcion == "6":
            print("Historial de citas")
            pass
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()