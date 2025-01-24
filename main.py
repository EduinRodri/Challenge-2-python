# Constantes
import os
import platform


SEPARADOR_ELEMENTO = "~"
SEPARADOR_TABLA = "~~~"
PROPIEDAD = "|"
TITULO = "||"
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
        self.__nombre = nombre
        self.__contacto = contacto
        self.id = identidad
    
    def getNombre (self):
        return self.__nombre
    
    def getContacto (self):
        return self.__contacto
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setContacto(self, contacto):
        self.__contacto = contacto

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
                    split = tabla.split(TITULO)

                    if len(split) > 1:
                        titulo = split[0]
                        contenidoTexto = split[1]
                        contenido = contenidoTexto.split(SEPARADOR_ELEMENTO)
                        for elemento in contenido:
                            propiedades = elemento.split(PROPIEDAD)
                            if len(propiedades) > 1:
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
    
    def largo (self):
        return len(self.tablas[self.use])
    
    def agregar(self, elemento):
        self.tablas[self.use].append(elemento)

    def obtenerTabla (self):
        return self.tablas[self.use]


def mostrarTabla(tabla: list[Persona]):
    for i in range(len(tabla)):
        print(f"{i + 1}. {tabla[i].getNombre()}")


def mostrarServicios (servicios: list[Servicio]):
    for i in range(len(servicios)):
        servicio: Servicio = servicios[i]
        print(f"{i+1} - {servicio.getDescripcion()}")
        pass

def preguntar (pregunta: str):
    print(pregunta)
    print("1. Si")
    print("2. No")
    respuesta = input("Seleccione una opcion")
    if respuesta == "Si" or respuesta == "SI" or respuesta == "si" or respuesta == "1":
        return True
    else:
        return False

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
            menuServicios(datos)
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