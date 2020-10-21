from flask import Flask, request, jsonify

class Estudiante:
	def __init__(self, carnet, nombre):
		self.carnet = carnet
		self.nombre = nombre



app = Flask(__name__)

@app.route('/misDatos', methods=['GET'])
#Método para hacer la autenticación del usuario
def devolverDatos():
	if request.method == 'GET':
		return {
    	'id' :"Carnet",
    	'nombre' :"Diego Abraham Robles Meza"
    	}

@app.route("/")
def index():
	return ""

if __name__ == "__main__":
	app.run(threaded = True,port = 8000, debug = True)