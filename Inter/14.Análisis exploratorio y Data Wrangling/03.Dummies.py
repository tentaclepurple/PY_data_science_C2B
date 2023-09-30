#!/usr/bin/env python
# coding: utf-8

# # Variables dummy

# Un conjunto de datos puede contener varios tipos de valores, y a veces consta de valores categóricos. Para utilizar esos valores categóricos en la programación de forma eficiente, creamos variables ficticias. Una variable ficticia es una variable binaria que indica si una variable categórica separada toma un valor específico. Necesitamos aplicar esta transformación para poder trabajar con Scikit Learn.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

import warnings
warnings.filterwarnings('ignore')

pd.options.display.float_format = '{:.2f}'.format #Desactivar notación científica en pandas:
np.set_printoptions(suppress=True) #Desactivar notación científica en numpy:
pd.set_option('display.max_columns', None) #comando para mostrar todas las columnas


# Sintaxis a usar:
# 
# **pd.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None)**
# 
# * get_dummies: función para creación de las dummies,
# * prefix: permite definir el prefijo a añadir a las nuevas columnas
# * prefix_sep: permite definir el separador del prefijo
# * drop_first: Elimina la primera variable dummy generada
# * columns: columnas a dummificar
# 

# In[2]:


# Creamos un set de datos
df = pd.DataFrame({
    'Temperatura': ['Frío', 'Calor', 'Templado', 'Frío']
})
df


# In[3]:


# Creamos las dummies...
pd.get_dummies(df)


# Pasamos de un set de 4x1 a otro de 4x3.  El total de filas se conservan, y se generan tantas columnas como valores únicos existen en la columna a 'dummificar'

# In[5]:


# Otro ejemplo
df2 = pd.DataFrame({'A': ['Kepa', 'Lirain', 'Saioa'],
                   'B': ['Algorta', 'Orduña', 'Getaria'],
                   'C': [1, 2, 3]})
df2


# In[6]:


pd.get_dummies(df2)


# Nos puede interesar dummificar sólo una columna de varias...

# In[7]:


pd.get_dummies(df2[['A']])


# El ejemplo anterior SÓLO genera las dummies para una columna, pero nos puede interesar mantener el resto de columnas...

# In[9]:


pd.get_dummies(data = df2, columns = ['A'])


# Podemos dar nombre a las dummies

# In[11]:


pd.get_dummies(data = df2, prefix='Nombre', prefix_sep="_", columns = ['A'])


# Simplificando los nombres de columna al máximo.

# In[12]:


pd.get_dummies(data = df2, prefix='', prefix_sep='', columns = ['A'])


# Cuando vayamos a modelar, y con el fin de evitar problemas de colinealidad, es necesario eliminar una de las variables dummy generadas.  Para ello...

# In[14]:


pd.get_dummies(data = df2, prefix='', prefix_sep='', columns = ['A'], drop_first=True)

