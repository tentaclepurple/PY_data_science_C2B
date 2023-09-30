""" 1. Supongamos los ficheros baterias.py, inventario.py se encuentran en la
misma carpeta.
Si ejecutamos inventario.py, ¿qué ocurre?
""" 
#1) Imprime aa 
"""
2) Imprime AA
3) Devuelve un error
############ fichero baterias.py #######################
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
########################################################
############ fichero inventario.py #####################
aa = "aa"
tripleA = "aaa"
print(aa)
########################################################
2. Supongamos los ficheros baterias.py, inventario.py se encuentran en la
misma carpeta.
Si ejecutamos inventario.py, ¿qué ocurre?
1) Imprime aa
2) Imprime AA
"""
#3) Devuelve un error 
"""
############ fichero baterias.py #######################
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
########################################################
############ fichero inventario.py #####################
aa = "aa"
tripleA = "aaa"
print(baterias.aa)
########################################################
3. Supongamos los ficheros baterias.py, inventario.py se encuentran en la
misma carpeta.
Si ejecutamos inventario.py, ¿qué ocurre?
1) Imprime aa
"""
#2) Imprime AA
"""
3) Devuelve un error
############ fichero baterias.py #######################
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
########################################################
############ fichero inventario.py #####################
import baterias
aa = "aa"
tripleA = "aaa"
print(baterias.aa)
########################################################
4. Supongamos los ficheros baterias.py, inventario.py se encuentran en la
misma carpeta.
Si ejecutamos inventario.py, ¿qué ocurre?
1) Imprime AA AAA C D
2) Imprime aa aaa c d
""" 
#3) Imprime aa AAA C D
"""
4) Devuelve un error
############ fichero baterias.py #######################
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
########################################################
############ fichero inventario.py #####################
from baterias import *
aa = "aa"
print(aa, aaa, c, d)
######################################################## """