
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
