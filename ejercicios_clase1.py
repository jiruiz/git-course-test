#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
#
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.

print("Hello World!")

# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.

# def exercise2():
#     for number in range(1,100):
#         if number%2==0:
#             print(number)
#
# exercise2()


# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.

# def exercise3():
#     for number in range(0, 101):
#         if number%3 == 0:
#             print(number)
#
# exercise3()


# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.

def exercise4():
    number1 = int(input("numero 1:  "))
    number2 = int(input("numero 2:  "))
    suma = number1 + number2
    print(suma)
    resta = number1 - number2
    print(resta)
    modulo = number1 % number2
    print(modulo)


exercise4()
# Ejercicio 5
#
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.
# def exercise5():
#     userValuesList = []
#     for number in range(10):
#         userValues = int(input(f"ingrese su numero entero({number +1}):  "))
#         userValuesList.append(userValues)
#     print(userValuesList)
#     userValuesList.sort()
#     print(userValuesList)
# exercise5()
# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.

# def exercise6(number1, number2):
#     if number1 > number2:
#         return 1
#     elif number1 == number2:
#         return 0
#     else:
#         return -1
# userInput1 = int(input("ingrese numero 1:  "))
# userInput2 = int(input("ingrese numero 2:  "))
#
# result = exercise6(userInput1, userInput2)
# print(result)
# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
#
# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#

# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".

# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

# def exercise11(userInput):
#     wordList = userInput.split()
#     print(len(userInput))
#     print(len(wordList))
#     return len(wordList[-1])
#
# word = exercise11("bienvenidos a paradigmas de programacion")
# print(word)


# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#
#
