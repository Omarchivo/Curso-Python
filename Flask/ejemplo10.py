from flask_bcrypt import Bcrypt

generador = Bcrypt()
password = 'clavesecreta1'
password_encriptada = generador.generate_password_hash(password)

verificar = generador.check_password_hash(password_encriptada,'clave1')

verificar = generador.check_password_hash(password_encriptada,'clavesecreta1')
print(verificar)