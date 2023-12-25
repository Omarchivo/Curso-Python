#   VARIABLES LOCALES Y GLOBALES

# numero = 30
# texto = "hola"

# def funcion1():
#     numero2 = 50
#     saludo = "Buenos días"
#     print(numero2)
#     print(saludo)
#     print(locals())

# #funcion1()
# print(numero)
# print(texto)
# print(globals())
# print(globals()['__file__'])

# FUNCIONES DECORADORAS: Es un función que se aplica sobre otra función

def asteriscos(funcion):
    def poner_asteriscos():
        print("**************************")
        funcion()
        print("**************************")
    return poner_asteriscos

@asteriscos
def imprimir():
    print("Hola, buenos días")

#imprimir = asteriscos(imprimir)
imprimir()