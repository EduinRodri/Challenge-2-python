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
