from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/misDatos', methods=['GET'])
#Método para hacer la autenticación del usuario
def devolverDatos():
	if request.method == 'GET':

		return {
    	'Carné' :"201901429",
    	'Nombre' : "Diego Abraham Robles Meza"
    	}

@app.route("/")
def index():
	return ""

if __name__ == "__main__":
	app.run(threaded = True,port = 8000, debug = True)