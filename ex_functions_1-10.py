
#1.Construir una función que reciba como parámetro un entero y retorne su último dígito.
def último_digito(num):
    unidad = int(num % 10)
    print("Último dígito: " + str(unidad))

último_digito(int(input("Elige un número entero: ")))

#2.Construir una función que reciba como parámetro un entero y retorne sus dos últimos dígitos.
def últimos_digitos(num):
    unidad = int(num % 100)
    print("Dos últimos dígitos: " + str(unidad))

últimos_digitos(int(input("Elige un número entero:")))

#3.Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos.
def cantidad_digitos(num):
    contador = 0
    while num >= 1:
        num = int(num / 10)
        contador = contador + 1
    print("Cantidad de dígitos del número elegido: " + str(contador))

cantidad_digitos(int(input("Elige un número entero: ")))

#4.Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos
# pares.
def cantidad_digitospar(num):
    contador = 0
    while num >= 1:
        if int(num % 2) == 0:
            contador = contador + 1
        num = int(num / 10)
    print("Cantidad de dígitos pares del número elegido: " + str(contador))

cantidad_digitospar(int(input("Elige un número entero: ")))

#5.Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos
# primos.
def cantidad_digitos_primos(number):
    contador = 0
    while number >= 1:
        unidad = int(number % 10)
        number = int(number / 10)
        for x in range(2, (unidad - 1)):
            if int(unidad % x) == 0:
                primo = False
                break
            primo = True
        if primo == True or unidad == 2 or unidad == 3:
            contador = contador + 1
    print("Cantidad de dígitos primos del número elegido: " + str(contador))

cantidad_digitos_primos(int(input("Elige un número entero: ")))

#6.Construir una función que reciba como parámetro un entero y retorne el carácter al cual
# pertenece ese entero como código ASCII.
def numero_ascii(num):
    caracterM = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    caracterm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if num >= 65 and num <= 91:
        contador = 65
        for letra in caracterM:
            if contador == num:
                print (letra)
                break
            contador = contador + 1
    elif num >= 97 and num <= 122:
        contador = 97
        for letra in caracterm:
            if contador == num:
                print (letra)
                break
            contador = contador + 1
    else:
        print("El número elegido no esta asociado a una letra en el código ASCII. ")

numero_ascii(int(input("Elige un número entero del 65 al 122: ")))

#7.Construir una función que reciba como parámetro un carácter y retorne el código ASCII
# asociado a él.
def caracter_ascii(letra):
    caracterM = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    caracterm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    contador = 65     
    for caracter in caracterM:
        if letra == caracter:
            print(contador)
            break
        contador = contador + 1
    contador = 97
    for caracter in caracterm:
        if letra == caracter:
            print (contador)
            break
        contador = contador + 1

caracter_ascii(str(input("Elige un caracter: ")))

#8. Construir una función que reciba como parámetro un entero y retorne 1 si dicho entero está
# entre los 30 primeros elementos de la serie de Fibonacci. Deberá retornar 0 si no es así.
def is_fibonacci(num):
    fibonacci = []
    x = 0
    y = 1
    for _ in range(0, 15):
        fibonacci.append(x)
        fibonacci.append(y)
        x = x + y
        y = x + y
    for dato in fibonacci:
        if num == dato:
            mismo = True
            print(1)
            break
        mismo = False
    if mismo == False:
        print(0)

is_fibonacci(int(input("Elige un número entero: ")))

#9. Construir una función que reciba un entero y le calcule su factorial sabiendo que el factorial de
# un número es el resultado de multiplicar sucesivamente todos los enteros comprendidos entre
# 1 y el número dado. El factorial de 0 es 1. No están definidos los factoriales de números
# negativos.
def factorial(num):
    factorial = 1
    for x in range(1, (num + 1)):
        factorial = factorial * x
    print("Factorial del número: " + str(factorial))

factorial(int(input("Elige un número entero: ")))

#10. Construir una función que reciba como parámetro un entero y retorne el primer dígito de este
# entero.
def primer_digito(num):
    while num >= 10:
        num = int(num / 10)
    print("Primer dígito: " + str(num))

primer_digito(int(input("Elige un número entero: ")))
