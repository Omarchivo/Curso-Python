#Range

#numeros = range(1,20,2)
#print(numeros)

#for elemento in range(5):
#    print("Hola")

###########################  FUNCIONES  ###########################
'''
def hola():
    print("Hola, buenos días")

hola()
hola()
hola()

def sumar(numero1, numero2):
    """
    Esta funcion suma dos numeros enteros
    Ejemplo de llamada
        sumar(5,3)
    """
    if type(numero1) == type(numero2) == type(10):
        resultado = numero1 + numero2
    else:
        resultado = "Error, deben ser numeros"
    return resultado

suma = sumar(5,"4")
print(suma)
'''

###########################  FUNCIONES LAMBDA  ###########################
'''
lista = [1,2,3,4,5,6]


def par(numero):
    resultado = (numero % 2) == 0
    return resultado


filtro = filter(lambda numero : (numero % 2) == 0,lista)
pares = list(filtro)
print(pares)
'''

###########################  AMBITO DE LAS VARIABLES  ###########################

variable = 5

def funcion():
    variable = 8
    print(variable)

funcion()
print(variable)
