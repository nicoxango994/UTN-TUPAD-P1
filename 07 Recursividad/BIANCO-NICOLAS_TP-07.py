# Ejercicio 1:

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# # Función recursiva para calcular el factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Solicitar al usuario un número entero
# limite = int(input("Ingresá un número entero positivo: "))

# # Calcular y mostrar el factorial de los números desde 1 hasta el número ingresado
# for i in range(1, limite + 1):
#     print(f"El factorial de {i} es {factorial(i)}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2:

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# # Función recursiva para obtener el valor de Fibonacci en una posición
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Solicitar al usuario una posición hasta la cual mostrar la serie
# posicion = int(input("Ingresá la cantidad de términos de la serie de Fibonacci a mostrar: "))

# # Mostrar la serie completa hasta esa posición
# print("Serie de Fibonacci:")
# for i in range(posicion):
#     print(fibonacci(i), end=" ")


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3:

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.

# # Funcion recursiva para calcular la potencia
# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)

# # Algoritmo general para probar la funcion
# base = int(input("Ingresar la base: "))
# exponente = int(input("Ingresar el exponente: "))

# resultado = potencia(base, exponente)
# print(f"{base} elevado a la {exponente} es igual a {resultado}")


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4:

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"

# # Funcion recursiva para convertir un numero decimal a binario
# def decimal_a_binario(n):
#     if n == 0:
#         return ""
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)

# # Numero a convertir
# numero = int(input("Ingresar un numero entero positivo: "))

# if numero == 0:
#     print("El binario de 0 es: 0")
# else:
#     binario = decimal_a_binario(numero)
#     print(f"El binario de {numero} es: {binario}")


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5:

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])

# # Ejemplo de uso
# palabra = input("Ingresar una palabra sin espacios ni tildes: ").lower()
# if es_palindromo(palabra):
#     print("Es un palindromo.")
# else:
#     print(False)


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6:

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)



#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7:

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# def contar_bloques(n):
#     if n <= 0:
#         return 0  # No hay bloques si n es 0 o negativo
#     if n == 1:
#         return 1  # Caso base: un solo bloque
#     return n + contar_bloques(n - 1)

# def main():
#     n = int(input("Ingrese la cantidad de bloques del piso más bajo: "))
#     total = contar_bloques(n)
#     print(f"Total de bloques para construir la pirámide: {total}")

# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8:

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0

# def contar_digito(numero, digito):
#     if numero == 0:
#         return 0
#     else:
#         cuenta = 1 if (numero % 10) == digito else 0
#         return cuenta + contar_digito(numero // 10, digito)

# def main():
#     numero = int(input("Ingrese un número entero positivo: "))
#     digito = int(input("Ingrese un dígito (0-9) a buscar: "))
#     cantidad = contar_digito(numero, digito)
#     print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

#------------------------------------------------------------------------------------------------------------------------------
