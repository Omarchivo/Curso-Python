lista = [1,2,'Verde',5,'Antonio']
print(lista)

#lista.pop()
#print(lista)

#lista.pop(0)
#print(lista)

lista.reverse()
print(lista)

lista = [5,9,2,3,1]
lista.sort()
print(lista)

lista = [1,2,3,4,['Verde','Rojo']]
print(lista)

elemento = lista[4][0]
print(elemento)


matriz = [[1,2,3], [4,5,6], [7,8,9]]
lista_nueva = [elemento[0] for elemento in matriz]
print(lista_nueva)