# -*- coding: utf-8 -*-
"""

"""

class MITPerson(Person):
    nextIdNum = 0 # objeto definid dentro de la clase
		  # no pertenece a la instancia, sino
		  # a la clase.

    def __init__(self, name):
        Person.__init__(self, name) # inicializa los atributos
				    # del objeto, llamando
                         # a la clase Person
                         # de esta manera, hereda
                         # sus métodos de dicha clase
        # Nuevo atributo para MITPerson: ID ÚNICO
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # ordenar MITPerson por ID, no nombre!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    # añadimos un método llamado speak
    # a esta clase.
    # este método, devuelve el apellido
    # para ese objeto.  método para 
    # obtener el apellido viene definido
    # en la clase Person
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
        

# Ejemplo de uso
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)


print (m1)
print (m1.speak("Hola"))


MITPersonList = [m1, m2, m3]

for e in MITPersonList:
    print(e)

# Ordenamos por ID    
MITPersonList.sort()

print()

for e in MITPersonList:
    print(e)
            
# Creamos 4 nuevas personas
# Varias con el mismo nombre
# para luego ordenarlas
# Las 3 primeras personas, llaman
# a la clase MITPerson que incluye
# un IdNum, sin embargo la 4
# llama a la clase Person que no 
# tiene definido ese atributo 
            
p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')    


# Comprobamos que pasa si 
# comparamos estos elementos.
# La comparación se hace en 
# base al idNum
p1 < p2
p1 < p4

# Vemos que falla, puesto que 
# p4 no tiene el atributo idNum
# definido.

p4 < p1
# Sin embargo en este caso nos
# devuelve False
# MITPerson y Person tienen sus 
# propios métodos __lt__
# Cuando hacemos p1<p4
# Python espera que ambas instancias
# p1 y p4 tengan los mismo métodos.
# p1 hereda los métodos de Person
# igual que p4.
# Sin embargo p4 no hereda los 
# métodos de p1.
# Cuando llamamos a __lt__ 
# en el caso p1 < p4, las 2 instancias
# no comparten los mismos atributos y 
# falla.  mira los atributos de p1 y 
# luego los compara con los de p4 que
# no tiene idNum
# Sin embargo al hacerlo a la inversa,
# p4 < p1, Python está comparando los
# atributos de p4 con los de p1, y p4
# tiene menos atributos que p1 por lo 
# que solo compara los atributos de p4
# con los que tiene p1
