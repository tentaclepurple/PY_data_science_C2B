"""13. Escribir un programa que pregunte por una muestra de números, separados por
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