#!/usr/bin/env python
# coding: utf-8

# # Tratamientos de los Outliers

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
pd.set_option('display.max_rows', 500) #comando para mostrar todas las columnas


# In[2]:


# Cargamos los datos
os.chdir(r"./data")
data = pd.read_csv("outliers.csv")


# In[3]:


data.info()


# In[4]:


# Igual que en anteriores ocasiones tenemos que comprender nuestros datos.
data.head()


# In[5]:


data.describe()


# In[6]:


# Comprobamos que no hay valores perdidos.
data.isnull().sum()


# ### Detección por boxplot y z-score

# In[7]:


# El primer paso es realizar un "box-plot" para visualizar si existen outliers y como se distribuyen.

# Podemos analizar variable a variableb
data1=data.iloc[:,0]
plt.boxplot(data1);


# In[8]:


# Tambien podemos realizar un grafico de todas las variables a la vez.
data.plot(kind='box');


# In[9]:


# El analisis grafico nos permite ver que existen outliers en todas las variables incluidas en el modelo.
# Una vez que hemos constatado que existen outliers.
# La primera opcion es eliminar las filas que contienen outliers en alguna de las variables.
import numpy as np
from scipy import stats

dataSinOut = data[(np.abs(stats.zscore(data)) <=3).all(axis=1)]  # nos quedamos con los registros cuyos zscore 
                                                                # menor de 3 veces la desviación estandar de la variable


# In[10]:


dataOut = data[(np.abs(stats.zscore(data)) >3).all(axis=1)]


# In[11]:


dataSinOut.plot(kind='box');


# In[12]:


dataSinOut.shape


# ### Marcación de outliers

# In[13]:


# Lo primero que tenemos que hacer es calcular los estadisticos basicos para la deteccion de outliers (media o mediana y desviacion tipica)
data.describe().transpose()


# In[14]:


# En los pasos anteriores hemos descubierto que la fila 38 presenta unos valores muy anomalos.
# Por ello la vamos a eliminar.
# Una forma de eliminarla es hacerlo manualmente.

data1=data.drop(data.index[38])
data1.head(n=40)


# In[15]:


# Ésto es una opción viable en el caso de que debamos eliminar pocas observaciones.
# Otra opción es seleccionar una de las variables, ver a partir de que valor 
# queremos eliminar la observación y hacerlo a mano.

data2=data[(data["G1"] < 5)]
data2.head(n=40)


# In[16]:


data['Outliers_G1'] = False
data['Outliers_G2'] = False
data['Outliers_G3'] = False
data.loc[(data["G1"] >= 5),'Outliers_G1'] = True
data.loc[(data["G2"] >= 5),'Outliers_G2'] = True
data.loc[(data["G3"] >= 5),'Outliers_G3'] = True


# In[17]:


data


# Otra opción es eliminar aquellas observaciones que sobrepasen una desviación prefijada. Ésto se puede aplicar sobre una de las variables o sobre todo el dataset. Aplicarlo sobre una determinada variable nos exige ser cuidadosos a la hora de fijar el límite para no eliminar demasiadas observaciones.
# 
# 

# In[18]:


# Para ello utilizamos una formula que ya hemos visto con anterioridad modificada.
# Tras ello comprobamos que no hemos eliminado elementos que queriamos mantener y 
# que hemos eliminado la fila 38.

from scipy import stats
data1=data[(np.abs(stats.zscore(data["G1"])) < 6)]

print(data1)
data1.head(n=40)


# In[19]:


data1.shape


# Otra opción en vez de eliminar la observación es transformarlos NAs

# ### Rango Intercuartílico y outliers

# In[20]:


tmp = data
tmp


# In[21]:


# Una forma de ver en cada variable en que observacion se encuentran los outliers.
# Se fundamenta en la diferencia para el percentil 25 y 75.

import numpy as np

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))


datos=data.iloc[:,:-3].apply(outliers_iqr)  # Ojo, no estoy cogiendo las 3columnas en las que guardamos
                                            # los lógicos de outliers. Este valor podría cambiar.
datos


# In[22]:


# Elimino aquellas columnas que empiezan por Outliers
data1= data1.filter(regex='^(?!Outliers)', axis=1)


# In[23]:


# Para ello utilizamos una formula ya utilizada pero modificada, igual que antes.
# Realizamos la comprobacion de antes
# Mostramos la fila que nos interesa (un numero menos ya que se ha eliminado la fila 38)

from scipy import stats
import numpy as np
data1=data1[(np.abs(stats.zscore(data1)) <6).all(axis=1)]

print(data1)


# In[24]:


print(data1.head(n=40))


# In[25]:


print(data1.iloc[151,:])


# ### Sustitución de outliers

# In[32]:


# Mediante esta formula podemos sustituir los outliers por la media.

def replace(group):
    mean, std = group.mean(), group.std()
    outliers = (group - mean).abs() > 3*std
    group[outliers] = mean        
    return group


datos= datos.filter(regex='^(?!Outliers)', axis=1)
datos=datos.apply(replace)

datos.head(n=40)


# In[33]:


# De esta manera podemos convertir los outliers en NAs y luego tratarlos como NAs.
# El trataiento de NAs lo hemos visto previamente.

import numpy as np

def replace2(group):
    mean, std = group.mean(), group.std()
    outliers = (group - mean).abs() > 3*std
    group[outliers] = np.nan        
    return group


datos=datos.apply(replace2)

datos.head(n=10)

