Persona: Clase base para Cliente y Veterinario.
	- nombre
	- contacto
	- id
Cliente y Veterinario: Heredan de Persona y tienen atributos específicos.
	- Cliente:
		- Direccion
	- Veterinario:
		- Especialidad
		- Licencia
		- Horario
Mascota: Contiene el nombre, especie, raza, edad, id, dueño.
Servicio: Representa un servicio de veterinaria, como consulta o vacunación.
	- Tipo de servicio: Especifica qué tipo de servicio se va a realizar (por ejemplo, consulta, vacunación, cirugía, 	etc.).
	- Descripción: Una breve descripción del servicio, que puede incluir detalles sobre lo que implica (por ejemplo, 	"Examen de salud general", "Vacunación contra la rabia", etc.).
	- Duración: Duración estimada del servicio en minutos.
	- Costo: El costo del servicio, que puede variar dependiendo del tipo (por ejemplo, una consulta básica puede 	costar menos que una cirugía).
	- Frecuencia: En algunos casos, puede ser útil saber si el servicio se realiza de manera regular (por ejemplo, 	"Vacunación anual").

Cita: Registra la fecha, hora, servicio y veterinario asignado a una mascota, id de mascota.