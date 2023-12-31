from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'

class Formulario(FlaskForm):
    nombre = StringField('Nombre', validators = [DataRequired()])
    edad = BooleanField('¿Eres mayor de edad?')
    sexo = RadioField('Sexo:', choices=[('h','Hombre'), ('m','Mujer')])
    color = SelectField('Color favorito:',
                            choices = [('r','Rojo'),('v','Verde'),('a','Azul')])
    comentario = TextAreaField()
    boton = SubmitField('Enviar')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/datos', methods=['GET','POST'])
def datos():
    miformulario = Formulario()
    if miformulario.validate_on_submit():
        session['nombre'] = miformulario.nombre.data
        session['edad'] = miformulario.edad.data
        session['sexo'] = miformulario.sexo.data
        session['color'] = miformulario.color.data
        session['comentario'] = miformulario.comentario.data
        return redirect(url_for('informacion'))

    return render_template('datos.html',formulario = miformulario)

if __name__ == '__main__':
    app.run(debug = True)