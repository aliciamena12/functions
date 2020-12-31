
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
