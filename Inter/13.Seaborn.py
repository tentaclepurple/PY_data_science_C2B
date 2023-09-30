#!/usr/bin/env python
# coding: utf-8

# # Seaborn

# Seaborn complementa a Mathplotlib, con una filosofía de hacer fácil lo menos fácil.  Incluye temas personalizados que nos permiten controlar la forma como se dibujan los gráficos.
# 
# En este sentido soluciona 2 problemas existentes en Matplotlib:
# 
# * Parámetros por defecto.
# * Trabajar con DataFrames.
# 

# In[1]:


# pip install seaborn
# conda install seaborn


# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math
from pylab import *
import warnings
warnings.filterwarnings('ignore')


# ### Definiendo la estética de mathplotlib

# Generamos un set de datos.  Básicamente una función senoidal que pintaremos con mathplotlib y modificaremos su estética con seaborn

# In[20]:


sns.reset_defaults()


# In[6]:


x=np.arange(0, math.pi*2, 0.05) # Rango de datos para pintar el eje X
y=np.sin(x)
plt.plot(x,y)
plt.show()


# In[8]:


x=np.arange(0, math.pi*2, 0.05) # Rango de datos para pintar el eje X
y=np.sin(x)

sns.set()
plt.plot(x,y)
plt.show()


# Definiendo el fondo y otros elementos estéticos a través de set_style():
# * Darkgrid
# * Whitegrid
# * Dark
# * White
# * Ticks

# In[9]:


sns.set_style('whitegrid')
plt.plot(x,y)
plt.show()


# #### Eliminar la cuadrídula

# In[13]:


sns.set_style('white')
sns.despine() # Si colocamos despine bajo plot, el resultado es distinto
plt.plot(x,y)
plt.show()


# Podemos definir los parámetros de configuración de los gráficos a través de un diccionario.

# In[14]:


# Parámetros por defecto
print (sns.axes_style())


# Podríamos modificar cualquiera de los parámetros definidos por defecto...

# In[28]:


# Añadimos fondo gris, y traemos la cuadrícula sobre el gráfico y eliminamos el marco de la imagen (despine())
sns.set_style('darkgrid', {'axes.axisbelow':False})
sns.despine()
plt.plot(x,y)
plt.show()


# ### Escalado rápido de las gráficas
# 
# A través de set_context() podemos definir 4 niveles de escalado.
# * paper
# * notebook: Opción por defecto
# * talk
# * poster

# In[10]:


sns.set_style('darkgrid', {'axes.axisbelow':False})
sns.set_context('poster')
sns.despine()
plt.plot(x,y)
plt.show()


# ### Trabajando con colores
# 
# Parámetros:
# * n_colors: Nº de colores de la paleta.  Por defecto = 6
# * desat: % de desaturación para cada color.

# Por defecto, tenemos 6 paletas:
# 
# * deep
# * muted
# * brigth
# * pastel
# * dark
# * colorblind
# 
# Pero podemos crear nuestras propias paletas

# In[29]:


sns.color_palette(palette=['red', 'blue', 'green'], n_colors=3, desat= 1)


# In[31]:


sns.color_palette(palette=['red', 'blue', 'green'], n_colors=3, desat= 0.5)


# In[32]:


paleta1 = sns.color_palette(palette=['red', 'blue', 'green'], n_colors=3, desat= 0.25)


# In[36]:


# Usamos la nueva paleta.
sns.set(context='notebook', style='darkgrid', palette=paleta1, font='sans-serif', font_scale=1, color_codes=False, rc=None)
plt.plot(x,y)
plt.show()


# In[37]:


# Usamos una paleta por defecto.
sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plt.plot(x,y)
plt.show()


# Si usamos despine() junto con set_style("white"), sólo se mostrarán 2 de los 4 marcos de la imagen (frente a ninguno si los usamos con otro set_style)

# In[38]:


sns.set_style("white")
plt.plot(x,y)
sns.despine()
plt.show()


# Podemos usar 3 tipos diferentes de paletas:
# * qualitative.  Colores categóricos (rojo, verde, azul, ...
# * sequential. Secuencia de diferentes tonalidades de un color
# * diverging. Colores divergentes
# 
# Definiremos la paleta a usar con **palplot()**

# In[49]:


# qualitative.  1 paleta. tab10.  Si no se indica otra, es la que toma por defecto
paleta = sns.color_palette('tab10',10)
sns.palplot(paleta)
plt.show()


# In[42]:


# sequential
# disponemos de 4 paletas secuenciales por defecto: rocket, mako, flare, crest
paleta = sns.color_palette('rocket',20)
sns.palplot(paleta)
plt.show()


# In[45]:


# divergent.
# Se basa en representar 2 colores
paleta = sns.color_palette("BrBG", 7) # Paleta con 7 colores empezando por el marrón (br) y terminando en el verde oscuro (BG)
sns.palplot(paleta)
plt.show()


# Como hemos visto antes, a través de **set_style()** definimos las opciones por defecto, incluida la paleta a usar.

# ## Gráficando...

# ### Histograma

# In[47]:


# Usaremos el dataset iris.
df = sns.load_dataset('iris')


# In[48]:


df.head()


# In[51]:


sns.reset_defaults() # volvemos a la configuración por defecto.
sns.distplot(df['petal_length'],kde=False)
sns.despine()
plt.show()


# In[65]:


# Podemos aumentar la definición de la imagen a través de los bins y mostrar KDE (método no paramétrico 
# que permite estimar la funcion de densidad de probabilidad de una variable aleatoria a partir de un número finito de observaciones
sns.distplot(df['petal_length'],bins = 100)
sns.despine()
plt.show()


# ### Scatter plot

# In[77]:


df.head()


# In[54]:


sns.jointplot(x='petal_length',y='petal_width', hue='species', data=df)
plt.show()


# ### Hexbin plot

# A usar en análisis bivariante, cuando la densidad de los datos sea baja (datos dispersos)

# In[85]:


sns.jointplot(x='petal_length',y='petal_width', data=df, kind='hex')
plt.show()


# ### Estimación de la distribución de una variables (KDE)

# In[134]:


g = sns.jointplot(data=df, x='petal_length',y='petal_width', kind='kde', hue='species', legend=False)
plt.show()


# ### Boxplot

# In[137]:


sns.boxplot(x="species", y="petal_length", data=df)
plt.show()


# ### Violin plot

# In[55]:


# Usaremos el dataset de propinas
df2 = sns.load_dataset('tips')


# In[57]:


df2.head()


# In[150]:


sns.violinplot(x = "day", y = "tip", data=df2)
plt.show()


# In[59]:


sns.violinplot(x = "day", y = "tip", hue="sex", data=df2)
plt.show()


# ### Mapas de calor

# In[61]:


#Nos permite ver de manera rápida los datos.  Sólo funciona con valores numéricos.
df3 = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
df3.head()


# In[63]:


sns.heatmap(df3, annot=True, cbar=False)
plt.show()


# ### Correlogramas

# In[65]:


sns.pairplot(df,hue='species')
plt.show()


# ### Gráficos de burbujas

# In[66]:


df2.head()


# In[177]:


sns.scatterplot(data=df2, y='total_bill', x='tip', size='time', hue='time')
plt.show()


# ### Treemap

# In[69]:


#pip install squarify
import squarify


# In[67]:


df4 = df2[['total_bill', 'tip', 'sex']]
df4.head()


# In[71]:


df4.sort_values('total_bill', ascending=False, inplace=True)


# In[72]:


squarify.plot(sizes=df4.total_bill, label=df4.sex)
plt.axis('off')
plt.show()


# ### Dendogramas

# In[233]:


df


# In[229]:


from scipy.cluster.hierarchy import dendrogram, linkage
Z = linkage(df.iloc[:,:-1], 'ward')
Z


# In[235]:


dendrogram(Z, labels=df.index, leaf_rotation=90)
plt.show()


# ### Donuts

# In[73]:


# Contruimos los agregados, en este caso el total de elementos por clase en Iris
totales = df.groupby('species')['species'].count()
totales


# In[79]:


etiquetas = totales
plt.pie(totales, labels=etiquetas)
circulo_central = plt.Circle((0,0), 0.7, color='white')

p=plt.gcf()
p.gca().add_artist(circulo_central)
plt.legend(labels=totales.index, loc='upper left')
plt.show()


# ### Más gráficos en python
# https://www.python-graph-gallery.com/
