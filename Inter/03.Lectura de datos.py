#!/usr/bin/env python
# coding: utf-8

# # Parte 1: Lectura de datos con diferentes formatos

# In[1]:


get_ipython().run_line_magic('reset', '-f')


# In[6]:


#pip install et-xmlfile


# In[1]:


import pandas as pd
import numpy as np
import os
from datetime import datetime
# Librería para tratamiento de ficheros xml
import xml.etree.ElementTree as ET
# Librería para efectuar peticiones a páginas web
import requests


# Vamos a generar las funciones necesarias para cargar los datos en los diferentes formatos

# https://pandas.pydata.org/docs/search.html?q=read_

# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# 
# https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
# 
# https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html
# 
# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html

# In[2]:


# carga de archivos xml

def cargaXml():
    inicio = datetime.now()
    xml_data = open('./data/calendario_laboral_2022.xml', 'r', encoding="UTF-8").read()  # Leer archivo
    root = ET.XML(xml_data)  # Parsear el XML
    data = []
    cols = []
    for i, child in enumerate(root):
        data.append([subchild.text for subchild in child])
        cols.append(child.tag)

    df = pd.DataFrame(data).T  # Escribir en DF y transponer datos
    df.columns = cols  # Actualizamos nombres de columna Update column names
    
    return ((datetime.now()-inicio).total_seconds())


# In[3]:


# carga de archivos xlsx
def cargaXlsx ():
    inicio = datetime.now()
    xlsx_data = pd.read_excel('./data/calendario_laboral_2022.xlsx', sheet_name='calendario_laboral_2022')
    return ((datetime.now()-inicio).total_seconds())


# In[4]:


# carga de archivos csv
def cargaCsv ():
    inicio = datetime.now()
    csv_data = pd.read_csv('./data/calendario_laboral_2022.csv', sep=';', encoding = "latin-1")
    return ((datetime.now()-inicio).total_seconds())


# In[5]:


# carga de archivos json
def cargaJson ():
    inicio = datetime.now()
    json_data = pd.read_json('./data/calendario_laboral_2022.json')
    return ((datetime.now()-inicio).total_seconds())


# In[6]:


cargaXml()


# In[7]:


cargaXlsx()


# In[8]:


cargaCsv()


# In[9]:


cargaJson()


# Vemos que la carga de datos más rápida es a través de CSV's.  También podemos cargar archivos directamente de internet...

# In[10]:


# carga de archivos csv internet
def cargaCsvInternet ():
    inicio = datetime.now()
    csv_data = pd.read_csv('https://opendata.euskadi.eus/contenidos/ds_eventos/calendario_laboral_2022/opendata/calendario_laboral_2022.csv', sep=';', encoding="latin-1")
    return ((datetime.now()-inicio).total_seconds())


# In[11]:


cargaCsvInternet()


# Lo ponemos bonito y automatizamos... Ejecutaremos el proceso 5 veces para tener un tiempo medio de carga por tipo de archivo

# In[27]:


resultados


# In[33]:


tiempos = pd.DataFrame([xml, xlsx, csv, json, csvInternet])
tiempos


# In[29]:


print ('Iteración:', a)
xml = cargaXml()
xlsx = cargaXlsx()
csv = cargaCsv()
json = cargaJson()
csvInternet = cargaCsvInternet()


# In[43]:


resultados = pd.DataFrame(columns=['xml','xlsx','csv','json','csvInternet'])
tiempos = np.array([])
for a in range(5):
    print ('Iteración:', a)
    xml = cargaXml()
    xlsx = cargaXlsx()
    csv = cargaCsv()
    json = cargaJson()
    csvInternet = cargaCsvInternet()
    
    tiempos = pd.DataFrame([xml, xlsx, csv, json, csvInternet]).transpose()
    tiempos.columns = ['xml','xlsx','csv','json','csvInternet']
   
    resultados = pd.concat([resultados, tiempos], ignore_index=True, axis=0)


# In[44]:


resultados


# Calculamos los tiempos medios para cada tipo de archivo

# In[45]:


tiemposMedios = pd.DataFrame(columns=['xml','xlsx','csv','json','csvInternet'])

tiemposMedios.loc ['0','xml'] = round(resultados ['xml'].mean(),3)
tiemposMedios.loc ['0','xlsx'] = round(resultados ['xlsx'].mean(),3)
tiemposMedios.loc ['0','csv'] = round(resultados ['csv'].mean(),3)
tiemposMedios.loc ['0','json'] = round(resultados ['json'].mean(),3)
tiemposMedios.loc ['0','csvInternet'] = round(resultados ['csvInternet'].mean(),3)


# In[46]:


tiemposMedios


# También podemos cargar tablas desde una url en internet...

# In[47]:


url = 'http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1] # Nos quedamos con la ultima tabla descargada

df.to_csv('tabla descargada de internet.csv')
df


# Concatenación de tablas (iguales) descargadas desde internet...

# In[48]:


urls = ["https://resultados.as.com/resultados/futbol/primera/2019_2020/",
        "https://resultados.as.com/resultados/futbol/primera/2020_2021/",
        "https://resultados.as.com/resultados/futbol/primera/2021_2022/"]


# In[49]:


tablas = []
for a in range(len(urls)):
    print(a)
    html = requests.get(urls[a]).content
    df_list = pd.read_html(html)
    tablas.append(df_list[-1]) # Nos quedamos con la ultima tabla descargada


# In[50]:


type (tablas)


# In[51]:


tablas


# In[52]:


tablas[0]

