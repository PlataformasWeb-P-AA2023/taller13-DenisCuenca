from flask import Flask, render_template
import requests
import json
from .config import usuario, clave

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/departamentos")
def los_estudiantes():
    """
    """
    r = requests.get("http://localhost:8000/departamentos/",
                     auth=(usuario, clave))
    estudiantes = json.loads(r.content)['results']
    return render_template("templates/losestudiantes.html", estudiantes=estudiantes)


@app.route("/edificios")
def los_telefonos():
    """
    """
    r = requests.get("http://localhost:8000/edificios/",
                     auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    return render_template("templates/lostelefonos.html", datos=datos
                           )
