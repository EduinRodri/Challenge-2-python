
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
1. Consultar Cliente por ID
2. Consultar Veterinario por ID
3. Modificar Cliente
4. Modificar Veterinario
'''

# Clases
class persona:
    def __init__(self, nombre, contacto, identidad):
        self.nombre = nombre
        self.contacto = contacto
        self.id = identidad


class cliente(persona):
    def __init__(self, nombre, contacto, identidad, dirección):
        super().__init__(nombre, contacto, identidad)
    pass

class veterinario(persona):
    def __init__(self, nombre, contacto, identidad, especialidad, licencia, horario):
        super().__init__(nombre, contacto, identidad)
    pass

class mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueño):
        pass

class servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        pass

class cita:
    def __init__(self, fecha, hora, servicio, veterinario, id_mascota):
        pass

def main():

    pass