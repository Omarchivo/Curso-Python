from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return "<h1>Hola, buenos días</h1>"

@app.route("/adios")
def adios():
    return "<h2>Adios, hasta la próxima</h2>"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "<h2>La letra en la posición 5 del nombre es: {}".format(nombre[5])

#Resolución del ejercicio 1
@app.route("/longitud/<nombre>")
def longitud(nombre):
    return "<h2>El nombre {} tiene una longitud de {} letras</h2>".format(nombre, len(nombre))

#Resolución del ejercicio 2
@app.route("/edad/<nombre>/<edad>")
def edad(nombre, edad):
    return "<h2>{} tiene {} años</h2>".format(nombre, edad)

#Resolución del ejercicio 3
@app.route("/sumar/<numero1>/<numero2>")
def sumar(numero1, numero2):
    suma = int(numero1) + int(numero2)
    resultado = str(suma)
    return "<h2>La suma de {} y {} es igual a {}</h2>".format(numero1, numero2, resultado)

if __name__ == '__main__':
    app.run() #app.run(debug=True)