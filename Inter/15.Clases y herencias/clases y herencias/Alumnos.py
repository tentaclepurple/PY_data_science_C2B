# -*- coding: utf-8 -*-
"""

"""
# Definimos la clase UG, que hereda de
# MITPerson, que a su vez hereda de Person
class UG(MITPerson):
    # Usamos el método MITPerson para crear
    # una nueva instancia que además
    # usará los métodos de Person
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
	# Añadimos el atributo year
	# a las instancias creadas 
	# a través de UG
        self.year = classYear
    # Metodo para definir el año
    # en que empezó las clases
    def getClass(self):
        return self.year
    # Usamos el método heredado speak
    # pero le añadimos nuestro texto.
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

# Creamos una nueva clase para los 
# estudiantes graduados.
class Grad(MITPerson):
    pass

# creamos una función que nos diga si una
# instancia pertenece o bien a la clase UG
# o a la clase Grad.
def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Arash Ferdowsi', 2018)
s4 = Grad('Drew Houston')
s5 = UG('Mark Zuckerberg', 2019)

studentList = [s1, s2, s3, s5, s4]
print (s1)

# Comprobamos cuando empezó a estudiar
print(s1.getClass())

# Miramos a ver qué dice con el método speak
print (s1.speak("..."))

# Probamos con la segunda persona
print (s2.speak("@#½~#|"))


