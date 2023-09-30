# -*- coding: utf-8 -*-
"""

"""

class Professor(MITPerson):
    # Inicializamos la clase Professor, a través
    # de la clase MITPerson.
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
	# aparte de los métodos heredados
	# de MITPerson, añadimos el 
	# atribudo departamento.
        self.department = department
    
    # Modificamos ligeramente lo que muestra
    # el método speak heredado de MITPerson.
    # En este método, "oculta" el método original
    # para que muestre un texto diferente.     
    def speak(self, utterance):
        newUtterance = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, newUtterance + utterance)
        
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)
        

faculty = Professor('Doctor Arrogant', 'six')

# Mostramos el método speak de la clase MITPerson
print(m1.speak("Hola, otra vez"))

# Mostramos el método speak de la clase MITPerson, pero 
# ahora para una clase que lo hereda.
# Usamos el método speak de la clase UG, la cual
# hereda el método speak de MITPerson y le añade
# "lo dice un estudiante"
print (s1.speak("lo dice un estudiante"))

# Usa el método de Professor que hereda
# el método de MITPerson
print (faculty.speak("'La facultad te saluda'"))

# El método lecture, usa el método Professor speak
# Si una clase tiene un método propio que también tiene
# la clase de la que hereda, se usará el método propio
# frente al de la clase superior.
print (faculty.lecture("estás a punto de terminar"))


# Comprobamos las clases que tenemos
import sys, inspect
clases = inspect.getmembers(sys.modules[__name__], inspect.isclass)
print(clases)

# Comprobamos de qué hereda UG
herencias = inspect.getmro(UG)
print(herencias)


