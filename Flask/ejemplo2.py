from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def portada():
    return render_template("portada.html")

@app.route("/hola")
def hola():
    diccionario = {
        'nombre' : 'Omar',
        'edad' : '24',
        'color': 'Azul'
    }
    return render_template("hola.html", datos = diccionario)

@app.route("/colores")
def colores():
    lista_colores = ["Verde","Rojo","Amarillo","Azul"]
    return render_template("colores.html", colores = lista_colores)

@app.route("/frase/<texto>")
def frase(texto):
    return render_template("frase.html",tipo = texto)

if __name__ == '__main__':
    app.run()