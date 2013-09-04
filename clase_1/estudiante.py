class Estudiante(object):
	def __init__(self, nombre_r, edad_r):
		self.nombre = nombre_r
		self.edad = edad_r

	def hola(self):
		return "Mi nombre es %s y tengo %s"%(self.nombre, self.edad)
e = Estudiante("jesus",26)
s = e.hola()
lista = []
for estudiante in range(10):
	nombre = "Estudiante %s"% estudiante
	e = Estudiante(nombre,23)
	lista.append(e)


for estudiante in lista:
	if estudiante.nombre == "Estudiante 5":
		print "soy el 5"
	else:
		print "no soy el 5"
