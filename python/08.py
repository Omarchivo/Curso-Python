# numero = "Hola"
# print(type(numero))

#lista = [1,2,3,4]
#print(type(lista))

'''
class clase1():
    pass

objeto1 = clase1()
print(type(objeto1))
'''

class Persona():
    texto = ''
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        self.texto = "Hola mi nombre es "+ self.nombre
        return self.texto

persona1 = Persona("Omar")
print(type(persona1))
print(persona1.nombre)
texto = persona1.saludar()
print(texto)

class Adulto(Persona):
    def __init__(self,nombre):
        Persona.__init__(self,nombre)
    def saludar(self):
        self.texto = "Hola, soy adulto"
        return self.texto
    def grabar_tarjeta(self,tarjeta):
        self.tarjeta = tarjeta
    def __str__(self):
        self.texto = "Adulto: nombre = " + self.nombre
        return self.texto

adulto1 = Adulto("Andres")
print(type(adulto1))
texto = adulto1.saludar()
print(texto)
adulto1.grabar_tarjeta("1122334455")
print(adulto1.tarjeta)

numero = 5
print(numero)
print(adulto1)