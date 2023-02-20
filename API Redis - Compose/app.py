from itertools import product
from flask import Flask,jsonify, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

from estudiante import estudiante

@app.route('/inicio')
def inicio():
    return jsonify({ "message": "Bienvenido"})

@app.route( '/demo')
def getEstudiantes():
    return jsonify({"estudiantes": estudiante, "message": "Estudent List's"})

#, methods=['GET']
@app.route( '/demo/greeting/<string:estudiante_codigo>', methods=['GET'] )
def getEstudiante(estudiante_codigo):
    estudianteFound = [estudiante for estudiante in estudiante if estudiante["codigo"]== estudiante_codigo ]
    if (len(estudianteFound) > 0 ):
        return jsonify({ "Datos_Estudiante": estudianteFound[0] })
    return jsonify({ "message": "Estudiante not Found"})

@app.route('/demo/register', methods=['POST'])
def addEstudiante():
    new_estudiante = {
        "codigo": request.json['codigo'],
        "name": request.json['name'],
        "email": request.json['email'],
        "carrera": request.json['carrera'],
        "nivel": request.json["nivel"]
    }
    estudiante.append(new_estudiante)
    return jsonify({"message": "Estudiante agregado Existosamente", "estudiante": estudiante})

if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)