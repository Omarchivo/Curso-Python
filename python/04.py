'''
#Tuplas en python

tupla = (1,2,5,'Hola','Antonio',5,'Verde')
print(tupla)

elemento = tupla[1:3]
print(elemento)

#tupla[0] = 9 #Es un error, las tuplas son inmutables, es decir no se pueden cambiar los datos que la contienen
'''

# Conjuntos en Python

conjunto = set()
print(conjunto)

conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add('Hola')
conjunto.add('Antonio')
print(conjunto)

conjunto.discard('Antonio')
conjunto.discard(2)
print(conjunto)

#Los valores en los conjuntos no se pueden repetir, se añade una vez nada mas
conjunto.add(9)
conjunto.add(9)
conjunto.add(9)
conjunto.add(9)
print(conjunto)

#Se suelen usar para eliminar duplicados en listas por ejemplo
lista = [1,2,2,2,3,3,3,3,1,1,1,1,2,2]
conjunto = set(lista)
print(conjunto)
