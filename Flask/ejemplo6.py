from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'

class Formulario(FlaskForm):
    nombre = StringField("Introduce tu nombre")
    boton = SubmitField("Enviar mensaje")

# SOLUCIÓN EJERCICIO PROPUESTO, AJUSTAR EL EJEMPLO PARA QUE EL MENSAJE MUESTRE EL NOMBRE INGRESADO

@app.route("/mensaje", methods=['GET','POST'])
def mensaje():
    formulario = Formulario()

    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        flash("Gracias {} por pulsar este botón".format(nombre))
        return redirect(url_for('mensaje'))
    return render_template('mensaje.html', formulario = formulario)

if __name__ == '__main__':
    app.run(debug = True)