# Ejercicio 1:

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# print("Imprimiendo números del 0 al 99:")
# num = 0

# while num < 101:
#     print(num)
#     num += 1


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2:

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# while True:
#     numero = input("Ingresa un número entero: ")
    
#     if numero.lstrip('-').isdigit():    # Verificamos si es un número entero (puede ser negativo)
#         break
#     else:
#         print("Entrada inválida. Solo se permiten números enteros sin comas ni puntos.")

# cantidad_digitos = str(len(numero))

# print("La cantidad de digitos que contiene es: " + cantidad_digitos)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3:

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# valor_1 = int(input("Ingrese primer valor: "))
# valor_2 = int(input("Ingrese segundo valor: "))

# for i in range(valor_1+1,valor_2):
#     print(i)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4:

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# total = 0

# print("Ingresa numeros enteros para sumarlos. Ingresa 0 para terminar.")

# while True:
#     numero = input("Número: ")

#     if numero.lstrip('-').isdigit():
#         numero = int(numero)

#         if numero == 0:
#             break  # Salir del bucle si el número es 0
#         total += numero
#     else:
#         print("Entrada inválida. Ingresá solo números enteros sin comas ni puntos.")

# print(f"La suma total es: {total}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5:

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random

# numero_secreto = random.randint(0, 9)
# intentos = 0

# print("Adiviná el número (entre 0 y 9):")

# while True:
#     intento = input("Tu intento: ")

#     if intento.isdigit():  # Validar que sea un número entero positivo
#         intento = int(intento)
#         intentos += 1

#         if intento == numero_secreto:
#             print(f"✅ ¡Correcto! Adivinaste el numero en {intentos} intento(s).")
#             break
#         else:
#             print("❌ Incorrecto.")
#     else:
#         print("⚠️ Entrada inválida. Ingresá un numero entero entre 0 y 9.")


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6:

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.


# for i in range(100, -1, -2):
#     print(i)


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7:

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# while True:
#     num = input("Ingresa un numero entero positivo: ")
#     if num.isdigit():
#         num = int(num)
#         break
#     else:
#         print("❌ Entrada invalida. Solo se permiten numeros enteros positivos.")

# suma = 0
# for i in range(num):
#     suma += i

# print(f"La suma de los números desde 0 hasta {num - 1} es: {suma}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8:

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


# TOTAL_NUMEROS = 10
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# contador = 0

# print(f"Ingresa {TOTAL_NUMEROS} numeros enteros:")

# while contador < TOTAL_NUMEROS:
#     entrada = input(f"Numero {contador + 1}: ")

#     if entrada.lstrip('-').isdigit():
#         numero = int(entrada)
#         # Par o impar
#         if numero % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
#         # Positivo o negativo
#         if numero > 0:
#             positivos += 1
#         elif numero < 0:
#             negativos += 1
#         contador += 1
#     else:
#         print("❌ Entrada invalida. Ingresa un numero entero.")

# print("\n📊 Resultados:")
# print(f"Pares: {pares}")
# print(f"Impares: {impares}")
# print(f"Positivos: {positivos}")
# print(f"Negativos: {negativos}")


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9:

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# from statistics import mean

# print("Este programa calcula la media de los números ingresados.")

# cantidad = 100
# numeros = []

# while len(numeros) < cantidad:
#     entrada = input(f"Ingrese el número {len(numeros)+1}/{cantidad}: ")
#     if entrada.lstrip('-').isdigit():
#         numeros.append(int(entrada))
#     else:
#         print("Ingrese solo números enteros validos.")

# media = mean(numeros)
# print("Numeros:"+ str(numeros))
# print(f"\nLa media de los numeros ingresados es: {media}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10:

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# numero = input("Ingresa un numero entero: ")

# # Validamos entero (positivo o negativo)
# if numero.lstrip('-').isdigit():
#     if numero.startswith('-'):
#         invertido = '-' + numero[:0:-1]  # Excluye el signo negativo al invertir
#     else:
#         invertido = numero[::-1]  # Invierte todos los caracteres
#     print(f"Número invertido: {invertido}")
# else:
#     print("Entrada inválida. Por favor ingresa un número entero.")