#!/usr/bin/env python
# coding: utf-8

# # Tratamiento de los valores perdidos

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
pd.set_option('display.max_rows', 10) #comando para mostrar todas las columnas


# In[2]:


# Cargamos los datos
os.chdir(r"/home/mydoctor/Documents/03.Trabajos/01.C2B/17.Python avanzado - C2B (15h)/data")
data = pd.read_csv("valores_perdidos.csv")


# In[3]:


# Preliminar de los datos
data.head(n=10)


# In[4]:


# Podemos usar print
print(data)


# In[5]:


# "Resumen estadistico" de cada una de las variables.
data.describe()


# In[6]:


# Comprobamos si existe algún valor perdido. True = Sí existen valores perdidos
data.isnull().any().any()


# In[7]:


# Analizamos su completitud.
# Tenemos que saber cuantos valores perdidos tenemos de cada variable antes de tomar una decision sobre como proceder.
data.isnull().sum()


# ### Borrar aquellas columnas con perdidos a partir de un umbral

# In[8]:


# Otra opcion es calcular el porcentaje que siempre es mas representativo.
filtro = data.isnull().sum()/len(data.index)


# In[9]:


data.shape[1]


# In[10]:


filtro


# In[11]:


# Elimnamos las columnas que tengan mas de un porcentaje de datos perdidos. 
# En este caso nos quedaremos con aquellas columnas con menos de un 10% de perdidos.
filtro = data.isnull().sum() < 0.1 * data.shape[0] 

df1 = data.loc[:, filtro]
df1.head()


# ### Borrar cualquier fila con perdidos

# In[12]:


# Esta es la opcion menos adecuada ya que supone una importante perdida de infomación
# Una vez eliminados los visualizamos los datos
df2=data.dropna()
print(df2)


# In[13]:


# Con esta funcion nos vemos si existen (TRUE) o no (FALSE) datos perdidos
df2.isnull().any().any()


# ## Imputación de valores perdidos por métodos estadísticos
# ### Media

# In[14]:


# El metodo de imputacion mas sencillo es la media 
df3 = data.fillna(data.mean())


# In[15]:


# Pocedemos a comprobar que no existen valores perdidos
df3.isnull().any().any()


# ### Media 2

# In[16]:


# Otra forma de imputar la media es la siguiente
import sklearn.preprocessing as sk


# In[17]:


data.info()


# In[18]:


# Seleccionamos los datos numericos.
datoNum = data.iloc[:,1:]
columnas = datoNum.columns
fecha = data.iloc[:,0]


# In[19]:


# Imputamos la media a los perdidos.
# Importante, tanto fit(), como transform() esperan un array 2D o dataframe.
# Si pasamos un array 1D, nos devolverá un error.
from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, # Generamos instancia para la imputación por la media
                      strategy="mean", 
                      verbose=0, 
                      copy=False) # La imputación se ejecuta "in-place"

imp = imp.fit(datoNum) # Generamos el array con los datos a sustituir
datoNum = imp.transform(datoNum) # Imputamos los valores

# Convertimos el resultado a Dataframe y concatenamos con la columna fecha
datoNum = pd.DataFrame(datoNum, index = list(range(len(datoNum))))
datoNum.columns = columnas
df4 = pd.concat([fecha, datoNum], axis=1)


# In[20]:


df4.head()


# In[21]:


df4.isnull().any().any()


# ### Moda
# Se usa habitualmente para imputar en valores categóricos

# In[22]:


# Seleccionamos los datos numericos.
datoNum = data.iloc[:,1:]
columnas = datoNum.columns
fecha = data.iloc[:,0]


# In[23]:


from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan,
                      strategy="most_frequent", 
                      verbose=0, 
                      copy=False)

imp = imp.fit(datoNum) 
datoNum = imp.transform(datoNum)

datoNum = pd.DataFrame(datoNum, index = list(range(len(datoNum))))
datoNum.columns = columnas
df5 = pd.concat([fecha, datoNum], axis=1)


# In[24]:


df5.head()


# In[25]:


# Nos aseguramos de que no haya valores perdidos.
df5.isnull().any().any()


# ### Mediana

# In[26]:


# Seleccionamos los datos numericos.
datoNum = data.iloc[:,1:]
columnas = datoNum.columns
fecha = data.iloc[:,0]


# In[27]:


from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan,
                      strategy="median", 
                      verbose=0, 
                      copy=False)

imp = imp.fit(datoNum) 
datoNum = imp.transform(datoNum)

datoNum = pd.DataFrame(datoNum, index = list(range(len(datoNum))))
datoNum.columns = columnas
df6 = pd.concat([fecha, datoNum], axis=1)


# In[28]:


df6.head()


# In[29]:


# Nos aseguramos de que no haya valores perdidos.
df6.isnull().any().any()


# ### Valor fijo

# In[30]:


# Seleccionamos los datos numericos.
datoNum = data.iloc[:,1:]
columnas = datoNum.columns
fecha = data.iloc[:,0]

imp = SimpleImputer(missing_values=np.nan,
                    strategy="constant", 
                    verbose=0, 
                    copy=False,
                    fill_value = 0)

imp = imp.fit(datoNum) 
datoNum = imp.transform(datoNum)

datoNum = pd.DataFrame(datoNum, index = list(range(len(datoNum))))
datoNum.columns = columnas
df7 = pd.concat([fecha, datoNum], axis=1)


# In[31]:


df7.isnull().any().any()


# In[32]:


df7.head()


# ### Otros métodos de imputación

# ### Series temporales

# In[33]:


# Al tratarse de una serie temporal se puede sustituir por el valor anterior de dicha serie
# Solo sustituye el valor siguiente, si faltan tres seguidos no lo imputa.

df8=data.fillna(method='bfill')
df8


# In[34]:


data


# In[35]:


df8.isnull().any().any() #Seguimos teniendo NAs


# ### Imputación múltiple

# In[36]:


# Este procedimiento es adecuado cuando las variables explicativas estan relacionadas entre si.
# Previamente obtenemos la matriz de correlacion.  
data.corr()


# In[37]:


# Lo vemos en color...
import seaborn as sns

sns.heatmap(data.corr())


# In[38]:


# Para este caso necesitamos saber el tipo de dato que hay en cada columna.
data.dtypes


# #### Se puede observar que existe cierta correlacion entre las variables dependientes. 
# #### Esto es un indicador de que puede ser adecuado utilizar metodos de imputacion multiple. 
# #### Hasta ahora hemos separado las columnas manualmente ya que estamos trabajando con pocos datos. 
# #### Con grandes bases de datos en los que se entremezclen datos numericos con otro tipo de datos puede generar problemas. 
# #### Por ello podemos separarlos en funcion de su tipologia.
# 

# In[39]:


#pip install fancyimpute


# In[40]:


datoNum = data.select_dtypes(include=[np.float])
fecha = data.select_dtypes(include=[np.object])

datoNum=pd.DataFrame(datoNum)
columnas =datoNum.columns
fecha=pd.DataFrame(fecha)

from fancyimpute import IterativeImputer
mice_imputer = IterativeImputer()  # Llamamos a la clase
datoNum = pd.DataFrame(mice_imputer.fit_transform(datoNum), columns = columnas)
df9 = pd.concat([fecha, datoNum], axis = 1)


# In[41]:


df9.isnull().any().any() 


# In[42]:


sns.pairplot(df9);
# No admite NaNs


# ### Imputación por vecinos cercanos

# In[46]:


# ¡Ojo!, este proceso tarda bastante tiempo.
from sklearn.impute import KNNImputer

datoNum = data.select_dtypes(include=[np.float])
fecha = data.select_dtypes(include=[np.object])

datoNum=pd.DataFrame(datoNum)
columnas =datoNum.columns
fecha=pd.DataFrame(fecha)

# Imputación por 3 vecinos cercanos, dando mayor importancia a los elementos más cercanos.
knn_imputer = KNNImputer(n_neighbors=3, weights='distance') 


knn_imputer.fit(datoNum)
imputado = knn_imputer.transform(datoNum)
pd.DataFrame(imputado, columns = columnas)

