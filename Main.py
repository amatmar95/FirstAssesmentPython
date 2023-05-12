## Escenario de Profesiones: Código 06

####  Aplicación principal

from flask import Flask, request, render_template
from profesiones.Profesion import *

app = Flask(__name__,template_folder='html')

@app.route("/")
def profesiones():
    return render_template("start_profesiones.html")

@app.route("/profesiones", methods=['POST'])
def mostrar_profesiones():
 # Obtener la profesión seleccionada por el usuario
    profesion = request.form["profesion"]
    area = request.form["area"]
 # Insertar el código aquí
    if profesion == "Ingeniero":
        puesto = request.form["sector"]
        profesion_ingresada = Ingeniero(profesion, area, puesto)
        
    elif profesion == "Medico":
        puesto = request.form["especialidad"]
        profesion_ingresada = Medico(profesion, area, puesto)

    elif profesion == "Abogado":
        puesto = request.form["rama"]
        profesion_ingresada = Abogado(profesion, area, puesto)


 # Renderizar la página de profesiones con la profesión seleccionada
    return render_template("profesiones.html", profesion=profesion_ingresada)


if __name__ == '__main__':
   app.run(debug=True)