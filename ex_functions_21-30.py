
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
