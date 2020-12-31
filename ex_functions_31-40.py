
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
