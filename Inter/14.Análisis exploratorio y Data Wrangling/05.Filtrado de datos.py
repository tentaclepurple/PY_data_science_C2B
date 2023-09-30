#!/usr/bin/env python
# coding: utf-8

# # Filtrado de datos

# In[15]:


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


# In[2]:


# Cargamos los datos
os.chdir(r"/home/mydoctor/Documents/03.Trabajos/01.C2B/17.Python avanzado - C2B (15h)/data")
data = pd.read_csv("SalePrice.csv")


# In[3]:


data.head()


# # 1. Eliminar duplicados

# In[8]:


# La primera opcion de filtrado es ELIMINAR DUPLICADOS.
# Seleccionamos dos columnas.  Nos aseguramos así de tener registros duplicados.b
DatosElim=data.iloc[:,7:9]
DatosElim.shape


# In[9]:


# Eliminamos duplicados
DatosDrop=DatosElim.drop_duplicates()
DatosDrop.shape


# # 2. Intersección (de columnas)

# Es equivalente a un **inner** pero a nivel de columnas.

# In[24]:


# Consiste en filtrar los elementos de una tabla, en función de otra.
SalePriceImportantes=data.iloc[0:100,0:15]
SalePriceImportantes


# In[25]:


data.shape, SalePriceImportantes.shape


# In[27]:


# Nos quedamos con todos los registros de data, pero sólo aquellas columnas comunes a ambos.
filtro = data.columns.intersection(SalePriceImportantes.columns)
SalePrice2=data[filtro]
print(SalePrice2)
print(SalePrice2.shape)


# # 3. Diferencia

# In[31]:


filtro = data.columns.difference(SalePriceImportantes.columns)
SalePrice3=data[filtro]
data.shape, SalePriceImportantes.shape, SalePrice2.shape, SalePrice3.shape


# # 4. Is in

# In[34]:


# En este caso, el filtrado implica las filas comunes.
SalePrice4=data[data.index.isin(SalePriceImportantes.index)]
data.shape, SalePriceImportantes.shape, SalePrice4.shape


# # 5. Not in

# In[37]:


SalePrice5=data[~data.index.isin(SalePriceImportantes.index)]
SalePrice5a=data[data.index.isin(SalePriceImportantes.index)==False]
data.shape, SalePriceImportantes.shape, SalePrice4.shape, SalePrice5.shape, SalePrice5a.shape


# # 6. Filtrado por una variable

# In[46]:


# Construimos la variable a usar como filtro

DatosDrop2=DatosDrop.iloc[:,0:1]
# Nos quedamos solo con los valores unicos
DatosDrop2=DatosDrop2.drop_duplicates()
# Eliminamos la última observación
DatosDrop2=DatosDrop2.iloc[:-1]
DatosDrop2


# Seleccionamos de la tabla 1 aquellos valores que **aparezcan** en la tabla 2.

# In[59]:


DatosElim['LotShape'].value_counts()


# In[57]:


DatosDrop2['LotShape'].value_counts()


# In[58]:


resultado=DatosElim[DatosElim["LotShape"].isin(DatosDrop2["LotShape"])]
resultado


# Seleccionamos de la tabla 1 aquellos valores **que NO** aparezcan en la tabla 2

# In[ ]:


resultadoNI=DatosElim[~DatosElim["LotShape"].isin(DatosDrop2["LotShape"])]
resultadoNI2=DatosElim[DatosElim["LotShape"].isin(DatosDrop2["LotShape"])==False]


# # 7. Filtrado a través de variables

# In[63]:


AreaGrande=data[(data["LotArea"]>10000)]
CallePabe=data[(data["LotConfig"]=="Corner")]


# In[61]:


AreaGrande


# In[64]:


CallePabe

