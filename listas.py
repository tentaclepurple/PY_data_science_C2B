
lista3 = ["Lunes", 1, "Mayo", 2018]
lista4 = [["Alberto", 1.75, 80],["Ana", 1.70, 65],["María", 1.90, 80]]
lista5 = [["Stanley Kubrick", ["Senderos de Gloria", 1957]], ["Woody Allen", ["Hannah y sus hermanas", 1986]]]
"""
De lista5, escribe el código para obtener los siguientes datos:
▪ Stanley Kubrick
▪ 1986
▪ ["Senderos de Gloria", 1957]
▪ ["Woody Allen", ["Hannah y sus hermanas", 1986]]
"""

print(lista5[0][0])
print(lista5[1][1][1])
print(lista5[0][1])
print(lista5[1])
print()

"""
Crea una lista con los nombres de los 6 primeros días de la semana. Llama a esa
lista, lista1
2. Crea una lista con los números del 1 al 7, llama a esa lista, lista2
7. Crea 2 copias de lista1, una en lista6 y otra en lista7. Después crea una nueva
lista8 que sea un alias de lista7. Crea una lista vacía en lista9
"""

lista1 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']   
lista2 = [1, 2, 3, 4, 5, 6, 7]

lista6 = list(lista1)
lista7 = list(lista1)
lista8 = lista7
lista9 = []
print()

"""
8. Elimina el "Miércoles" de la lista6, así como el "Viernes” de la lista8.
 Comprueba la lista7.
9. Ordena la lista1, lista2 y lista3. Estudia los resultados obtenidos.
10.Comprueba si ‘lunes’ existe en lista3.
11.Modifica el tercer elemento de la lista2, para que incluya el número 1000
"""

lista6.pop(2)
print(lista6)
del(lista8[4])
print(lista8)
print(lista7)
print(lista1)
lista1.sort()
print(lista1)
lista2.sort()
print(lista2)
#lista3.sort()
print(lista3)
print('Lunes' in lista3)
lista2[2] = 1000
print(lista2)
print()
"""
12.Añade ‘Domingo’ a la lista1.
13.Ejecuta el comando necesario para obtener el tamaño de la lista5. ¿Cuál es el
tamaño de la segunda lista en la lista4?
14.Extiende la lista6 con la lista3.
"""
lista1.append('Domingo')
print(lista1)
print(len(lista5))
print(len(lista4[1]))
lista6.extend(lista3)
print(lista6)