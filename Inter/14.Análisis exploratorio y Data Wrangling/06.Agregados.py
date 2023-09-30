#!/usr/bin/env python
# coding: utf-8

# # Agregados y pivotados (tablas )

# In[2]:


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


# In[3]:


# Cargamos los datos
os.chdir(r"/home/mydoctor/Documents/03.Trabajos/01.C2B/17.Python avanzado - C2B (15h)/data")
data = pd.read_csv("SalePrice.csv")
data.head()


# In[8]:


data.shape


# Funciones de agregación disponibles:
# * count()
# * sum()
# * mean()
# * median()
# * min()
# * max()
# * mode()
# * std()
# * var()
# 

# # 1.Agregados por valor de una columna

# In[9]:


# Total registros por grupo (C(all), FV, ...)
data.groupby(['MSZoning']).size()


# In[12]:


# count() no cuenta los valores perdidos y por eso nos devuelve cantidades diferentes a size()
data.groupby(['MSZoning']).count()


# In[14]:


# valores medios de la variable mszoning agrupada.
data.groupby(['MSZoning']).mean()


# In[8]:


Zona=data.groupby(['MSZoning']).agg(len).reset_index()

# Contar valores unicos por agrupacion.
ZonaUni=data.groupby(['MSZoning']).agg(len).reset_index().nunique()

# Tambien podemos realizar el sumatorio.
# Solo incluye variables numericas.
ZonaSuma=data.groupby(['MSZoning']).agg(sum).reset_index()


# In[10]:


Zona


# In[15]:


ZonaUni


# In[5]:


ZonaSuma


# # 2.Agregados por los valores de varias columnas

# In[20]:


data.groupby(['MSZoning',"YrSold"]).agg(len)


# In[21]:


# También podemos resetear los índices generados a través de la agregación
data.groupby(['MSZoning',"YrSold"]).agg(len).reset_index()


# In[29]:


data.groupby(['MSZoning',"YrSold"]).agg(sum).reset_index()


# In[7]:


data.groupby(['MSZoning',"YrSold"]).agg(np.mean).reset_index()


# # 3.Fundido de tablas (melt)

# Pasamos de tablas en formato ancho a largo

# In[12]:


# Fundimos la tabla original en base a la variable Id
fundido = pd.melt(data, id_vars="Id")
fundido


# In[11]:


# Fundimos a través de 2 variables
fundido2 = pd.melt(data, id_vars=["Id","MSZoning"])
fundido2


# # 4. Pivotado tablas (tablas dinámicas)

# In[13]:


# El fundido es reversible mediante una operación de pivotado.
# En columns, indicamos la columna de fundido que recoge todas las variables de la tabla sin fundir
fundido.pivot(index='Id', columns='variable')['value']


# In[14]:


import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()


# In[49]:


# Extracción de porcentajes de supervivencia en función de la clase
titanic.pivot_table(values = 'survived', columns = 'class')


# In[44]:


# Si quisiéramos obtener no los porcentajes de supervivencia, sino los totales, usaremos una función de agregación
titanic.pivot_table('survived', 'class', aggfunc=np.sum)


# In[53]:


titanic.pivot_table('survived', 'class', aggfunc=np.mean)


# In[48]:


# ¿Y si quisiéramos obtener el porcentaje de supervivencia, segregado por sexo y clase?
titanic.pivot_table(values = 'survived', index =  ['sex', 'alone'], columns = 'class')


# In[15]:


# Complicamos un poco más el ejemplo
titanic.pivot_table(values = 'survived',
                    index = ['sex', 'alone'],
                    columns = ['embark_town', 'class'])


# In[54]:


# Pivotado en base a varias funciones de agregación

# Mostrar el precio medio pagado por el pasaje, en función de su clase y sexo, y además, 
# el total de supervivientes segregados por clase y sexo
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived': np.sum,
                             'fare': np.mean})

