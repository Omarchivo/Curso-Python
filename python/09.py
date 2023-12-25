#   TRATAMIENTO DE ERRORES
'''
try:
    fichero = open("datos3.txt","r")
    fichero.write("Estos son los datos para el segundo fichero")
    fichero.close()
except FileNotFoundError:
    print("Error de tipo FileNotFoundError. El fichero no existe")
except:
    print("Error general")
else:
    print("Tratamiento del fichero correcto")
finally:
    print("Tratamiento del fichero finalizado")

print("Continua el programa")
'''

#   EXPRESIONES REGULARES
import re

# texto = "Este carro verde es muy rápido"
# print(texto)
# patron = "verde"
# encontrado = re.search(patron,texto)

# if encontrado:
#     print("Patron {} encontrado en el texto".format(patron))
#     ini = encontrado.start()
#     fin = encontrado.end()
#     print("Patron {} empieza en la posición {} y termina en la posición {}".format(patron, ini, fin))
# else:
#     print("Patron {} no encontrado".format(patron))

# texto = "Me gusta el color verde y por eso he comprado pintura verde."
# patron = "e"
# resultado = re.findall(patron,texto)
# print(resultado)
# veces = len(resultado)
# print(veces)

texto = "Me gusta el color verde y por eso he comprado pintura verde."
patrones = ["carro","pintura","moto"]
for patron in patrones:
    print("Estamos buscando por el patron {}".format(patron))
    resultado = re.findall(patron,texto)
    veces = len(resultado)
    print(veces)