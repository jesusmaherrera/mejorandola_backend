class Estudiante(object):
	def __init__(self, nombre_r, edad_r):
		self.nombre = nombre_r
		self.edad = edad_r

	def hola(self):
		return "Mi nombre es %s y tengo %s"%(self.nombre, self.edad)
e = Estudiante("jesus",26)
s = e.hola()
print s