


"""
1. Crear un programa que imprima una secuencia de números pares, que
empezando por el 0, su número más alto sea menor que 30
"""
x = 0
while x < 30:
    print(x)
    x += 2


"""
2. Supongamos el siguiente programa:


 # la variable letra en el loop, itera sobre todos los caracteres
 # de la cadena, incluidas comas, espacios y símbolos

 
Sin ejecutar el código en Python, analiza el código y responde a las cuestiones.
1) ¿Cuál es el valor de la variable contador durante la iteración 0?
    0-11
2) ¿Cuál es el valor de la variable contador durante la iteración 1?
    11-22
3) ¿Cuál es el valor de la variable contador durante la iteración 2?
    22-33
4) ¿Cuál es el valor de la variable contador durante la iteración 3?
    33-44
5) ¿Cuál es el valor de la variable contador durante la iteración 4?
    44-55
iteracion = 0
contador = 0
while iteracion < 5:
    for letra in "¡Hola mundo!":
        contador += 1
    iteracion += 1
"""



"""
3. Supongamos el siguiente programa:

1) ¿Cuál es el valor de la variable contador durante la iteración 0?
    0-11
2) ¿Cuál es el valor de la variable contador durante la iteración 1?
    0-11
3) ¿Cuál es el valor de la variable contador durante la iteración 2?
    0-11
4) ¿Cuál es el valor de la variable contador durante la iteración 3?
    0-11
5) ¿Cuál es el valor de la variable contador durante la iteración 4?
    0-11
    
iteracion = 0
while iteracion < 5:
    contador = 0
    for letra in "¡Hola mundo!":
        contador += 1
    iteracion += 1 
"""



"""
4. Supongamos el siguiente programa:

1) ¿Cuántas veces se ejecuta el comando print?
    5
2) ¿Cuál es el máximo valor que toma la variable iteracion?
    5
3) ¿Cuál es el máximo valor de la variable contador?
    12
4) ¿Cuál es el menor valor de la variable contador?
    0

iteracion = 0
while iteracion < 5:
    contador = 0
    for letra in "¡Hola mundo!":
        contador += 1
        if iteracion % 2 == 0:
            break
    print("hola") 
    iteracion += 1 

"""

"""
5. Crear un programa que tras introducir un número, nos diga si dicho número tiene
cubo perfecto o no.
Nota: 8 cubo perfecto de 2, 27 cubo perfecto de 3, 64 cubo perfecto de 4, …
"""
num = int(input("Introduzca número mayor que 0:\n"))

raiz_cubica = 0
while raiz_cubica ** 3 < num:
    raiz_cubica += 1

if raiz_cubica ** 3 == num:
    print(f"{num} es un cubo perfecto")
else:
    print(f"{num} no es un cubo perfecto")



"""
6. Crea un programa que añada elementos a una lista de manera indefinida,
mientras pulsemos una tecla.
NOTA: Cada vez que introduzcamos un elemento en la lista, nos deberá preguntar
si queremos seguir añadiendo elementos, si no pulsemos una tecla en concreto,
el proceso terminará.
"""
a = input("Presione 'q' para salir o cualquier otra tecla para continuar\n")
lista = list()
while a != 'q':
    lista.append(input("Introduzca elemento a la lista:\n"))
    print(lista)
    a = input("Presione 'q' para salir o cualquier otra tecla para continuar\n")
    if a == 'q':
        break



"""
7. Crea un programa que calcule el factorial de un número.
Nota: Factorial de 4 = 4! = 4 * 3 * 2 * 1
Factorial de 5 = 5! = 5 * 4 * 3 * 2 * 1
"""


def factorial (nb):
    if nb == 0:
        return 1
    else:
	    return nb * factorial(nb - 1)

x = int(input("Introduce un num:\n"))
f = factorial(x)
print(f)

"""
8. Crear un programa que extráiga el total de vocales existentes en una cadena de
texto.
NOTA: El programa nos pedirá introducir una cadena de texto y nos devolverá el
total de vocales. Para simplificar la resolución del ejercicio, asegúrate de
convertir la cadena de texto a analizar a minúsculas.
"""
txt = input("Introduzca un texto:\n")
txt = txt.lower()
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for i in txt:
    if i in vowels:
        count += 1
if count == 0:
    print ("No hay ninguna vocal")
elif count == 1:
    print (f"Hay {count} vocal")
else:
    print (f"Hay {count} vocales")

"""
9. Crear un programa que nos diga si una cadena de texto, contiene las vocales “i”
y “u”.
"""
txt = input("Introduzca un texto:\n")



txt = txt.lower()
if 'i' in txt and 'u' in txt:
    print ("Yes")
else:
    print ("Nope")



counti = 0
countu = 0
for i in txt:
	if i == 'i':
		counti += 1
	elif i == 'u':
		countu +=1
if counti > 0 and countu > 0:
	print("Hay al menos 1 'i' y 1 'u'")
else:
	print("No se dan las condiciones")


"""
10.Desarrollar un programa que dado un número de mes (1 al 12), nos diga el
nombre del mes y liste los 11 siguientes meses.
Pej, si introducimos un 8, el programa deberá decir Agosto, e imprimir en pantalla
Agosto, Septiembre, Octubre, Noviembre, Diciembre, Enero, ... , Julio
"""

try:
	tuple = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
	num = (int(input("Introduzca número de mes:\n"))) - 1
	print(f"El mes correspondiente es {tuple[num]}")
except IndexError:
	print("No ha introducido un número de mes válido")


"""
11.Desarrollar un programa que dada una cadena de texto, la invierta. Intenta
plantear el ejercicio con WHILE y FOR
"""

txt = input("Introduzca un texto:\n")
i = 0
txt1 = ""
for j in txt:
    txt1 += txt[-i - 1]
    i += 1
print(txt1)