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
    	'Carnet' :"201901429",
    	'nombre' :"Diego Abraham Robles Meza"
    	}

@app.route("/inversor", methods=['POST'])
def prueba():
	if request.method == 'POST':
		return "Inversando";

@app.route("/")
def index():
	return ""

if __name__ == "__main__":
	app.run(threaded = True,port = 8000, debug = True)