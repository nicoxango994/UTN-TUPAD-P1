# Ejercicio 1:

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

# multiplos_de_4 = list(range(4, 101, 4))
# print(multiplos_de_4)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2:

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

# mis_favoritos = ['pizza', 'guitarra', 'playa', 'Python', 'bicicleta']
# print(mis_favoritos[-2])  # Accede al penúltimo elemento

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3:

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

# lista_vacia = []
# lista_vacia.append('sol')
# lista_vacia.append('libro')
# lista_vacia.append('café')
# print(lista_vacia)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4:

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

# animales = ["perro", "gato", "conejo", "pez"]

# print(f"Primera lista: {animales}")

# # Reemplazar el segundo valor (índice 1) por "loro"
# animales[1] = "loro"

# # Reemplazar el último valor (índice -1) por "oso"
# animales[-1] = "oso"

# print(f"Lista actualizada: {animales}")



#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5:

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)
# Retira el numero mayor en comparacion a la lista completa y lo muestra sin el numero 22(en este caso el mayor)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6:

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

# numeros = list(range(10, 31, 5))
# print(numeros[:2])

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7:

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

# autos = ["sedan", "polo", "suran", "gol"]
# autos[1:3] = ["camioneta", "coupe"]
# print(autos)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8:

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

# dobles = []
# dobles.append(5 * 2)
# dobles.append(10 * 2)
# dobles.append(15 * 2)
# print(dobles)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9:

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# Lista original
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# compras[2].append("jugo")
# compras[1][1] = "tallarines"
# compras[0].remove("pan")
# # Lista resultante:
# print(compras)


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10:

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla

# lista_anidada = [
#     15,                 # lista_anidada[0]
#     True,               # lista_anidada[1]
#     [25.5, 57.9, 30.6], # lista_anidada[2][0], [2][1], [2][2]
#     False               # lista_anidada[3]
# ]

# print(lista_anidada)
