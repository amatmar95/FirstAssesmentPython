## Escenario de Profesiones: Código 06

# Usted ha sido contratado para trabajar como `python developer` en la secretaría de empleo de su localidad.

# Se controlará la información de empleo por profesiones.

# Usted iniciará un proyecto que incluirá la elaboración de `site` en Internet para la gestión de  la información de empleo de las profesiones.

# Las profesiones que se gestionarán inicialmente son Ingenieros, Médicos y Abogados, pero próximamente se añadirán otra profesiones hasta cubrir todos los sectores económicos y sociales.

# Debe crear el proyecto de iniciación para comenzar a desarrollar en las siguientes jornadas toda la aplicación.

# Hoy deberá entregar el proyecto web, con la jerarquía de clases, y con el funcionamiento de la primera página web; incluyendo toda la información proporcionada en este documento. Solo añadirá lo faltante.

# - Jerarquía de clases

# ```
# Profesiones: Ingeniero, Médico y Abogado.
# ```


####  Aplicación principal

from flask import Flask, request, render_template

app = Flask(__name__,template_folder='html')

@app.route("/")
def profesiones():
    return render_template("start_profesiones.html")

@app.route("/profesiones", methods=['POST'])
def mostrar_profesiones():
 # Obtener la profesión seleccionada por el usuario

 # Insertar el código aquí
        
 # Renderizar la página de profesiones con la profesión seleccionada
 return render_template("profesiones.html", profesión=profesión_ingresada)


if __name__ == '__main__':
   app.run(debug=True)





