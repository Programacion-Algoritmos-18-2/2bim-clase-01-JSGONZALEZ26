import codecs

class MiArchivo:

	def __init__(self):
		self.archivo = codecs.open("paqueteAcademico/Archivos/informacion.csv", "r")

	def obtenerInformacion(self):
		return self.archivo.readlines()

	def cerrarArchivo(self):
		self.archivo.close()

class MiArchivoEscribir:

	def __init__(self):
		self.archivo = codecs.open("paqueteAcademico/Archivos/informacion2.csv", "a")

	def agregarInformacion(self, e):
		self.archivo.write("%-10s : %-4.2f\n" % (e.getNombre(), e.obtenerPromedio()))

	def cerrar_archivo(self):
		self.archivo.close()