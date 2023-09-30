#!/usr/bin/env python
# coding: utf-8

# # Manipulación de rutas

# In[1]:


import os


# In[2]:


os.getcwd()


# In[9]:


path = r'C:\Users\german\Documents\00.Trabajo\01.C2B\35.Python Intermedio - C2B (15h)\Ejercicio'
#path = 'C:\\Users\\ibai\\tmp'

# Obtener ultimo componente
os.path.basename(path)


# In[10]:


# Obtener el nombre del directorio
os.path.dirname(path)


# In[13]:


# Unir componentes a la ruta
os.path.join(os.path.basename(path),'tmp\\')
# os.path.join('tmp\\',os.path.basename(path))


# In[12]:


# Expandir una ruta
path1 = '~\\datos\\.andoni\\Productos.txt'
os.path.expanduser(path1)


# In[14]:


# Separar la extensión del archivo
os.path.splitext(path1)


# In[15]:


# Y podemos quedarnos con la extensión
os.path.splitext(path1)[1]


# In[33]:


# ¿Se os ocurre otra manera de extraer la extensión en path1?
path1.split('.')[-1]


# ### Existencia de ficheros y directorios

# In[17]:


os.path.exists('./datos/csv')


# In[18]:


os.path.exists('./data')


# In[19]:


os.path.exists('./datos/tmp')


# In[20]:


os.path.isfile('./data/calendario_laboral_2022.csv')


# In[21]:


os.path.isdir('./data')


# In[22]:


os.path.isdir('./data/calendario_laboral_2022.csv')


# In[23]:


os.path.getsize('./data/calendario_laboral_2022.csv')


# In[24]:


date = os.path.getmtime('./data/calendario_laboral_2022.csv')
date 
# devuelve el tiempo (en segundos) desde el 1 de enero de 1970 hasta el último acceso


# In[27]:


import time
time.ctime(date)


# ### Listas de archivos

# In[25]:


import os
names = os.listdir('./data')
names


# In[30]:


import glob
files_text = glob.glob('.\data\calendario*')

for file in files_text:
    print(file)
    #Cargar el archivo


# In[31]:


import glob
files_text = glob.glob('.\data\*.csv')

for file in files_text:
    print(file)
    #Cargar el archivo


# # OPERACIONES CON FICHEROS

# ### Abrir, Leer y Cerrar archivos

# In[34]:


# Abre archivo en modo lectura
archivo = open('./data/calendario_laboral_2022.csv',mode='r', encoding='latin-1')


# In[35]:


# Leer archivo completo
cadena = archivo.read()
cadena


# In[36]:


# Cerrar archivo
archivo.close()


# In[37]:


archivo = open('./data/calendario_laboral_2022.csv',mode='r', encoding='latin-1')

# Leer los n primeros bytes
cadena1 = archivo.read(4)
cadena1


# In[38]:


# Leer los 4 siguientes bytes
cadena2 = archivo.read(4)
cadena2


# In[39]:


# Leer el resto del archivo.  Ojo, el puntero está situado ahora en la posición 8
cadena3 = archivo.read()
cadena3


# In[40]:


archivo.close()


# #### Leer archivo linea a linea

# In[41]:


archivo = open('./data/calendario_laboral_2022.csv',mode='r', encoding = 'latin-1')
resultado = []
# Bucle infinito para leer linea a linea
while True:
    linea = archivo.readline()  # leer linea
    if not linea:
        break   # Si no hay linea se para el bucle  
    resultado.append(linea)
archivo.close()
resultado


# #### Leer todas las lineas de un archivo (a través de for)
# ##### En este caso, podríamos seleccionar el rango de líneas a leer, definiendo numlin y el total de iteraciones

# In[42]:


archivo = open('./data/calendario_laboral_2022.csv',mode='r', encoding="latin-1")

lista = archivo.readlines()

numlin = 0 # Iniciar variable contador

# Recorremos todos los elementos que hay en la lista
for linea in lista:
    numlin += 1     # Incrementamos contador
    print(numlin, linea)

archivo.close()


# In[60]:


# ¿Cómo podríamos leer únicamente de la línea 25 a la 50?


# #### With-As ( Cierra archivo y libera memoria )

# In[43]:


with open("./data/calendario_laboral_2022.csv", encoding='latin-1') as archivo:
    for linea in archivo:
        print(linea)


# ### Escribir en archivo

# In[44]:


cadena1 = 'Este es un hermoso día'
cadena2 = 'Para cargar por primera vez archivos'

archivo = open('./data/prueba.txt',mode='w')
archivo.write(cadena1 + '\n')  # + cadena2
archivo.write(cadena2)
archivo.close()


# In[45]:


archivo = open('./data/prueba.txt',mode='r')
archivo.read()


# In[46]:


archivo.close()


# In[47]:


archivo = open('./data/prueba.txt',mode='w')
archivo.write("Adios\nmundo")
archivo.close()


# #### Escribir con una lista

# In[48]:


lista = ['Uno','Dos','Tres','Cuatro']


# In[49]:


archivo = open('./data/prueba.txt',mode='w')
archivo.writelines(lista) 
archivo.close() 


# In[50]:


lista = ['Uno\n','Dos\n','Tres\n','Cuatro\n']
archivo = open('./data/prueba.txt',mode='w')
archivo.writelines(lista) 
archivo.close() 


# ### Movimiento de puntero

# In[51]:


archivo = open('./data/prueba.txt',mode='r')
archivo.seek(6) # Movemos el puntero al quinto byte.  Ojo!, los saltos de línea \n cuentan como un byte
cadena = archivo.read(5) # Leemos 5 bytes desde la posicion actual


# In[52]:


# Mostrar el contenido de 5 bytes desde la posición 6
cadena


# In[53]:


# Mostrar la posición del puntero en el archivo
archivo.tell()


# ### Leer y escribir a un archivo pickle
# 
# Pickle nos permite serializar (y de-serializar) objetos en Python.  Con ello podemos almacenar objetos en un archivo, sin necesidad de convertirlo.

# In[54]:


import pickle

lista = ['Lunes','Martes','Miercoles','Jueves','Viernes']
fichero = open('./data/datospickle.dat','wb')
# Cargamos la lista en el ficherp
pickle.dump(lista, fichero) 
fichero.close()


# In[55]:


del lista #Borrar memoria de la lista
fichero = open('./data/datospickle.dat','rb')
#Cargamos el fichero en una lista
lista = pickle.load(fichero)
print(lista)
fichero.close()


# In[56]:


lista

