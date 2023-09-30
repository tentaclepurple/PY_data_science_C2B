#!/usr/bin/env python
# coding: utf-8

# # Análisis exploratorio inicial de los datos

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

pd.options.display.float_format = '{:.2f}'.format #Desactivar notación científica en pandas:
np.set_printoptions(suppress=True) #Desactivar notación científica en numpy:
pd.set_option('display.max_columns', None) #comando para mostrar todas las columnas


# In[2]:


get_ipython().system('pip install -U pandas-profiling[notebook]')
#jupyter nbextension enable --py widgetsnbextension    

#Instalación vía Conda -> desde terminal
#conda env create -n pandas-profiling
#conda activate pandas-profiling
#conda install -c conda-forge pandas-profiling

#Instalación manual
#pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip --user


# In[3]:


#Cargamos la función
from pandas_profiling import ProfileReport
import ydata_profiling as pp
#import pandas_profiling.ProfileReport


# In[4]:


df = pd.read_csv('./data/clima.csv', sep=";", decimal=",")


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


profile = pp.ProfileReport(df, title='wsb')


# In[8]:


profile.to_file("pandas-profiling.html")


# # Sweetviz

# In[9]:


pip install sweetviz


# In[10]:


import sweetviz as sv


# In[11]:


# Carga del set de datos
eda = sv.analyze(df)


# In[12]:


# Mostrar el informe
eda.show_html('Clima.html')


# ### Hemos generado un informe exploratorio inicial, con sólo 3 líneas de código. También podemos usar sweetviz para **comparar conjuntos** de datos de entrenamiento y test

# In[13]:


from sklearn.model_selection import train_test_split

training_data, testing_data = train_test_split(df, test_size=0.3, random_state=123)


# ### Ya tenemos los datos divididos en Train y Test, comparamos ambos conjuntos...

# In[14]:


df2 = sv.compare(training_data, testing_data)
df2.show_html('Comparación train y test.html')


# ### La compararción puede hacerse entre elementos de un mismo conjunto de datos.

# In[15]:


df3 = pd.read_csv('./data/Titanic.csv', sep=";")


# In[16]:


df3.head()


# In[17]:


# Comparamos los datos en base a la columna Sex
titanic_sex = sv.compare_intra(df3, df3["Sex"] == "male", ["Male", "Female"])


# In[18]:


titanic_sex.show_html('Comparación sexos titanic.html')


# ### EDA tomando como base una variable.  En este caso haremos un EDA respecto de la variables Survived.

# In[19]:


titanic_survived = sv.analyze(df3, target_feat='Survived')
titanic_survived.show_html('Titanic-survived.html')


# In[20]:


titanic_survived = sv.analyze(df3)
titanic_survived.show_html('Titanic-survived2.html')


# In[21]:


titanic_survived.show_notebook(layout='vertical')


# ### En determinados casos, podría interesarnos NO comparar alguna dimensión. Vamos a ejecutar el EDA sin tener en cuenta la variable Ticket y PassengerId.  Ademas forzaremos el análisis considerando que Cabin y Survived son categóricas.

# In[22]:


df3.columns


# In[23]:


sweet_config = sv.FeatureConfig(skip=['PassengerId','Ticket'], force_cat=['Cabin','Survived'])


# In[24]:


titanic_sex2 = sv.compare_intra(df3, df3["Sex"] == "male", ["Male", "Female"], None, sweet_config)
titanic_sex2.show_html('Comparación sexos titanic 2.html')


# # Autoviz

# In[25]:


#pip install autoviz


# In[26]:


#https://github.com/AutoViML/AutoViz


# In[27]:


from autoviz.AutoViz_Class import AutoViz_Class

# Creamos el objeto
av = AutoViz_Class()


# In[28]:


# Parámetros posibles
filename = './data/Titanic.csv'
sep = ";"


resultado = av.AutoViz(filename, sep,
                      verbose=0, #valores posibles [0,1,2]
                      chart_format = 'bokeh' # valores posibles [svg, jpg, png, bokeh, html] -> bokeh permite interactuar con los gráficos
                      )


# ### Definición de una variable objetivo...

# In[29]:


resultado = av.AutoViz(filename, sep,
                      verbose=0, #valores posibles [0,1,2]
                      chart_format = 'html', # valores posibles [svg, jpg, png, bokeh, html] -> bokeh permite interactuar con los gráficos
                      depVar = 'Sex' 
                      )


# ### Podemos cargar directamente un dataframe...

# In[30]:


filename = ''

resultado = av.AutoViz(filename, sep,
                      verbose=0, #valores posibles [0,1,2]
                      chart_format = 'html', # valores posibles [svg, jpg, png, bokeh, html] -> bokeh permite interactuar con los gráficos
                      depVar = 'Sex',
                      dfte = df3
                      )


# In[31]:


resultado


# # D-Tale

# ### Es una de las librerías EDA más completas

# In[32]:


#pip install dtale
# Instalación desde conda
# conda config --add channels conda-forge
# conda install dtale

# https://github.com/man-group/dtale


# In[33]:


pip install dtale


# In[34]:


import dtale


# In[35]:


# Creamos el EDA
d = dtale.show(df)

# Mostramos el resultado en un navegador
d.open_browser()


# In[36]:


d = dtale.show(df3)

# Mostramos el resultado en un navegador
d.open_browser()

