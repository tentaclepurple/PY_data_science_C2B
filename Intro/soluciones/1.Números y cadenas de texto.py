#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 09:51:51 2022

@author: mydoctor
"""

# 1. ¿A qué tipo de variables corresponden los siguientes valores?
# 1) 3.14159
float
# 2) 56
integer
# 3) -56
integer
# 4) 2.0
float
# 5) "Miércoles"
string
# 6) 5.4e+10
float

# 2.Ejecuta las siguientes operaciones:
3 + 2 -10
3.0 + 2 - 10
3 * 2
10 / 3
(1 + 3) / 4
1 + 3 / 4
2**2
3**2
25**0.5
625**.25

# 3. Asigna cada una de las operaciones anteriores a una variable
a = 3 + 2 -10
b = 3.0 + 2 - 10
c = 3 * 2
d = 10 / 3
e = (1 + 3) / 4
f = 1 + 3 / 4
g = 2**2
h = 3**2
i = 25**0.5
j = 625**.25

# 4. Comprueba qué tipo de variable has generado en el punto anteriores
type(a)
type(b)
type(c)
type(d)
type(e)
type(f)
type(g)
type(h)
type(i)
type(j)

# 5. Genera las siguientes cadenas de texto: "Hola Mundo", 'Hola Mundo', "abcdefghi", "123456" y asígnalas a las variables, cadena1, cadena2, cadena3, cadena4
cadena1 = "Hola Mundo"
cadena2 = 'Hola Mundo'
cadena3 = "abcdefghi"
cadena4 = "123456"

# 6. Comprueba que las variables generadas sean de tipo texto.
type(cadena1)
type(cadena2)
type(cadena3)
type(cadena4)

# 7. Obtén la longitud de cada cadena de texto.
len(cadena1)
len(cadena2)
len(cadena3)
len(cadena4)

# 8. Realiza las siguientes operaciones de concatenación:
# ▪ cadena1 y cadena2 y asigna el resultado a cadena5
# ▪ cadena1 y cadena3 pero separando ambas cadenas con un espacio y
#   asigna el resultado a cadena6
# ▪ duplica cadena1 y asigna el resultado a cadena7
#   comprueba la longitud de las nuevas cadenas generadas (cadena5,
#   cadena6, cadena7)
cadena5 = cadena1 + cadena2
cadena6 = cadena1 + " " + cadena3
cadena7 = 2 * cadena1
len(cadena5)
len(cadena6)
len(cadena7)

# 9. De la cadena1, extrae (usando un solo comando):
# -el carácter situado en la primera posición,
# -los caracteres de las posiciones 2 y 3
# -los caracteres desde la 2ªposición hasta la anteúltima
# -los caracteres de las posiciones 1, 4, 7, 10
cadena1[0]
cadena1[1:3]
cadena1[1:-1]
cadena1[::3]

# 10.Mediante un comparador de pertenencia, comprueba si existen las cadenas H, M, Ma en cadena1
'H' in cadena1
'M' in cadena1
'Ma' in cadena1

'h' in cadena1

# 11.Convierte cadena1 en mayúsculas y asigna el resultado a cadena1mayus.
# Convierte cadena1 en minúsculas y asigna el resultado a cadena1minus
cadena1mayus = cadena1.upper()
cadena1minus = cadena1.lower()

# 12.Comprueba cuántas veces aparece la cadena "undo" en cadena5
cadena5.count("undo")

# 13.Reemplaza la cadena "Ho" en cadena1 por "Mo" y asigna el resultado a
# cadena6
cadena6 = cadena1.replace("Ho", "Mo")

