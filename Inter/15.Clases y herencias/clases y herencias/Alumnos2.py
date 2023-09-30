# -*- coding: utf-8 -*-
"""

"""
# Definimos la clase Student, que hereda
# de MITPerson.

class Student(MITPerson):
    pass


# Definimos la clase UG, que hereda de
# Student, que a su vez hereda de MITPerson
# y de Person
class UG(Student):
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

# Modificamos la clase para que dependa de Student
class Grad(Student):
    pass

# Definimos la clase TransferStudent
class TransferStudent(Student):
    pass

# Modificamos la función isStudent para que apunte
# a la clase correcta a la hora de devolver si
# un objeto es un estudiante del MIT
def isStudent(obj):
    return isinstance(obj,Student)


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Arash Ferdowsi', 2018)
s4 = Grad('Drew Houston')
s5 = UG('Mark Zuckerberg', 2019)
s6 = TransferStudent('Robert deNiro')

studentList = [s1, s2, s3, s5, s4]
print (s1)

# Comprobamos cuando empezó a estudiar
print(s1.getClass())

# Miramos a ver qué dice con el método speak
print (s1.speak("..."))

# Probamos con la segunda persona
print (s2.speak("@#½~#|"))


