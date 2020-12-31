
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

#11. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho
# entero es múltiplo de dicho dígito y 0 si no es así.
def is_digitomultiplo(num, digito):
    if int(num % digito) == 0:
        print(1)
    else:
        print(0)

is_digitomultiplo(int(input("Elige un número entero: ")), int(input("Elige un dígito: ")))

#12. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho
# dígito está en dicho entero y 0 si no es así.
def is_digito_in_number(num, digito):
    while num >= 1:
        unidad = int(num % 10)
        num = int(num / 10)
        if unidad == digito:
            esta = True
            print(1)
            break
        esta = False
    if esta == False:
        print(0)

is_digito_in_number((int(input("Elige un número entero: "))), (int(input("Elige un dígito: "))))

#13. Construir una función que reciba como parámetro un entero y un dígito y retorne la cantidad de
# veces que se encuentra dicho dígito en dicho entero.
def cantidad_digito_in_number(num, digito):
    contador = 0
    while num >= 1:
        unidad = int(num % 10)
        num = int(num / 10)
        if unidad == digito:
            contador = contador + 1
    print(digito)
    print("Número de veces que el dígito se encuentra en el número: " + str(contador))

cantidad_digito_in_number((int(input("Elige un número entero: "))), (int(input("Elige un dígito: "))))

#14. Construir una función que reciba como parámetros dos números enteros y retorne el valor del
# mayor.
def mayor(num1, num2):
    if num1 > num2:
        print("Número mayor: " + str(num1))
    if num2 > num1:
        print("Número mayor: " + str(num2))
    elif num1 == num2:
        print("Los dos números son iguales")

mayor(int(input("Elige un número entero: ")), int(input("Elige un dígito: ")))

#15. Construir una función que reciba como parámetros dos números enteros y retorne 1 si el
# primer número es múltiplo del segundo y 0 si no.
def is_primero_multiplo_segundo(num, digito):
    if int(num % digito) == 0:
        print(1)
    else:
        print(0)

is_primero_multiplo_segundo(int(input("Elige un número entero: ")), int(input("Elige un dígito: ")))

#16. Construir una función que reciba como parámetro un entero y retorne 1 si corresponde al
# código ASCII de una letra minúscula (Los códigos ASCII de las letras minúsculas van desde 97
# que el código de la letra a hasta 122 que es el código de la letra z). Deberá retornar 0 si no es
# así.
def is_ascii_minuscula(num):
    if num >= 97 and num <= 122:
        print(1)
    else:
        print(0)

is_ascii_minuscula(int(input("Elige un número entero: ")))

#17. Construir una función que reciba como parámetro un entero y retorne 1 si corresponde al
# código ASCII de un dígito (Los códigos ASCII de las letras minúsculas van desde 48 que es el
# código del dígito 0 hasta 57 que es el código del dígito 9). Deberá retornar 0 si no es así.
def is_ascii_digito(num):
    if num >= 48 and num <= 57:
        print(1)
    else:
        print(0)

is_ascii_digito(int(input("Elige un número entero: ")))

#18. Construir una función que reciba como parámetro un valor entero y retornar 1 si dicho valor es
# el factorial de alguno de los dígitos del número. Deberá retornar 0 si no es así.
def is_factorial(num):
    vecfac = []
    factorial = 1
    x = num
    mismo = False
    while num >= 1:
        unidad = int(num % 10)
        num = int(num / 10)
        factorial = 1
        for y in range(1, (unidad + 1)):
            factorial = factorial * y
        vecfac.append(int(factorial))
    for number in vecfac:
        if x == number:
            mismo = True
            print(1)
            break
        mismo = False
    if mismo == False:
        print(0)
    print(vecfac)

is_factorial(int(input("Elige un número entero: ")))

#19. Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es un
# número de mínimo 3 dígitos. Deberá retornar 0 si no es así.
def has_centenas(num):
    if num >= 100:
        print(1)
    else:
        print(0)

has_centenas(int(input("Elige un número entero: ")))

#20. Construir una función que reciba como parámetro un entero y retorne 1 si en dicho valor todos
# los dígitos son iguales. Deberá retornar 0 si no es así.
def digitos_iguales(num):
    digitos = []
    x = 0
    igual = True
    while num >= 1:
        digito = int(num % 10)
        num = int(num / 10)
        digitos.append(digito)
    x = digitos[0]
    for digito in digitos:
        if digito != x:
            igual = False
            print(0)
            break
        x = digito
        igual = True
    if igual == True:
        print(1)

digitos_iguales(int(input("Elige un número entero: ")))

#21. Construir una función que reciba como parámetro un entero y retorne 1 si en dicho valor el
# primer dígito es igual al último. Deberá retornar 0 si no es así.
def primer_ultimo_iguales(num):
    unidad = int(num % 10)
    while num >= 10:
        num = int(num / 10)
    if num == unidad:
        print(1)
    else:
        print(0)

primer_ultimo_iguales(int(input("Elige un número entero: ")))

#22. Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es
# múltiplo de 5. Deberá retornar 0 si no es así.
def is_multiplocinco(num):
    if int(num % 5) == 0:
        print(1)
    else:
        print(0)

is_multiplocinco(int(input("Elige un número entero: ")))

#23. Construir una función que reciba como parámetro dos enteros y retorne 1 si la diferencia entre
# los dos valores es un número primo. Deberá retornar 0 si no es así.
def is_diferencia_prima(num1, num2):
    diferencia = 0
    is_prime = False
    if num1 > num2:
        diferencia = num1 - num2
        for x in range(2, (diferencia - 1)):
            if int(diferencia % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or diferencia == 2 or diferencia == 3:
            print(1)
        else:
            print(0)
    elif num2 > num1:
        diferencia = num2 - num1
        for x in range(2, (diferencia - 1)):
            if int(diferencia % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or diferencia == 2 or diferencia == 3:
            print(1)
        else:
            print(0)
    else:
        print("Los dos números son iguales.")

is_diferencia_prima(int(input("Elige un número entero: ")), int(input("Elige un número entero: ")))

#24. Construir una función que reciba como parámetro dos enteros de dos dígitos cada uno y
# retorne 1 si son inversos. Ejemplo: 83 es inverso de 38. Deberá retornar 0 si no es así.
def inversos(num1, num2):
    unidad1 = int(num1 % 10)
    unidad2 = int(num2 % 10)
    decenas1 = int(num1 / 10)
    decenas2 = int(num2 / 10)
    if unidad1 == decenas2 and decenas1 == unidad2:
        print(1)
    else:
        print(0)

inversos(int(input("Elige un número entero: ")), int(input("Elige un número entero: ")))

#25. Construir una función que reciba como parámetro un entero y un dígito menor o igual a 5 y
# retorne el dígito del número que se encuentre en la posición especificada por el dígito que llegó
# como parámetro.
def posicion_digito(num, posicion):
    contador = 0
    x = num
    resultado = 0
    while num >= 1:
        num = int(num / 10)
        contador = contador + 1

    x = int(x / 10 ** ((contador - posicion)))
    resultado = int(x % 10)
    print("Dígito del número en la posición elegida: " + str(resultado))

posicion_digito(int(input("Elige un número entero: ")), int(input("Elige un número del 1 al 5: ")))

#26. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# el mayor de los datos del vector.
def mayor_dato_vector():
    grande = 0
    for number in vector:
        if number > grande:
            grande = number
    print("El mayor número es: " + str(grande))

vector = []
for i in range (0, 10):
    vector.append(int(input("Elige un número: ")))
mayor_dato_vector()

#27. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la posición en la cual se encuentra el mayor de los datos del vector.
def mayor_vector():
    grande = 0
    contador = 1
    for number in vector:
        if number > grande:
            grande = number
    for number in vector:
        if number == grande:
            break
        else:
            contador = contador + 1
    print("El mayor número esta en la posición: " + str(contador))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
mayor_vector()

#28. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la cantidad de números primos almacenados en el vector.
def cantidad_primos_vector():
    contador = 0
    for number in vector:
        for x in range(2, (number - 1)):
            if int(number % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or number == 2 or number == 3:
            contador = contador + 1
    print("Cantidad de números primos: " + str(contador))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
cantidad_primos_vector()

#29. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la cantidad de números que pertenecen a los 30 primeros elementos de la serie de Fibonacci.
def cantidad_fibonacci():
    fibonacci = []
    contador = 0
    x = 0
    y = 1
    for _ in range(0, 15):
        fibonacci.append(x)
        fibonacci.append(y)
        x = x + y
        y = x + y
    for num in vector:
        for dato in fibonacci:
            if num == dato:
                contador = contador + 1
                break
    print("Cantidad de números que coinciden con los 30 primeros numeros de la lista de Fibonacci: " + str(contador))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
cantidad_fibonacci()

#30. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la posición del mayor número primo almacenado en el vector.
def posicion_mayor_primo_vector():
    primos = []
    mayor = 0
    is_prime = False
    contador = 0
    for number in vector:
        for x in range(2, (number - 1)):
            if int(number % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or number == 2 or number == 3:
            primos.append(number)
    for primo in primos:
        if primo > mayor:
            mayor = primo
    for number in vector:
        contador = contador + 1
        if number == mayor:
            break
    print("Posición del mayor número primo: " + str(contador))

vector = []
for i in range (0, 10):
    vector.append(int(input("Elige un número: ")))
posicion_mayor_primo_vector()

#31. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# el promedio entero del vector.
def promedio_vector():
    suma = 0
    promedio = 0
    contador = 0
    for number in vector:
        suma = suma + number
        contador = contador + 1
    promedio = int(suma / contador)
    print("Promedio de los números elegidos: " + str(promedio))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
promedio_vector()

#32. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# el promedio real del vector.
def promedio_vector_real():
    suma = 0
    contador = 0
    promedio = 0
    for number in vector:
        suma = suma + number
        contador = contador + 1
    promedio = float(suma / contador)
    print("Promedio de los números elegidos: " + str(promedio))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número: ")))
promedio_vector_real()

#33. Construir una función que reciba como parámetros un vector de 10 posiciones enteras y un
# valor entero y retorne 1 si dicho valor entero se encuentra en el vector. Deberá retornar 0 si no
# es así.
def is_in_vector():
    esta = False
    for number in vector:
        if number == num:
            esta = True
            print(1)
            break
        esta = False
    if esta == False:
        print(0)

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige números para el vector: ")))
num = int(input("Elige otro número para compararlo: "))
is_in_vector()


#34. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la posición del número entero que tenga mayor cantidad de dígitos.
def posiciones_mayor():
    contador = 0
    digitos = []
    posiciones = []
    for number in vector:
        contador = 0
        while number >= 1:
            contador = contador + 1
            number = int(number / 10)
        digitos.append(contador)
    mayor = digitos[0]
    for digito in digitos:
        if digito > mayor:
            mayor = digito
    contador = 0
    for digito in digitos:
        contador = contador + 1
        if digito == mayor:
            posiciones.append(contador)
    print("Posicion/es del o los números con más dígitos: " + str(posiciones))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número: ")))
posiciones_mayor()

#35. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la posición en la que se encuentre el mayor número primo que termine en 3 almacenado en el
# vector.
def posicion_mayor_primo_tres():
    primos = []
    mayor = 0
    is_prime = False
    contador = 0
    for number in vector:
        for x in range(2, (number -1)):
            if int(number % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or number == 2 or number == 3:
            primos.append(number)
    for primo in primos:
        if int(primo % 10) == 3:
            mayor = primo
            break
    for primo in primos:
        if int(primo % 10) == 3 and primo > mayor:
            mayor = primo
    for number in vector:
        contador = contador + 1
        if number == mayor:
            break
    print("Posición del mayor número primo: " + str(contador))

vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
posicion_mayor_primo_tres()

#36. Construir una función que reciba como parámetro un entero y retorne ese elemento de la serie
# de Fibonacci.
def elemento_fibonacci(num):
    vector = []
    x = 0
    y = 1
    for _ in range(0, (int(num / 2) - 1)):
        vector.append(x)
        vector.append(y)
        x = x + y
        y = x + y
    print(vector)
    print("Elemento de la serie de Fibonacci en esa posición: " + str(y))

elemento_fibonacci(int(input("Elige un número entero para obtener su equivalente en la serie de Fibonacci: ")))


#37. Construir una función que reciba como parámetros dos enteros, el primero actuará como base
# y el segundo como exponente y retorne el resultado de elevar dicha base a dicho exponente.
def elevar_exponente(base, exponente):
    resultado = base ** exponente
    print(resultado)

elevar_exponente(int(input("Elige un número para la base: ")), int(input("Elige un número para el exponente: ")))

#38. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne
# la cantidad de números terminados en 3 que contiene el vector.
def numeros_tres():
    contador = 0
    for num in vector:
        if int(num % 10) == 3:
            contador = contador + 1
    print("Cantidad de números terminados en 3: " + str(contador))

vector = []
for i in range (0, 10):
    vector.append(int(input("Elige un número: ")))
numeros_tres()

#39. Construir una función que reciba como parámetros un vector de 10 posiciones enteras y un
# dígito y que retorne la cantidad de veces que dicho dígito se encuentra en el vector. No se
# olvide que un mismo dígito puede estar varias veces en un solo número.
def cantidad_mismo_digito():
    contador = 0
    for num in vector:
        while num >= 1:
            if int(num % 10) == digito:
                contador = contador + 1
            num = int(num / 10)
    print("Cantidad de veces que el dígito se encuentra en los números: " + str(contador))

vector = []
for i in range (0, 3):
    vector.append(int(input("Elige un número: ")))
digito = int(input("Elige un dígito para comparar: "))
cantidad_mismo_digito()

#40. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y un
# dígito y que retorne la cantidad de números del vector que terminan en dicho dígito.
def cantidad_mismo_final():
    contador = 0
    for num in vector:
        if int(num % 10) == digito:
            contador = contador + 1
    print("Cantidad de números terminados en el dígito: " + str(contador))

vector = []
for i in range (0, 10):
    vector.append(int(input("Elige un número: ")))
digito = int(input("Elige un dígito para comparar: "))
cantidad_mismo_final()

#41. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y un
# dígito y que retorne la cantidad de números del vector en donde dicho dígito está de penúltimo.
def cantidad_digito_penultimo():
    contador = 0
    for num in vector:
        if int((num / 10)% 10) == digito:
            contador = contador + 1
    print("Cantidad de números que tienen el dígito como penúltimo: " + str(contador))

vector = []
for i in range (0, 10):
    vector.append(int(input("Elige un número: ")))
digito = int(input("Elige un dígito para comparar: "))
cantidad_digito_penultimo()

#42. Construir una función que reciba como parámetro una matriz de 3x4 entera y retorne la
# cantidad de veces que se repite el mayor dato de la matriz.
def cantidad_mayor():
    mayor = 0
    contador = 0
    for i in range(3):
        for j in range(4):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    for i in range(3):
        for j in range(4):
            if matriz[i][j] == mayor:
                contador = contador + 1
    print("Cantidad de veces que se repite el mayor número: " + str(contador))

matriz = []
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
cantidad_mayor()

#43. Construir una función que reciba como parámetro una matriz 3x4 entera y retorne la cantidad
# de números primos almacenados en la matriz.
def cantidad_primos_matriz():
    is_prime = False
    contador = 0
    for i in range(3):
        for j in range(4):
            for x in range(2, ((matriz[i][j]) - 1)):
                if int((matriz[i][j]) % x) == 0:
                    is_prime = False
                    break
                is_prime = True
            if is_prime == True or matriz[i][j] == 2 or matriz[i][j] == 3:
                contador = contador + 1
    print(matriz)
    print("Cantidad de números primos: " + str(contador))

matriz = []
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
cantidad_primos_matriz()

#44. Construir una función que reciba como parámetro una matriz 3x4 entera y retorne la cantidad
# de veces que se repite el mayor número primo de la matriz.
def cantidad_mayor_primo():
    primos = []
    is_prime = False
    mayor = 0
    contador = 0
    for i in range(3):
        for j in range(4):
            for x in range(2, ((matriz[i][j]) - 1)):
                if int((matriz[i][j]) % x) == 0:
                    is_prime = False
                    break
                is_prime = True
            if is_prime == True or matriz[i][j] == 2 or matriz[i][j] == 3:
                primos.append(matriz[i][j])
    mayor = primos[0]        
    for primo in primos:
        if primo > mayor:
            mayor = primo
    for i in range(3):
        for j in range(4):
            if matriz[i][j] == mayor:
                contador = contador + 1
    print("Cantidad de veces que se repite el mayor números primo: " + str(contador))

matriz = []
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
cantidad_mayor_primo()

#45. Construir una función que reciba como parámetros una matriz 4x4 entera y un valor entero y
# retorne la cantidad de veces que se repite dicho valor en la matriz.
def cantidad_repetidos():
    contador = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == num:
                contador = contador + 1
    print("Cantidad de veces que se repite el número elegido: " + str(contador))

matriz = []
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
num = int(input("Elige un número para ver cuantas veces se encuentra en la matriz: "))
cantidad_repetidos()

#46. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne el número de
# la fila en donde se encuentre por primera vez el número mayor de la matriz.
def fila_mayor():
    mayor = 0
    fila = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    for i in range(4):
        fila = fila + 1
        for j in range(4):
            if matriz[i][j] == mayor:
                print("Fila en la que se encuentra el número mayor de la matriz: " + str(fila) + ".")
                break

matriz = []
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
fila_mayor()

#47. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne el número de
# la columna en donde se encuentre por primera vez el número mayor de la matriz.
def columna_mayor():
    mayor = 0
    columna = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    for i in range(4):
        columna = 0
        for j in range(4):
            columna = columna + 1
            if matriz[i][j] == mayor:
                print("Columna en la que se encuentra el número mayor de la matriz: " + str(columna) + ".")
                break

matriz = []
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
columna_mayor()

#48. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne la posición
# exacta en donde se encuentre almacenado el mayor número primo.
def posicion_mayor_primo_matriz():
    primos = []
    mayor = 0
    fila = 0
    columna = 0
    for i in range(4):
        for j in range(4):
            for x in range(2, (matriz[i][j] - 1)):
                if int(matriz[i][j] % x) == 0:
                    is_prime = False
                    break
                is_prime = True
            if is_prime == True or matriz[i][j] == 2 or matriz[i][j] == 3:
                primos.append(matriz[i][j])
    mayor = primos[0]        
    for primo in primos:
        if primo > mayor:
            mayor = primo
    for i in range(4):
        fila = fila + 1
        columna = 0
        for j in range(4):
            columna = columna + 1
            if matriz[i][j] == mayor:
                print("Posición del mayor número primo: Fila: " + str(fila) + ". Columna: " + str(columna) + ".")
                break

matriz = []
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
posicion_mayor_primo_matriz()

#49. Construir una función que reciba una matriz 5x5 y retorne el valor de su moda. La moda de un
# conjunto de datos es el dato que mas se repite.
def valor_moda():
    contador = 0
    repeticiones = []
    posicion = 0
    for i in range(5):
        for j in range(5):
            contador = 0
            for x in range(5):
                for y in range(5):
                    if matriz[i][j] == matriz[x][y]:
                        contador = contador + 1
            repeticiones.append(contador)
    moda = repeticiones[0]
    for num in repeticiones:
        if num > moda:
            moda = num
    contador = 0
    for num in repeticiones:
        contador = contador + 1
        if num == moda:
            break
    for i in range(5):
        for j in range(5):
            posicion = posicion + 1
            if posicion == contador:
                valormoda = matriz[i][j]
    print("La moda de la matriz (el valor que más se repite) es: " + str(valormoda))

matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige números para la matriz: ")))    
valor_moda()

#50. Construir una función que reciba una matriz 5x5 y retorne la cantidad de veces que se repite su
# moda.
def cantidad_moda():
    contador = 0
    repeticiones = []
    for i in range(5):
        for j in range(5):
            contador = 0
            for x in range(5):
                for y in range(5):
                    if matriz[i][j] == matriz[x][y]:
                        contador = contador + 1
            repeticiones.append(contador)
    moda = repeticiones[0]
    for num in repeticiones:
        if num > moda:
            moda = num
    print("Cantidad de veces que se repite su moda: " + str(moda))

matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige números para la matriz: ")))    
cantidad_moda()
