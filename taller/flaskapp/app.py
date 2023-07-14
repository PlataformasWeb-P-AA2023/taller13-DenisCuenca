from flask import Flask, render_template
import requests
import json
from .config import usuario, clave

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/departamentos")
def departamentos():
    """
    """
    r = requests.get("http://localhost:8000/departamentos/",
                     auth=(usuario, clave)).json()
    return render_template("list.html", datos=r)


@app.route("/edificios")
def edificios():
    """
    """
    r = requests.get("http://localhost:8000/edificios/",
                     auth=(usuario, clave)).json()
    return render_template("list.html", datos=r
                           )
