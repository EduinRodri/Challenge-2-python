# Constantes
import os
import platform


SEPARADOR_ELEMENTO = "|||"
SEPARADOR_TABLA = "~~~"
PROPIEDAD = "°"
TITULO = "°°"
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
5. Salir
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
    
    def toArray (self):
        return [self.nombre, self.contacto, str(self.id)]

class Cliente(Persona):
    def __init__(self, nombre, contacto, identidad, direccion):
        super().__init__(nombre, contacto, identidad)
        self.direccion = direccion
    
    def toArray(self):
        array = super().toArray()
        array.append(self.direccion)
        return array
    


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
        return False
    
    def toArray(self):
        array = super().toArray()
        array.append(self.especialidad)
        array.append(self.licencia)
        array.append(self.horario)
        return array
            


class Mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.identidad = identidad
        self.dueño = dueño

    def toArray(self):
        return [self.nombre, self.especie, self.raza, self.edad, self.identidad, self.dueño]


class Servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        self.tipo = tipo
        self.descripcion = descripcion
        self.duracion = duracion
        self.costo = costo
        self.frecuencia = frecuencia
    
    def toArray(self):
        return [self.tipo, self.descripcion, self.duracion, self.costo, self.frecuencia]


class Cita:
    def __init__(self, fecha, hora, servicio, veterinario, id_mascota):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
        self.id_mascota = id_mascota
    
    def toArray(self):
        return [self.fecha, self.hora, self.servicio, self.veterinario, self.id_mascota]

class PropiedadFormulario:
    def __init__(self, titulo, valor, callback = None, invalido = ""):
        self.titulo = titulo
        self.valor = valor
        self.callback = callback
        self.invalido = invalido


class Formulario:
    def __init__(self, titulo:str, campos:list[PropiedadFormulario]):
        self.__titulo = titulo
        self.__campos = campos
    
    def agregarCampo(self, titulo:str, valor:str, callback = None, invalido=""): 
        prop = PropiedadFormulario(titulo, valor)
        if callback != None:
            prop.callback = callback
            prop.invalido = invalido
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
        formulario: dict[str, str | int | float | bool] = {}
        for campo in self.__campos:
            while True:
                texto = campo.titulo + ": "
                error = "Valor incorrecto"
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
                            error = "El valor debe ser un número entero"
                    elif campo.valor == "float":
                        if isFloat(respuesta):
                            valorIngresar = float(respuesta)
                        else:
                            valorCorrecto = False
                            error = "El valor debe ser un numero decimal"
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
                        valorCorrecto = boo
                        if campo.invalido != "":
                            error = campo.invalido
                            
                    if boo:
                        formulario[campo.titulo] = valorIngresar
                        pass
                            

                    if not valorCorrecto:
                        raise ValueError(error)
                    break
                except ValueError as e:
                    print(e)
                    
                
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
                    input(tabla)
                    split = tabla.split(TITULO)

                    if len(split) > 1:
                        titulo = split[0]
                        
                        contenidoTexto = split[1]
                        contenido = contenidoTexto.split(SEPARADOR_ELEMENTO)
                        if len(contenido) > 1:
                            for elemento in contenido:
                                propiedades = elemento.split(PROPIEDAD)
                                if titulo == "clientes":
                                    cliente = Cliente(propiedades[0], propiedades[1], propiedades[2], propiedades[3])
                                    self.tablas["clientes"].append(cliente)
                                elif titulo == "veterinarios":
                                    veterinario = Veterinario(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4], propiedades[5])
                                    self.tablas["veterinarios"].append(veterinario)
                                elif titulo == "mascotas":
                                    mascota = Mascota(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4], propiedades[5])
                                    self.tablas["mascotas"].append(mascota)
                                elif titulo == "servicios":
                                    servicio = Servicio(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4])
                                    self.tablas["servicios"].append(servicio)
                                elif titulo == "citas":
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
                    iterable = elemento.toArray()
                    for propiedad in iterable:
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


def mostrarTabla(tabla: list[Persona]):
    for i in range(len(tabla)):
        print(f"{i + 1}. {tabla[i].nombre}")


def menuVeterinario(datos: Datos):
    datos.use = "veterinarios"
    especialidades = ["Cardiologia", "Dermatologia", "Neurologia", "Oftalmologia", "Oncologia", "Ortopedia"]
    def seleccionarVeterinario():
        print("Seleccione el veterinario")
        mostrarTabla(datos.tablas["veterinarios"])
        veterinario = int(input("Veterinario: ")) - 1
        return veterinario
    while True:
        borrarConsola()
        print(MENU_VETERINARIO)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            borrarConsola()
            # creamos el formulario y agregamos los campos
            formulario = Formulario("Registrar veterinario", [])
            formulario.agregarCampo("Nombre", "str", lambda x: len(x) >= 3 and x.isalpha(), 
            "El nombre no debe contener numeros y debe tener al menos 3 caracteres")
            formulario.agregarCampo("Contacto", "str", lambda x: len(x) == 8 or len(x) == 10 and x.isnumeric(),
            "El contacto debe tener 8 o 10 digitos y debe ser un numero")
            formulario.agregarCampo("Especialidad", "str", lambda x: x in especialidades,
            "La especialidad no es valida")
            formulario.agregarCampo("Licencia", "str", lambda x: len(x) == 10 and x.isnumeric(),
            "La licencia debe tener 10 digitos y debe ser un numero")

            # vamos a realizar un segundo formulario para obtener el horario de atención
            formularioHorario = Formulario("Horario de atención. ¿Tiene disponibilidad los siguientes dias?", [])
            for dia in DIAS:
                formularioHorario.agregarCampo(dia, "boolean")

            resultado = formulario.realizar()
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
            datos.guardar()
            pass
        elif opcion == "2":
            borrarConsola()
            veterinario = seleccionarVeterinario()
            borrarConsola()
            veterinarioSeleccionado = datos.obtener(veterinario)
            print("Veterinario seleccionado: " + veterinarioSeleccionado.nombre)
            formulario = Formulario("Modificar veterinario, Por favor ingrese los datos solicitados, deje en blanco para no modificar el valor", [])
            formulario.agregarCampo("Nombre", "str", lambda x: (len(x) >= 3 or len(x) == 0) and x.isalpha())
            formulario.agregarCampo("Contacto", "str", lambda x: (len(x) > 5 or len(x) == 0))
            formulario.agregarCampo("Especialidad", "str", lambda x: (x in especialidades or len(x) == 0))
            formulario.agregarCampo("Licencia", "str", lambda x: (len(x) == 10 or len(x) == 0) and x.isnumeric())

            resultado = formulario.realizar()
            horario = ""


            if input("¿Desea modificar tambien los horarios? (S/N)") == "S":
                formularioHorario = Formulario("Horario de atención. ¿Tiene disponibilidad los siguientes dias?", [])
                for dia in DIAS:
                    formularioHorario.agregarCampo(dia, "boolean")

                resultadoHorario =  formularioHorario.realizar()

                for dia in resultadoHorario:
                    if resultadoHorario[dia]:
                        horario += "1"
                    else:
                        horario += "0"
                datos.modificar(veterinario, "horario", horario)

            for key in resultado:
                if resultado[key] != "":
                    datos.modificar(veterinario, key, resultado[key])

            pass
        elif opcion == "3":
            borrarConsola()
            print("Consultar veterinarios")
            verVeterinario:Veterinario = datos.obtener(seleccionarVeterinario())
            borrarConsola()
            print("Nombre: " + verVeterinario.nombre)
            print("Contacto: " + verVeterinario.contacto)
            print("Especialidad: "+verVeterinario.especialidad)
            print("Licencia: " + verVeterinario.licencia)
            print("Horario de atención:")
            for dia in DIAS:
                if verVeterinario.obtenerDia(dia):
                    print(dia)
            input("Precione entre para volver ")
            pass
        elif opcion == "4":
            borrarConsola()
            print("Eliminacion de veterinario")
            veterinarioSeleccionado = seleccionarVeterinario()
            borrarConsola()
            print("¿Esta seguro de eliminar a "+ datos.obtener(veterinarioSeleccionado).nombre+"?")
            print("1) Si")
            print("2) No")
            response = input("Seleccione una opcion: ")
            if response == "1" or response == "Si" or response == "SI" or response == "si":
                datos.eliminar(veterinarioSeleccionado)
            datos.guardar()
            pass
        elif opcion == "5":
            break
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
            menuVeterinario(datos)
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