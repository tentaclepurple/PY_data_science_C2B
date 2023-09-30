# -*- coding: utf-8 -*-
"""

"""

class Grades(object):
    """Inicializamos la creación de cuadernos de grados"""
    def __init__(self):
        """Generamos un cuaderno de grados vacío"""
        self.students = []  # lista de objetos estudiantes
        self.grades = {}    # me interesa poder obtener
                            # las notas de un alumno 
                            # a través de su idNum
        self.isSorted = True # True si self.students está ordenado

    def addStudent(self, student):
        """Asume: student es un tipo Student
           Añade student al cuaderno de grados"""
        if student in self.students:
            raise ValueError('Estudiante Repetido')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Asume: grade es coma flotante
           Añade grade a la lista de grados del estudiante"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('El estudiante no está en el cuaderno de grados')

    def getGrades(self, student):
        """Devuelve los grados de un estudiante"""
        try:    # devuelve una copia de los grados del estudiante
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('El estudiante no está en el cuaderno de grados')


    def allStudents(self):
        """Devuelve una lista con los estudiantes del libro de grados"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] 
        #devuelve una copia de la lista de estudiantes



def gradeReport(course):
    """Supone: Course es un tipo grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append("La media del grado de " +str(s) + ' es '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' no tiene grado')
    return '\n'.join(report)
    

# Creamos una BBDD de estudiantes
# ugX alumnos que todavía no han terminado su grado  
# gX alumnos que han terminado su grado
ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')



# Creamos un libro de grados.
# Introducimos los elementos desordenados
# Veremos que no importa.
six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)



# Añadimos las notas de los grados
# para los diferentes ejemplos.
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print()

print(gradeReport(six00))

# Anadimos más notas.
six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print()

print(gradeReport(six00))

# Comprobación de existencia de alumno en cuaderno
# Creo el alumno pero no lo añado al cuaderno
# de notas
ug5 = UG('Germán Alonso', 2022)
six00.getGrades(ug5)


# Imprimir el listado de alumnos
# del libro de grados ORDENADOS 
# por ID.  
for s in six00.allStudents():
    print (s)

