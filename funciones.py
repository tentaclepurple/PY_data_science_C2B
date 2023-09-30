""" 1. Crear una función que multiplique 2 números, mediante sumas. Llama a
dicha función multiplicación.
"""
def multiplicacion (x, y):
	i = 0
	result = 0
	while i < y:
		result += x
		i += 1
	return result


print (multiplicacion(0, 8))

"""
2. Crear una función que calcule el cuadrado de un número (entero o no).
"""
def cuadrado (x):
	return x * x

print (cuadrado(8))


"""
3. Crear una función que devuelva el valor de una ecuación de segundo
grado.
NOTA: Las ecuaciones de segundo grado se resuelven a partir de:
a * x 2 + b * x + c
"""
def ecuacion(a, b, c, x):
    return a*x**2+b*x+c
"""
4. Crear una función llamada imprimirNombre que, dado un nombre y
apellido, los invierta (a menos que se le indique lo contrario).
Ej: imprimirNombre (“John”,“Smith”). La función devolverá Smith John
imprimirNombre (“John”,“Smith”, False). La función devolverá John
Smith
"""
def imprimirNombre (nombre, apellido, compr = True):
    if compr == True:
        print(apellido, nombre)
    elif compr == False:
        print(nombre, apellido)

imprimirNombre('paco', 'gonzalez')  

"""
5. Desarrolla un función que calcule el máximo comun divisor de 2 números.
La idea es usar iteración. El máximo comun divisor, es aquel número que
divide a otros por 2 y su resto es 0.
Empezar comprobando la división entre el mayor y el menor número.
Posteriormente ir reduciendo el menor número en 1 e ir probando la
división entre el mayor y menor.
El máximo común divisor, será el mayor número que divida a los 2 con
resto = 0
"""

def mcd(a, b):
    mayor = max(a, b)
    menor = min(a, b)
    while mayor % menor != 0:
        tmp = mayor % menor
        mayor = menor 
        menor = tmp
    return menor

print(mcd(24, 36))

#---#

def mcdopt(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

print(mcdopt(24, 36))


"""
6. Desarrolla una función que calcule la potencia de un número dado, usando
la multiplicación. 2^3 = 2 * 2 * 2
"""
def pow(num, n):
    #calcula la potencia a la n
	if n == 0:
		return 1
	else:
		return num * pow(num, n - 1)

print(pow(2, 4))


"""
7. Desarrollar una función que devuelva la cuota a pagar en un préstamo a un
año con un interés anual del 12%. La cuota dependerá de los intereses a
pagar.
NOTA: Interes = Capital * (interes anual / 100) /12
Cuota = Capital / 12 + Intereses
"""
def interesesmensuales (cap, intanual):
    #funcion para calcular los intereses mensuales
    return cap * (intanual / 100) / 12

def cuota (cap, intanual):
    #calcular la cuota llamando a la funcion intesesesmensuales para sumarlos
	#a la mensualidad
	return round((cap / 12) + (interesesmensuales(cap, intanual)), 4)

print(cuota(100000, 12))


"""
8. Desarrollar una función que calcule si una cadena de texto tiene un numero
par o impar de caracteres
"""
def strparimpar(str):
    if len(str) % 2 == 0:
        print("La cadena es par")
    else:
        print("La cadena es impar")
        
strparimpar(input("Escriba una cadena de caracteres:\n"))


"""
9. Desarrollar una función que encuentre los números divisibles entre 7 (pero
no 5) para todos los números entre 1000 y 2000 (ambos incluidos). """

def multiplos7 ():
    lista = []
    for i in range(1000, 2001):
          if i % 7 == 0 and i % 5 != 0:
                lista.append(i)
    return lista
            
print(multiplos7())
