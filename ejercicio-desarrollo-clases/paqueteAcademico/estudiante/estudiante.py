class Estudiante(object):

	def __init__(self, nombre, nota1, nota2, nota3):
		self.nombre = nombre
		self.nota1 = float(nota1)
		self.nota2 = float(nota2)
		self.nota3 = float(nota3)
		self.promedio = 0.0

	def setNombre(self, n):
		self.nombre = n

	def getNombre(self):
		return self.nombre

	def setNota1(self, n):
		self.nota1 = n

	def getNota1(self):
		return self.nota1

	def setNota2(self, n):
		self.nota2 = n

	def getNota2(self):
		return self.nota2	

	def setNota3(self, n):
		self.nota3 = n

	def getNota3(self):
		return self.nota3

	def CalcularPromedio(self, nota1, nota2, nota3):
		self.promedio = (nota1 + nota2 + nota3) / 3
	
	def obtenerPromedio(self): 
		return self.promedio	

	def __str__(self):
		return "%-10s : %-4.2f\n" % (self.getNombre(), self.obtenerPromedio())
