# Constantes
import os
import platform


SEPARADOR_ELEMENTO = "§§§"
SEPARADOR_TABLA = "¶¶¶"
PROPIEDAD = "§"
TITULO = "¶"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

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

# funciones fundamentales para clases
def borrarConsola():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def isFloat(valor: str):
    try:
        float(valor)
        return True
    except ValueError:
        return False

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
    
    def obtenerDia (self, dia: str):
        index = DIAS.index(dia)
        if self.horario[index] == "1":
            return True
            


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

class PropiedadFormulario:
    def __init__(self, titulo, valor, callback: function = None):
        self.titulo = titulo
        self.valor = valor
        self.callback = callback


class Formulario:
    def __init__(self, titulo:str, campos:list[PropiedadFormulario]):
        self.__titulo = titulo
        self.__campos = campos
    
    def agregarCampo(self, titulo:str, valor:str, callback: function = None): 
        prop = PropiedadFormulario(titulo, valor)
        if callback != None:
            prop.callback = callback
        self.__campos.append(prop)
    
    def modificarCampo(self, titulo:str, valor:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                campo.valor = valor
    
    def eliminarCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                self.__campos.remove(campo)
    
    def obtenerCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                return campo
    
    def realizar(self):
        print(self.__titulo)
        print("Digite los valores solicitados")
        formulario: dict[str, str | int | float | bool] = {}
        for campo in self.__campos:
            while True:
                texto = campo.titulo + ": "
                if campo.valor == "boolean":
                    print(campo.titulo)
                    print("1. Sí")
                    print("2. No")
                    texto = "Respuesta: "
                respuesta = input(texto)
                try:
                    valorCorrecto = True
                    valorIngresar = ""
                    
                    # validamos que el campo ingresado sea un valor admitido por el formulario
                    if campo.valor == "int":
                        if respuesta.isnumeric():
                            valorIngresar = int(respuesta)
                        else:
                            valorCorrecto = False
                    elif campo.valor == "float":
                        if isFloat(respuesta):
                            valorIngresar = float(respuesta)
                        else:
                            valorCorrecto = False
                    elif campo.valor == "boolean":
                        if respuesta == "1" or respuesta == "Si" or respuesta == "si" or respuesta == "SI":
                            valorIngresar = True
                        elif respuesta == "2" or respuesta == "No" or respuesta == "no" or respuesta == "NO":
                            valorIngresar = False
                        else: 
                            valorCorrecto = False
                            
                    else:
                        valorIngresar = respuesta

                    boo = True
                    if campo.callback != None:
                        boo = campo.callback(respuesta)
                    if boo:
                        formulario[campo.titulo] = valorIngresar
                        pass
                            

                    if not valorCorrecto:
                        raise ValueError("Valor incorrecto")
                    break
                except ValueError as e:
                    print(e)
                    return
                
        return formulario

    

class Datos:
    use = ""
    tablas: dict[str, list[Persona]] = {
        "clientes": [],
        "veterinarios": [],
        "mascotas": [],
        "servicios": [],
        "citas": []
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
                        elif titulo == "cita":
                            cita = Cita(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4])
                            self.tablas["citas"].append(cita)
                        

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
    
    def modificar(self, id: int, key: str, value):
        self.tablas[self.use][id][key] = value
    
    def largo (self):
        return len(self.tablas[self.use])
    
    def agregar(self, elemento):
        self.tablas[self.use].append(elemento)




def menuVeterinario(datos: Datos):
    borrarConsola()
    print(MENU_VETERINARIO)
    opcion = input("Seleccione una opción: ")
    datos.use = "veterinarios"
    if opcion == "1":
        # tipos de especialidades admitidas
        especialidades = ["Cardiología", "Dermatología", "Neurología", "Oftalmología", "Oncología", "Ortopedia"]

        # creamos el formulario y agregamos los campos
        formulario = Formulario("Registrar veterinario", [])
        formulario.agregarCampo("Nombre", "str", lambda x: len(x) >= 3 and x.isalpha() )
        formulario.agregarCampo("Contacto", "str")
        formulario.agregarCampo("Especialidad", "str", lambda x: x in especialidades)
        formulario.agregarCampo("Licencia", "str", lambda x: len(x) == 10 and x.isnumeric())
        resultado = formulario.realizar()

        # vamos a realizar un segundo formulario para obtener el horario de atención
        formularioHorario = Formulario("Horario de atención. ¿Tiene disponibilidad los siguientes dias?", [])
        for dia in DIAS:
            formularioHorario.agregarCampo(dia, "boolean")

        resultadoHorario =  formularioHorario.realizar()
        horario = ""
        for dia in resultadoHorario:
            if resultadoHorario[dia]:
                horario += "1"
            else:
                horario += "0"

        # obtenemos los valores del resultado del formulario
        nombre = resultado["Nombre"]
        contacto = resultado["Contacto"]
        especialidad = resultado["Especialidad"]
        licencia = resultado["Licencia"]

        veterinario = Veterinario(nombre, contacto, datos.largo(), especialidad, licencia, horario)
        datos.agregar(veterinario)
        pass
    elif opcion == "2":
        print("Modificar veterinario")
        pass
    elif opcion == "3":
        print("Consultar veterinarios")
        pass
    elif opcion == "4":
        print("Eliminar veterinario")
        pass
    else:
        print("Opción no válida. Intente de nuevo.")

# Main Programa
def main():
    while True:
        borrarConsola()
        print(MENU_PRINCIPAL)
        opcion = input("Seleccione una opción: ")
        datos = Datos()
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