""" 1. Escribir un programa que almacene 5 elementos distintos de cesta de la compra en una
lista y muestre en pantalla el mensaje "La lista de la compra contiene 5 elementos y
son: <elemento1>, <elemento2>, ..., <elemento5>
2. Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
3. Partiendo de la base del caso anterior, modifícalo para que sólo muestre los casos en
los que la nota sea inferior a 5 (suspenso).
4. Escribir un programa que pregunte al usuario los números de la lotería primitiva, los
almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
5. NOTA: No incluir el complementario y reintegro
6. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre
por pantalla en orden inverso separados por comas.
7. Escribir un programa que almacene el abecedario en una lista (sólo los valores en
minúscula y sin acentos), elimine de la lista las letras que ocupen posiciones múltiplos
de 3, y muestre por pantalla la lista resultante.
NOTA: Para este ejercicio es necesario el uso de iteraciones. Además puedes crear una
iteración para generar los valores a través de los códigos ASCII. Siendo el código ASCII
de la a:97 y el de la z:122. Añade la ñ tras la n. El código ASCII de la ñ es el 241
8. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.
9. NOTA: Para este ejemplo necesitas usar condicionales.
10. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número
de veces que contiene cada vocal.
NOTA: Para este ejemplo necesitas usar condicionales e iteraciones.
11. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22,
80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
NOTA: Para este ejemplo necesitas usar condicionales e iteraciones.
12. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y
muestre por pantalla su producto escalar.
NOTA: El producto escalar es el resultado de multiplicar 1*-1 + 2*0 + 3*2. Para este
ejemplo necesitas usar iteraciones.
""" 
def prodesc(a, b):
     return (a[0] * b[0], a[1] * b[1], a[2] * b[2])
v1 = (1, 2, 3)
v2 = (-1, 0, 2)
print(prodesc(v1, v2))


"""
13. Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una tupla y muestre por pantalla su media y desviación estándar.
Puedes probar a programar el proceso para la obtención de la media y la desviación
estándar ó cargar la librería numpy que contiene las funciones para calcular ambos
estadísticos.
NOTA: Para este ejemplo necesitas usar iteraciones. La función media es numpy.mean
y la función desviación estándar numpy.std  """

import numpy

def mean(tupla):
    return numpy.mean(tupla)
def std(tupla):
    return numpy.std(tupla)

entrada = input("Introduzca una serie de numeros separados por comas:\n")

numeros = [float(num) for num in entrada.split(",")]

""" numeros = []
for i in entrada.split(','):
    numeros.append(float(i)) """

tupla = tuple(numeros)
print("La tupla es:", tupla)
print("La media es: ", round(mean(tupla), 2), "y la desviación standard es: ", round(std(tupla), 2))