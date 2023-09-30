#!/usr/bin/env python
# coding: utf-8

# # NumPy 
# 
# NumPy (o Numpy) es una librería muy importante dentro del ecosistema Data Science en Python.  La mayor parte de las librerías en el ecosistema PyData, dependen o se apoyan en NumPy.
# 
# Numpy es muy rápido (usa librerías C).

# ## Instalación
# 
# **Puesto que la instalación de Python se ha ejecutado a través de Anaconda, Numpy ya viene instalado.  Los siguientes pasos nos ayudarían a instalar Numpy en caso de no tenerlo instalado.  A través de un terminal ejecutar:**
#     
#     conda install numpy
#     
# **En el caso de no tener instalado Anaconda, consultar [Documentación oficial Numpy's.](https://scipy.org/install.html)**

# ## Usando NumPy
# 
# Una vez instalado NumPy, lo importamos como librería:

# In[1]:


import numpy as np


# Numpy tiene muchas funciones y opciones.  No podremos cubrir todas ellas, pero nos vamos a centrar en algunos de los aspectos más importantes de Numpy: vectores,arrays (conjunto de datos del mismo tipo), matrices, y generación de números.
# 
# # Arrays Numpy (Arreglos)
# 
# Los arrays en Numpy son esencialmente vectores y matrices. Los vectores son arrays de una dimensión y las matrices de 2 dimensiones (aunque podemos tener matrices de 1 fila o columna).  Son de tipado **estático** y **homogéneo**.  Son más eficientes en el uso de la memoria.  Las funciones matemáticas complejas y computacionalmente costosas (p.ej: multiplicación de matrices) están implementadas en lenguajes compilados como C o Fortran).
# 
# ## Creación Arrays en Numpy
# 
# ### Desde una lista
# 
# Podemos generar un array directamente convirtiendo una lista o lista de listas:

# In[9]:


my_list = [1,2,3]
my_list


# In[10]:


arr = np.array(my_list)
arr


# In[11]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix


# In[12]:


np.array(my_matrix)


# In[13]:


my_list


# ## Métodos incluidos para la generación de Arrays

# ### arange
# 
# Genera un rango de datos a partir de un intervalo definido.

# In[14]:


np.arange(0,11)


# In[15]:


np.arange(0,11,2)


# In[33]:


np.arange(10,-1,-2)


# Comparación con **range()**, visto previamente.

# In[18]:


a = np.arange(0,11)
b = range(11)
print (type(a))
print (type(b))
print (a)
print (*b)


# In[22]:


a[-1]


# In[23]:


b[-1]


# ### Ceros y unos
# 
# Generar arrays de unos y ceros.

# In[24]:


np.zeros(3)


# In[25]:


np.zeros((5,5))


# In[26]:


np.ones(3)


# In[27]:


np.ones((3,3))


# ### linspace
# 
# Devuelve números espaciados uniformemente en un intervalo especificado.

# In[37]:


np.linspace(0,10,4)  #El intervalo viene definido por el número 4.  En este caso, divide el intervalo [0-10] en 4 partes iguales.


# In[35]:


np.linspace(0,10,50)


# ## eye
# 
# Crea una matriz identidad (sólo unos en la diagonal y el resto ceros)

# In[38]:


np.eye(5)


# ## Random 
# 
# Numpy tiene muchas maneras de generar arrays con números aleatorios:
# 
# ### rand
# Crea un array con la estructura elegida y lo rellena con datos aleatorios obtenidos a partir de una distribución uniforme.

# In[39]:


np.random.rand(2)


# In[41]:


np.random.rand(5,5)


# In[40]:


np.random.rand(5,5)


# ¿Hemos obtenido todos los mismos resultados? ¿Porqué obtenemos diferentes arrays?
# Ello se debe a que no estamos usando la misma 'semilla' para generar los números aleatorios.

# In[42]:


np.random.seed(30)
np.random.rand(5,5)


# In[43]:


np.random.seed(30)
np.random.rand(5,5)


# ### randn
# 
# Devuelve una muestra (o muestras) de una distribución estándar normal, al contrario que **rand** que es uniforme:
# 

# In[44]:


np.random.randn(2)


# In[45]:


np.random.randn(5,5)


# ### randint
# Devuelve enteros aleatorios entre un rango inferior (incluido) y otro superior (no incluido).  El rango inferior, debe ser menor que el rango superior.

# In[46]:


np.random.randint(1,100)  # El rango estaría comprendido entre 1 y 99,99999999999999999


# In[47]:


np.random.randint(1,100,10)  # Con el tercer argumento, nos devuelve 10 números aleatorios.


# In[49]:


np.random.randint(100,1,10)


# ## Atributos y métodos en Arrays
# 

# In[52]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10) # El método randint devuelve un entero del rango especificado.


# In[53]:


arr


# In[54]:


ranarr


# ## Reshape
# Devuelve un array que contiene los mismos datos, pero con una distribución diferente.

# In[55]:


arr.reshape(5,5)


# In[56]:


arr.reshape(25,1)


# ### max,min,argmax,argmin
# 
# Métodos prácticos para obtener los valores máximos y mínimos, o para encontrar su índice a través de argmin o argmax

# In[57]:


ranarr


# In[58]:


ranarr.max()


# In[59]:


ranarr.argmax()


# In[60]:


ranarr.min()


# In[61]:


ranarr.argmin()


# ## Shape
# 
# Shape es un atributo que devuelve una tupla con las dimensiones del array

# In[65]:


# Vector
arr.shape


# In[34]:


# Atención a los 2 sets de corchetes
arr.reshape(1,25)


# In[66]:


arr


# En el primer caso tenemos un array unidimensional con 25 elementos,  mientras que en el segundo caso tenemos un array de 2 dimensiones(1x25, 1 fila)

# In[71]:


print(arr.ndim)
print(arr.reshape(1,25).ndim)


# In[67]:


arr.reshape(1,25).shape


# In[68]:


arr.reshape(25,1)


# In[37]:


arr.reshape(25,1).shape


# In[7]:


arr.ndim


# ### dtype
# 
# El método dtype devuelve el tipo de dato en el array.

# In[75]:


arr.dtype


# # NumPy Indexación y Selección 
# 
# Veremos cómo seleccionar elementos o grupos de elementos de un array.

# In[2]:


#Generamos un array de muestra
arr = np.arange(0,11)


# In[3]:


arr


# ## Indexación y selección a través de "Corchetes"
# Es la manera más sencilla de seleccionar uno o varios elementos de un array.  Se parece mucho a las listas de python:

# In[4]:


#Devuelve el valor existente en la posición 9 del array
arr[8]


# In[5]:


#Devuelve los valores existentes en un rango
arr[1:5]


# In[6]:


#Devuelve los valores existentes en un rango
arr[0:5]


# ## Difusión
# 
# Los arrays en numpy tienen la propiedad de "difusión":

# In[9]:


#Asignar un valor a través de un rango en el índice (difusión)
arr[0:5]=100

arr


# In[10]:


# Resetear el array (vemos en un momento porqué)
arr = np.arange(0,11)

arr


# In[11]:


#Extraemos una "porción" de los datos
slice_of_arr = arr[0:6]

slice_of_arr


# In[12]:


#Cambiamos de una vez los valores existentes en la "porción" extraída
slice_of_arr[:]=99

slice_of_arr


# ¿Qué ha pasado con el array original?.  

# In[12]:


arr


# slice_of_arr es un alias de arr (ocupan el mismo espacio de memoria) y cualquier cambio en slice_of_arr se refleja en arr

# In[13]:


#Para generar una copia del array, debemos hacerlo explícitamente.
arr_copy = arr.copy()

arr_copy


# In[14]:


arr_copy[:]=100
print (arr_copy)
print (arr)


# ## Indexado de matrices 2D
# El formato general es **arr_2d[filas][columnas]** o **arr_2d[filas,columnas]**. La notación a través de comas, suele ser más clara.

# In[15]:


arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

arr_2d


# In[17]:


#Indexado de fila 1.  Ojo, la fila 1 es la segunda fila del array.  La primera fila es la 0.
arr_2d[1]


# In[18]:


# Extrayendo un elemento individual
arr_2d[1][0]


# In[19]:


# Extrayendo un elemento individual
arr_2d[1,0]


# In[13]:


# Extracción de elementos en un array 2D array.
arr_2d[:2,1:]


# In[20]:


#Extracción de la última fila
arr_2d[2]


# In[21]:


#Otra forma de extraer la última fila
arr_2d[2,:]


# In[22]:


#Generamos un nuevo array de ejemplo
arr_2d = np.arange(50).reshape(5,10)
arr_2d


# In[23]:


#Extraemos las filas 2 y 3 y las columnas 4 y 5.  Recordad que la primera fila y columna es la 0
arr_2d[1:3,3:5]


# Podemos verlo gráficamente

# 
# <img src='./logo/numpy_indexing.png' /></a>

# ## Selección de elementos en un array
# 

# In[14]:


arr = np.arange(1,11)
arr


# In[15]:


#Devuelve un lógico con los elementos que cumplen o no la condición a evaluar.
arr > 4


# In[17]:


bool_arr = arr>4


# In[18]:


bool_arr


# In[19]:


#Podemos usar el lógico creado, para seleccionar los elementos que cumplen la condición en el array
arr[bool_arr]


# In[20]:


#De manera directa
arr[arr>2]


# In[21]:


x = 2
arr[arr>x]


# ## Operaciones matemáticas

# In[8]:


import numpy as np
arr = np.arange(0,11)
arr


# In[9]:


#Suma de elementos de un array
arr + arr


# In[10]:


#Multiplicación
arr * arr


# In[11]:


#Sustracción
arr - arr


# In[12]:


# Mensaje de advertencia de división entre 0.  No es un error.  Reemplaza la advertencia por nan.  0/0 = nan
arr/arr


# In[13]:


# Nos muestra otra advertencia, pero no error.  1/0 = infinito
1/arr


# In[14]:


arr**3


# ## Funciones universales en arrays
# 
# El listado completo de funciones disponibles en numpy puede consultarse aquí: http://docs.scipy.org/doc/numpy/reference/ufuncs.html)
# Vemos algunos ejemplos:

# In[15]:


#Raíces cuadradas
np.sqrt(arr)


# In[16]:


#Exponenciales (e^)
np.exp(arr)


# In[17]:


np.max(arr) #Se obtiene el mismo resultado a través de arr.max()


# In[18]:


np.sin(arr) #Cálculo del seno


# In[19]:


np.log(arr) #Cálculo del logaritmo


# In[20]:


np.log2(arr) #Cálculo del logaritmo en base 2


# 
