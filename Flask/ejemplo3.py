from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/gracias')
def gracias():
    valor1 = request.args.get('nombre')
    valor2 = request.args.get('apellidos')
    return render_template('gracias.html',nombre=valor1, apellidos=valor2)

#SOLUCIÓN AL RETO PLANTEADO EN EL CURSO

@app.route('/validador')
def validador():
    return render_template('validador.html')


@app.route('/resultado')
def resultado():
    #Recupera el nombre que envia el usuario por el formulario
    nombre = request.args.get('nombre')

    #En esta línea se valida por medio de un ciclo for en todo lo que envio el usuario si encuentra una letra minuscula
    minuscula = any(letra.islower() for letra in nombre)

    #En esta línea se valida tambien por un ciclo for si existe algun digito en lo que envia el usuario por el formulario
    numero = any(letra.isdigit() for letra in nombre)

    #En esta línea valida que la primera letra es o no mayuscula
    mayuscula = nombre[0].isupper()

    #Finalmente esta variable (validar_todo) recupera el resultado booleano de todas las validaciones anteriores
    validar_todo = minuscula and numero and mayuscula

    return render_template('resultado.html', validar_todo = validar_todo, minuscula = minuscula, numero = numero, mayuscula = mayuscula)

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('pagina404.html'),404

if __name__ == '__main__':
    app.run(debug = True)