from paqueteAcademico.estudiante.estudiante import *
from paqueteAcademico.manejoArchivos.archivo import * 

a = MiArchivo()
a2 = MiArchivoEscribir()

lista = a.obtenerInformacion()
lista = [l.split("|") for l in lista]

lista = lista[1:]

for d in lista:
#	print(d)
	e = Estudiante(d[0], d[1], d[2], d[3])
	e.CalcularPromedio(float(d[1]), float(d[2]), float(d[3]))
	print(e)
	a2.agregarInformacion(e)