
class Estudiante:
	def __init__(self, carnet, nombre):
		self.carnet = carnet
		self.nombre = nombre

	def dump(self, carnet, nombre ):
    	return {
    	'Carnet' :self.carnet,
    	'Nombre' :self.nombre
    			}

alumno = Estudiante("201901429","Diego Abraham Robles Meza")