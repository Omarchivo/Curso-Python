'''
numero1 = 3
numero2 = 4
suma = numero1 + numero2
print(suma)
'''
'''
texto = "Hola, buenos días"
print(texto)

caracter = texto[-2]
print(caracter)

#slicing
caracter = texto[6::2]
print(caracter)

#funciones sobre las cadenas de caracteres

mayusculas = texto.upper()
print(mayusculas)

minusculas = mayusculas.lower()
print(minusculas)

colores = "Rojo,Verde,Azul,Negro"
lista = colores.split(",")
print(lista)
color = lista[1]
print(color)
'''
'''
nombre = "Antonio"
print("Hola {} buenos días".format("nombre"))

numero1 = 5
numero2 = 3
sum = numero1 + numero2
print("{} mas {} es igual a {}".format(numero1,numero2,sum))
'''

#Listas en python
lista = [1, 2, 3]
print(lista)

lista = ['Antonio', 'Luis', 2, 40, 'María', 1, 4, 25]
print(lista)

elemento = lista[2:4] #El slacing tambien aplica en listas
print(elemento)

nuevos_elementos = ['Rojo', 'Verde', 'Azul']
lista.append(nuevos_elementos)
print(lista)

lista = ['Antonio', 'Luis', 2, 40, 'María', 1, 4, 25]
nuevos_elementos = ['Rojo', 'Verde', 'Azul']
lista.extend(nuevos_elementos) #el extend se usa para añadir los elementos de una lista en otra
print(lista)

