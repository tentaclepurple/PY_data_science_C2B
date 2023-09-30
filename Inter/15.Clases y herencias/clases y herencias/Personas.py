# -*- coding: utf-8 -*-

"""
hacemos uso de la librería datetime
que me permite trabajar con fechas,
convertir un texto a su representación
en una fecha
"""

import datetime

# Definimos la clase Person, que hereda
# del objeto object
class Person(object):
    # Generamos una instancia nueva
    # para un objeto Person vacío al que 
    # añadiremos métodos y atributos.
    def __init__(self, name):
        """Crea un persona llamada name"""
        self.name = name
        self.birthday = None
        """para obtener el apellido, hacemos
	   uso del metodo split, y partimos
	   el nombre por el espacio.  Una
	   vez partido, nos quedamos con
	   el último elemento de name."""
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """Devuelve el apellido de self (instancia
	   creada del objeto que a llamado a la 
	   clase"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """Definimos el cumpleaños de self"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """Devuelve, la edad de self en días"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """Devuelve True, si el nombre de self es más
	   pequeño que otros nombres, y False en caso contrario"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName



    # other methods

    def __str__(self):
        """Devuelve el nombre de self"""
        return self.name
        

# ejemplo de uso
# introducimos unos nombres y
# fechas de nacimiento.
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')


personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)
    

