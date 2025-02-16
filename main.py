# Constantes
from datetime import date
import os
import platform

SEPARADOR_ELEMENTO = "~"
SEPARADOR_TABLA = "~~~"
PROPIEDAD = "|"
HEADER = "||"
AUTOINCREMENT = "(]"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
CARACTERES_RECERVADOS = [
    SEPARADOR_ELEMENTO, PROPIEDAD, AUTOINCREMENT
]


MENU_PRINCIPAL = '''
====Bienvenido a Huella Feliz====
1. Clientes
2. Veterinarios
3. Mascotas
4. Servicios
5. Agendar citas
6. Historial de citas (General)
7. Terminar ciclo
8. Salir
'''

MENU_CLIENTE = '''
===Cliente===
1. Registrar cliente
2. Modificar cliente
3. Consultar clientes
4. Eliminar cliente
5. Salir
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
5. Salir
'''

MENU_SERVICIOS = '''
1. Ver servicios
2. Registrar Servicio
3. Modificar Servicio
4. Eliminar Servicio
5. Salir
'''

MENU_AGENDAR_CITA = '''
===Agendar Cita===
1. Seleccionar Fecha
2. Seleccionar Veterinario
3. Seleccionar Servicio
4. Seleccionar Mascota
5. Seleccionar Cliente
6. Aceptar
7. Cancelar
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
        self.__nombre = nombre
        self.__contacto = contacto
        self.id = identidad
    # se definiran los geters y seters 
    def getNombre (self):
        return self.__nombre
    
    def getContacto (self):
        return self.__contacto
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setContacto(self, contacto):
        self.__contacto = contacto
    # ? La funcion toArray esta presente en todas las clases que se almacenan en los datos 
    def toArray (self):
        return [self.__nombre, self.__contacto, str(self.id)]

class Cliente(Persona):
    def __init__(self, nombre, contacto, identidad, direccion):
        super().__init__(nombre, contacto, identidad)
        self.__direccion = direccion
    
    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def toArray(self):
        array = super().toArray()
        array.append(self.__direccion)
        return array
    


class Veterinario(Persona):
    def __init__(self, nombre, contacto, identidad, especialidad, licencia, horario):
        super().__init__(nombre, contacto, identidad)
        self.__especialidad = especialidad
        self.__licencia = licencia
        self.__horario = horario
    
    def getEspecialidad(self):
        return self.__especialidad

    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad

    def getLicencia(self):
        return self.__licencia

    def setLicencia(self, licencia):
        self.__licencia = licencia

    def getHorario(self):
        return self.__horario

    def setHorario(self, horario):
        self.__horario = horario
    
    def obtenerDia (self, dia: str):
        index = DIAS.index(dia)
        if self.__horario[index] == "1":
            return True
        return False
    
    def toArray(self):
        array = super().toArray()
        array.append(self.__especialidad)
        array.append(self.__licencia)
        array.append(self.__horario)
        return array
            

# * La clase Mascota en adelante no son extenciones de persona pero esta, servicios y citas se toman como tal en
# * la clase Datos
class Mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueno):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__identidad = identidad
        self.__dueno = dueno

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie

    def getRaza(self):
        return self.__raza

    def setRaza(self, raza):
        self.__raza = raza

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getIdentidad(self):
        return self.__identidad

    def setIdentidad(self, identidad):
        self.__identidad = identidad

    def getDueno(self):
        return self.__dueno

    def setDueno(self, dueno):
        self.__dueno = dueno

    def toArray(self):
        return [self.__nombre, self.__especie, self.__raza, self.__edad, self.__identidad, self.__dueno]


class Servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__duracion = duracion
        self.__costo = costo
        self.__frecuencia = frecuencia
    
    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getDuracion(self):
        return self.__duracion

    def setDuracion(self, duracion):
        self.__duracion = duracion

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo

    def getFrecuencia(self):
        return self.__frecuencia

    def setFrecuencia(self, frecuencia):
        self.__frecuencia = frecuencia
    
    def toArray(self):
        return [self.__tipo, self.__descripcion, self.__duracion, self.__costo, self.__frecuencia]


class Cita:
    def __init__(self, fecha:str, hora, servicio, veterinario, id_mascota):
        self.__fecha = fecha
        self.__hora = hora
        self.__servicio = servicio
        self.__veterinario = veterinario
        self.__id_mascota = id_mascota
        try:
            formato = fecha.split("@")
            self.__ciclo = int(formato[0])
            self.__dia = int(formato[1])
        except (ValueError, IndexError):
            print("Hay un dato corrupto en las fechas de las citas por favor revise su base de datos o reiniciela")
            self.__ciclo = 0
            self.__dia = 0

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha:str):
        self.__fecha = fecha
        formato = fecha.split("@")
        self.__ciclo = formato[0]
        self.__dia = formato[1]
    
    def getDia (self):
        return int(self.__dia)

    def setDia (self, dia):
        self.__dia = dia
        self.__fecha = str(self.__ciclo) + "@" + str(dia)
    
    def getCiclo (self):
        return self.__ciclo
    
    def setCiclo(self, ciclo):
        self.__ciclo = ciclo
        self.__fecha = str(ciclo) + "@" + str(self.__dia)

    def getHora(self):
        return self.__hora

    def setHora(self, hora):
        self.__hora = hora

    def getServicio(self):
        return self.__servicio

    def setServicio(self, servicio):
        self.__servicio = servicio

    def getVeterinario(self):
        return self.__veterinario

    def setVeterinario(self, veterinario):
        self.__veterinario = veterinario

    def getIdMascota(self):
        return self.__id_mascota

    def setIdMascota(self, id_mascota):
        self.__id_mascota = id_mascota
    
    def toArray(self):
        return [self.__fecha, self.__hora, self.__servicio, self.__veterinario, self.__id_mascota]
    
# * Este error personalizado debe saltar cuando el usuario dijita un caracter apartado por el sistema
# Char = Character que significa caracter
# Error de caracter recervado
class RecervedCharError (Exception):
    def __init__(self):
        mensaje = "Error: No se admiten los siguientes caracteres para los valores de entrada: "
        for caracter in CARACTERES_RECERVADOS:
            mensaje += f"{caracter}, "
        super().__init__(mensaje)

# * Esta clase es utilizada por Formulario como los campos que se van a preguntar
# Esta clase usa diferentes tipos, aqui se definen y cual es su funcion
# str (o cualquier otro no admitido): Recibe cualquier cosa que escriba el usuario y se le devolvera al programador un string
# int: Recibira unicamente numeros del usuario y se le entregara al programador un int
# float: Recibira unicamente numeros del usuario y se entregara al programador un float
# boolean: Hara una pregunta de si y no al usuario y se devolvera al programador True si respondio si y False si respondio no
class PropiedadFormulario:
    def __init__(self, titulo, tipo, callback = None, invalido = ""):
        self.titulo = titulo
        self.tipo = tipo
        self.callback = callback
        self.invalido = invalido


# * La clase formulario se usa para facilitar las peticiones de datos al usuario
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
    
    def modificarCampo(self, titulo:str, tipo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                campo.tipo = tipo
    
    def eliminarCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                self.__campos.remove(campo)
    
    def obtenerCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                return campo
    
    # * Esta funcion es importante, se debe usar para realizar todo el formulario y pedir la informacion al usuario
    def realizar(self):
        print(self.__titulo)
        formulario: dict[str, str | int | float | bool] = {}
        for campo in self.__campos:
            while True:
                texto = campo.titulo + ": "
                error = "Valor incorrecto"
                if campo.tipo == "boolean":
                    print(campo.titulo)
                    print("1. Sí")
                    print("2. No")
                    texto = "Respuesta: "
                respuesta = input(texto)
                try:
                    valorCorrecto = True
                    valorIngresar = ""
                    
                    # validamos que el campo ingresado sea un valor admitido por el formulario
                    if campo.tipo == "int":
                        if respuesta.isnumeric():
                            valorIngresar = int(respuesta)
                        else:
                            valorCorrecto = False
                            error = "El valor debe ser un número entero"
                    elif campo.tipo == "float":
                        if isFloat(respuesta):
                            valorIngresar = float(respuesta)
                        else:
                            valorCorrecto = False
                            error = "El valor debe ser un numero decimal"
                    elif campo.tipo == "boolean":
                        if respuesta == "1" or respuesta == "Si" or respuesta == "si" or respuesta == "SI":
                            valorIngresar = True
                        elif respuesta == "2" or respuesta == "No" or respuesta == "no" or respuesta == "NO":
                            valorIngresar = False
                        else: 
                            valorCorrecto = False
                            
                    else:
                        for caracter in CARACTERES_RECERVADOS:
                            if caracter in respuesta:
                                raise RecervedCharError
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
                except (ValueError, RecervedCharError) as e:
                    print(e)
                    
                
        return formulario

    
# * La clase datos es la encargada de almacenar la informacion que ingrese el usuario
class Datos:
    use = ""
    __state = "fine"
    __ciclo = 0
    __tablas: dict[str, list[Persona]] = {
        "clientes": [],
        "veterinarios": [],
        "mascotas": [],
        "servicios": [],
        "citas": []
    }
    __autoincrement: dict[str, int] = {
        "clientes": 0,
        "veterinarios": 0,
        "mascotas": 0,
        "servicios": 0,
        "citas": 0,
        "ciclo": 0
    }
    def __init__(self):
        try:
            with open("datos.txt", "r") as datos:
                text = datos.read()
                if text != "":
                    # Primero separamos los datos por cada tabla
                    tablasContenido = text.split(SEPARADOR_TABLA)
                    for tabla in tablasContenido:
                        # A cada tabla la separamos por header y contenido
                        split = tabla.split(HEADER)

                        if len(split) > 1:
                            # Dividimos el header partiendolo para conseguir de un lado el titulo y del otro el autoincrement de la id
                            header = split[0].split(AUTOINCREMENT)
                            titulo = header[0]
                            autoincrement = int(header[1])
                            contenidoTexto = split[1]
                            contenido = contenidoTexto.split(SEPARADOR_ELEMENTO)

                            self.__autoincrement[titulo] = autoincrement

                            for elemento in contenido:
                                propiedades = elemento.split(PROPIEDAD)
                                if len(propiedades) > 1:
                                    if titulo == "ciclo":
                                        self.__ciclo = int(propiedades[0])
                                    elif titulo == "clientes":
                                        cliente = Cliente(propiedades[0], propiedades[1], int(propiedades[2]), propiedades[3])
                                        self.__tablas["clientes"].append(cliente)
                                    elif titulo == "veterinarios":
                                        veterinario = Veterinario(propiedades[0], propiedades[1], int(propiedades[2]), propiedades[3], propiedades[4], propiedades[5])
                                        self.__tablas["veterinarios"].append(veterinario)
                                    elif titulo == "mascotas":
                                        mascota = Mascota(propiedades[0], propiedades[1], propiedades[2], propiedades[3], int(propiedades[4]), int(propiedades[5]))
                                        self.__tablas["mascotas"].append(mascota)
                                    elif titulo == "servicios":
                                        servicio = Servicio(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4])
                                        self.__tablas["servicios"].append(servicio)
                                    elif titulo == "citas":
                                        cita = Cita(propiedades[0], propiedades[1], propiedades[2], int(propiedades[3]), int(propiedades[4]))
                                        self.__tablas["citas"].append(cita)
        except FileNotFoundError:
            with open("datos.txt", "w") as datos:
                print("Archivo de datos creado correctamente vuelva a ejecutar el programa")
                self.__state = "reload"

        except ValueError:
            print("Parece que la base de datos esta corrupta vuelva a intentarlo")
            self.__state = "error"

    def getCiclo (self):
        return self.__ciclo
    
    def setCiclo (self, num:int):
        self.__ciclo = num

    def obtenerEstado (self):
        return self.__state

    def obtener(self, index: int):
        result = self.__tablas[self.use][index]
        return result
    
    def guardar(self):
        with open("datos.txt", "w") as datos:
            datos.write(f"ciclo{AUTOINCREMENT}0{HEADER}{self.__ciclo}{PROPIEDAD}{SEPARADOR_ELEMENTO}{SEPARADOR_TABLA}")
            for key in self.__tablas:
                texto = key + AUTOINCREMENT + str(self.__autoincrement[key]) + HEADER
                for elemento in self.__tablas[key]:
                    iterable = elemento.toArray()
                    for propiedad in iterable:
                        texto += propiedad + PROPIEDAD
                    texto += SEPARADOR_ELEMENTO
                texto += SEPARADOR_TABLA
                datos.write(texto)

    def eliminar(self, index: int):
        self.__tablas[self.use].pop(index)
    
    def largo (self):
        return len(self.__tablas[self.use])
    
    def agregar(self, elemento: Persona):
        elemento.id = self.__autoincrement[self.use]
        self.__autoincrement[self.use] += 1
        self.__tablas[self.use].append(elemento)

    def obtenerTabla (self):
        return self.__tablas[self.use]

    def obtenerPorId (self, id):
        resultado: Persona
        if self.use == "servicios" or self.use == "citas":
            return self.obtener(id)
        for element in self.__tablas[self.use]:
            if element.id == id:
                resultado = element
                pass
            pass
        return resultado
    
    def eliminarPorId (self, id):
       for i, element in enumerate(self.__tablas[self.use]):
            if element.id == id:
                self.__tablas[self.use].pop(i)
                pass
            pass

    
    def horarioVeterinario(self, idVeterinario: int):
        # TODO: Probar que el sistema de horario funcione
        horario: list[bool] = [
            False, False, False, False, False, False
        ]
        for i in len(self.__tablas['citas']):
            cita: Cita = self.__tablas['cita'][i]
            if cita.getVeterinario() == idVeterinario and self.__ciclo == cita.getCiclo():
                horario[cita.getFecha()] = True
        return horario
    

    def getDiaHorarioVeterinario (self, idVeterinario: int, dia: int):
        retorno = False
        for i in len(self.__tablas['citas']):
            cita: Cita = self.__tablas['cita'][i]
            if cita.getVeterinario() == idVeterinario and self.__ciclo == cita.getCiclo() and cita.getDia() == dia:
                retorno = True
        return retorno


# * esta funcion define si la fecha1 es una fecha anterior a fecha2
def fechaAnterior(fecha1: date, fecha2: date):
    if fecha1.year < fecha2.year:
        return True
    elif fecha1.month < fecha2.month and fecha1.year == fecha2.year:
        return True
    elif fecha1.day < fecha2.day and fecha1.month == fecha2.month and fecha1.month == fecha2.month:
        return True
    return False
        
# * Esta funcion se usa para mostrar una tabla que sea extencion de persona o la tabla mascota
def mostrarTabla(tabla: list[Persona]):
    for i in range(len(tabla)):
        print(f"{i + 1}. {tabla[i].getNombre()}")

# * Esta funcion se usa para mostrar una lista de servicios
def mostrarServicios (servicios: list[Servicio]):
    for i in range(len(servicios)):
        servicio: Servicio = servicios[i]
        print(f"{i+1} - {servicio.getDescripcion()}")
        pass

# * Esta funcion realiza una pregunta de si y no al usuario y devuelve True si la respuesta es si y False si es no
def preguntar (pregunta: str):
    print(pregunta)
    print("1. Si")
    print("2. No")
    respuesta = input("Seleccione una opcion")
    if respuesta == "Si" or respuesta == "SI" or respuesta == "si" or respuesta == "1":
        return True
    else:
        return False

def pedirNumero (pregunta: str, max: int | float = 0, min: int | float = 0):
    retorno = 0
    while True:
        opcion = input(pregunta)
        if opcion.isnumeric():
            opcion = int(opcion)
        elif isFloat(opcion):
            opcion = float(opcion)
        else: 
            print("Opcion invalida")
            continue

        if (opcion > max and max > 0) or opcion < min :
            print("Opcion invalida")
            continue
        retorno = opcion
        break
    return retorno



def menuVeterinario(datos: Datos):
    datos.use = "veterinarios"
    especialidades = ["Cardiologia", "Dermatologia", "Neurologia", "Oftalmologia", "Oncologia", "Ortopedia"]

    def seleccionarVeterinario():
        print("Seleccione el veterinario")
        mostrarTabla(datos.obtenerTabla())
        while True:
            try:
                opcion = input("Veterinario: ")
                if opcion.isnumeric(): 
                    veterinario = int() - 1
                    break
                else:
                    raise ValueError("Valor incorrecto digitado")
            except ValueError as e:
                print(e)

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
            veterinarioSeleccionado: Veterinario = datos.obtener(veterinario)
            print("Veterinario seleccionado: " + veterinarioSeleccionado.getNombre())
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
                veterinarioSeleccionado.setHorario(horario)

            listLambda = {
                "Nombre": lambda x: veterinarioSeleccionado.setNombre(x),
                "Contacto": lambda x: veterinarioSeleccionado.setContacto(x),
                "Especialidad": lambda x: veterinarioSeleccionado.setEspecialidad(x),
                "Licencia": lambda x: veterinarioSeleccionado.setLicencia(x)
            }

            for key in resultado:
                if resultado[key] != "":
                    listLambda[key](resultado[key])


            pass
        elif opcion == "3":
            borrarConsola()
            print("Consultar veterinarios")
            verVeterinario:Veterinario = datos.obtener(seleccionarVeterinario())
            borrarConsola()
            print("Nombre: " + verVeterinario.getNombre())
            print("Contacto: " + verVeterinario.getContacto())
            print("Especialidad: "+verVeterinario.getEspecialidad())
            print("Licencia: " + verVeterinario.getLicencia())
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
            print("¿Esta seguro de eliminar a "+ datos.obtener(veterinarioSeleccionado).getNombre()+"?")
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
        


def menuServicios (datos: Datos):
    datos.use = "servicios"
    borrarConsola()
    
    while True:
        print(MENU_SERVICIOS)
        opcion = input("Seleccione una opcion: ")

        def seleccionarServicio (needIndex = False):
            mostrarServicios(datos.obtenerTabla())
            resultado = False
            while True:
                select = input("Seleccione un servicio o precione enter sin escribir nada para ir atras")
                if select == "":
                    borrarConsola()
                    break
                elif select.isnumeric():
                    borrarConsola()
                    index = int(select)-1
                    servicioSeleccionado: Servicio = datos.obtener(index)
                    resultado = servicioSeleccionado
                    if needIndex:
                        resultado = index
                    break
                else:
                    print("Opcion no valida, por favor, ingrese un numero o de enter sin escribir nada")
                    pass
                pass
            return resultado

        if opcion == "1":
            borrarConsola()
            servicioSeleccionado = seleccionarServicio()
            if servicioSeleccionado:
                print("==== Informacion del servicio ====")
                print(f"Descripcion: {servicioSeleccionado.getDescripcion()}")
                print(f"Tipo: {servicioSeleccionado.getTipo()}")
                print(f"Duracion: {servicioSeleccionado.getDuracion()} minutos")
                print(f"Frecuencia {servicioSeleccionado.getFrecuencia()} meses")
                print(f"Costo: ${servicioSeleccionado.getCosto()}")
                input("Precione enter para continuar ")
        elif opcion == "2":
            # Tenemos que hacer un formulario de registro
            borrarConsola()
            formulario = Formulario("=== Registro de Servicio ===", [])
            formulario.agregarCampo('Ingrese el tipo de servicio', 'str', lambda x: len(x) >= 3, 'Por favor digite un campo con al menos 3 caracteres')
            formulario.agregarCampo('Descripcion del servicio', 'str', lambda x: len(x) >= 3, 'Por favor digite un campo con al menos 3 caracteres')
            formulario.agregarCampo('Duracion en minutos del servicio', 'float')
            formulario.agregarCampo('Frecuencia optima del servicio en meses', 'float')
            formulario.agregarCampo('Costo del servicio', 'float')

            realizar = formulario.realizar()
            tipo = realizar['Ingrese el tipo de servicio']
            descripcion = realizar['Descripcion del servicio']
            duracion = realizar['Duracion en minutos del servicio']
            frecuencia = realizar['Frecuencia optima del servicio en meses']
            costo = realizar['Costo del servicio']

            nuevoServicio = Servicio(tipo, descripcion, duracion, costo, frecuencia)
            datos.agregar(nuevoServicio)
            datos.guardar()
            pass
        elif opcion == "3":
            borrarConsola()
            servicioSeleccionado = seleccionarServicio()
            if servicioSeleccionado:
                formulario = Formulario("=== Modificacion de servicio === \n (Escriba enter sin nada para dejar el servicio tal como estaba)", [])
                formulario.agregarCampo("Tipo", 'str', lambda x: len(x) == 0 or len(x) > 3, 'Por favor digite un campo con al menos tres caracteres')
                formulario.agregarCampo("Descripcion", 'str', lambda x: len(x) == 0 or len(x) > 3, 'Por favor digite un campo con al menos tres caracteres')
                formulario.agregarCampo("Duracion", 'float')
                formulario.agregarCampo('Frecuencia', 'float')
                formulario.agregarCampo("Costo", 'float')

                realizar = formulario.realizar()

                listLambda = {
                    "Tipo": lambda x: servicioSeleccionado.setTipo(x),
                    "Descripcion": lambda x: servicioSeleccionado.setDescripcion(x),
                    "Duracion": lambda x: servicioSeleccionado.setDuracion(x),
                    "Frecuencia": lambda x: servicioSeleccionado.setFrecuencia(x),
                    "Costo": lambda x: servicioSeleccionado.setCosto(x)
                }

                for element in realizar:
                    if listLambda[element]:
                        listLambda[element](realizar[element])
                        pass
                    pass
                pass
            pass
        elif opcion == "4":
            borrarConsola()
            indexServicioSeleccionado = seleccionarServicio()
            if indexServicioSeleccionado:
                deseaEliminar = preguntar("¿Esta seguro de eliminar este servicio?")
                if deseaEliminar:
                    datos.eliminar(indexServicioSeleccionado)
                    pass
        elif opcion == "5":
            break
        else:
            print("Opcion no valida")
        pass


    pass


def agendarCitas (datos: Datos):
    # TODO: Realizar el sistema de agendado de citas tomando en cuenta el horario del veterinario
    cliente: Cliente = None
    servicio: Servicio = None
    veterinario: Veterinario = None
    mascota: Mascota = None
    fechaDeCita = -1
    borrarConsola()

    def asignarVeterinario (opcion):
        borrarConsola()
        datos.use = "veterinarios"
        veterinarios: list[Veterinario] = datos.obtenerTabla()
        veterinariosDisponibles: list[Veterinario] = []
        if opcion == -1:
            veterinariosDisponibles = veterinarios
        else:
            for personal in veterinarios:
                if personal.obtenerDia(DIAS[opcion]) and not datos.getDiaHorarioVeterinario(personal.id, opcion):
                    veterinariosDisponibles.append(personal)
                    # Estos pass son solo para guiarme yo, por fis no lo quites
                    pass
                pass
        # Supongo que ahora toca informar al usuario... Bueno aqui va
        print("Por favor seleccione un veterinario de los disponibles")
        for i, personal in enumerate(veterinariosDisponibles):
            print(f"{i+1}. {personal.getNombre()}")
        seleccion: int = pedirNumero("Escriba aqui su eleccion: ", len(veterinariosDisponibles), 1) - 1 
        borrarConsola()
        return veterinariosDisponibles[seleccion]
    
    def asignarFecha (horario: list[bool] = []):
        # Al final decidi no agregar lo de la hora, me complique mucho aun sin la hora... 
        print("Seleccione un dia para la cita durante la semana en curso")

        # se verifica que se envia un horario valido para la revision del veterinario especifico
        if len(horario) > 0 and len(horario) == len(DIAS):
            indexDay = 1
            listIndex: list[int] = []
            for i, dia in enumerate(DIAS):
                if horario[i]:
                    print(f"{indexDay}. {dia}")
                    indexDay += 1
                    listIndex.append(i)
            opcion:int = pedirNumero("Eleccion: ", len(listIndex)+1, 1) - 1
            return listIndex[opcion]
        else:
            for i, dia in enumerate(DIAS):
                print(f"{i+1}. {dia}")
            opcion: int = pedirNumero("Eleccion: ", len([DIAS])+1, 1) - 1
            return opcion

    while True:
        print(MENU_AGENDAR_CITA)
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            # * En seleccionar "Dia" tambien ira el seleccionar hora de la cita... Aunque aun no se si incluir esto
            fechaDeCita = asignarFecha()
            if veterinario is None:
                veterinario = asignarVeterinario(fechaDeCita)
            else:
                if veterinario.obtenerDia(DIAS[fechaDeCita]) and not datos.getDiaHorarioVeterinario(veterinario.id, fechaDeCita):
                    borrarConsola()
                else:
                    veterinario = asignarVeterinario(fechaDeCita)
                    
        elif opcion == "2":
            # * Seleccionar un veterinario implica seleccionar un dia que este trabaje
            if fechaDeCita > -1:
                reasignar = preguntar("¿Desea seleccionar un veterinario en la misma fecha que eligio?")
                if reasignar:
                    asignarVeterinario(fechaDeCita)
                else:
                    asignarVeterinario(-1)
            else:
                veterinario = asignarVeterinario(-1)
                horario = datos.horarioVeterinario(veterinario.id)
                fechaDeCita = asignarFecha(horario)
                borrarConsola()
        elif opcion == "3":
            print("Seleccionar Servicio")
            datos.use = "servicios"
            servicios: list[Servicio] = datos.obtenerTabla()
            mostrarServicios(servicios)
            opcion = pedirNumero("Eleccion: ", len(servicios)+1, 1) - 1
            servicio = servicios[opcion]
        elif opcion == "4":
            # * Al seleccionar una mascota se debe seleccionar automaticamente su dueño como cliente
            mascotas: list[Mascota] = []
            if cliente is not None:
                pregunta = preguntar("Se a seleccionado un cliente, ¿desea seleccionar una mascota de ese cliente?")
                if not pregunta:
                    cliente = None
            if cliente is None:
                print("Seleccionar Mascota")
                datos.use = "mascotas"
                mascotas = datos.obtenerTabla()
            else:
                datos.use = "mascotas"
                for element in datos.obtenerTabla():
                    element: Mascota
                    if element.getDueno() == cliente.id:
                        mascotas.append(element)
                        pass
                    pass
            
            mostrarTabla(mascotas)
            opcion = pedirNumero("Eleccion: ", len(mascotas)+1, 1) - 1
            mascota = mascotas[opcion]
            if cliente is None:
                datos.use = "clientes"
                cliente = datos.obtenerPorId(mascota.getDueno())
        elif opcion == "5":
            # * Recuerda que si se selecciona un cliente el rango de busqueda de las mascotas se reduce a las de ese cliente
            print("Seleccionar Cliente")
        
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        pass


    pass

# Main Programa
def main():
    while True:
        datos = Datos()
        # determinamos si la base de datos cargo correctamente
        if datos.obtenerEstado() != "fine":
            break
        borrarConsola()
        print(MENU_PRINCIPAL)
        opcion = input("Seleccione una opción: ")
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
            menuServicios(datos)
            pass
        elif opcion == "5":
            agendarCitas(datos)
            pass
        elif opcion == "6":
            # TODO: Hay que realizar el menu de historial de citas
            print("Historial de citas")
            pass
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()