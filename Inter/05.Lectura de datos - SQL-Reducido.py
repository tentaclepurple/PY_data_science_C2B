#!/usr/bin/env python
# coding: utf-8

# # Acceso a AzureSQL

# In[1]:


pip install pyodbc


# In[2]:


import pyodbc
import pandas as pd
import warnings
#warnings.filterwarnings('ignore')
#import sqlalchemy


# ### Prueba descarga tablas

# #### **Descarga tabla completa**

# In[3]:


from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import sqlalchemy as sa


# In[5]:


server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'
port='1433'

connection_string = ('DRIVER='+driver+';SERVER=tcp:'+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = create_engine(connection_url)

with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT * FROM calendario_festivos_2022"), conn)


# ### Método de conexión antiguo

# In[6]:


server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'
port='1433'

db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()
df = pd.read_sql_query('SELECT * FROM calendario_festivos_2022', db)

#cursor.execute("DROP TABLE table_name")


# In[7]:


df


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


type(df.municipalitycode)


# In[11]:


cursor.close()


# #### **Descarga de datos filtrados**

# La sintaxis para extracción de datos vía sql es la siguiente:
# 
# SELECT campos (separados por comas) FROM tabla WHERE condicion

# In[12]:


server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'
port='1433'

connection_string = ('DRIVER='+driver+';SERVER=tcp:'+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = create_engine(connection_url)


# In[13]:


# Extraer de la tabla transacciones, aquellas realizadas en el CP 48004
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT * FROM Transacciones WHERE Codigo_Postal = 48004"), conn)
    #df = pd.read_sql_query(sa.text('SELECT * FROM Transacciones WHERE Tipo_de_Comercio = "es_taxi"'), conn)
df


# In[14]:


# Extraer de la tabla transacciones, aquellas realizadas en el CP>48004 y CP< 48010
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text('SELECT * FROM Transacciones WHERE Codigo_Postal >= 48004 AND Codigo_Postal <= 48010'), conn)
df


# In[15]:


# Extraer de la tabla transacciones la columna Tipo de Comercio y Transacciones, para transacciones aquellas realizadas en el CP>48004 y CP< 48010
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text('SELECT Tipo_de_Comercio, Transacciones FROM Transacciones WHERE Codigo_Postal >= 48004 AND Codigo_Postal <= 48010'), conn)
df


# In[16]:


# Otra manera
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text('SELECT Tipo_de_Comercio, Transacciones FROM Transacciones WHERE Codigo_Postal BETWEEN 48004 AND 48010'), conn)
df


# **Lógica booleana y operadores en SQL**
# 
# Algunos de los operadores que nos permiten construir expresiones booleanas son:
# 
#     > : "A > B" devuelve cierto si A es estrictamente mayor que B, de lo contrario devuelve falso.
#     < : "A < B" devuelve cierto si A es estrictamente menor que B, de lo contrario devuelve falso.
#     = : "A = B" devuelve cierto si A es igual a B, de lo contrario devuelve falso.
#     >= : "A >= B" devuelve cierto si A es mayor o igual a B, de lo contrario devuelve falso.
#     <= : "A <= B" devuelve cierto si A es menor o igual a B, de lo contrario devuelve falso.
#     != : "A != B" devuelve cierto si A es distinto a B, de lo contrario devuelve falso.
#     
#     AND : "A and B" devuelve cierto si A y B valen cierto, y falso en cualquier otro caso.
#     OR : "A or B" devuelve cierto si A o B valen cierto, y falso únicamente cuando tanto A como B valen falso.
#     NOT : "not A" devuelve falso si A vale cierto, y cierto si A vale falso.

# In[17]:


with engine.begin() as conn:
    df = pd.read_sql_query(sa.text('SELECT * FROM Transacciones WHERE (Transacciones = 8)'), conn)
df


# #### **Agregados**

# In[18]:


# Total transacciones
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text('SELECT SUM(Transacciones) FROM Transacciones'), conn)
df


# In[19]:


# Total registros en tabla
with engine.begin() as conn:
    display(pd.read_sql_query(sa.text('SELECT count(*) FROM Transacciones'), conn))


# In[20]:


# Medias
with engine.begin() as conn:
    display(pd.read_sql_query(sa.text('SELECT avg(Transacciones) FROM Transacciones'), conn))


# #### **Agrupaciones**

# In[21]:


#Construyo una función para hacer las consultas
def leerSQL(x):
    with engine.begin() as conn:
        return(pd.read_sql_query(sa.text(x), conn))


# In[22]:


# Transacciones totales por tipo de comercio
leerSQL('SELECT Tipo_de_Comercio, count(*) AS Total FROM Transacciones GROUP BY Tipo_de_Comercio')


# In[23]:


# Elementos únicos en una columna
leerSQL('SELECT Tipo_de_Comercio FROM Transacciones GROUP BY Tipo_de_Comercio')


# #### **Ordenar los datos**

# In[24]:


leerSQL('SELECT * FROM Transacciones ORDER BY Transacciones DESC')


# In[25]:


# Ordenar por varios campos
leerSQL('SELECT * FROM Transacciones ORDER BY Codigo_Postal, Transacciones DESC')


# #### **Operador LIKE**

# In[26]:


# A través de este operador podemos hacer búsquedas que cumplan un determinado criterio.  
# En este caso registros que contengan 'sme' en tipo de comercio

leerSQL("SELECT Fecha, Codigo_Postal, Tipo_de_Comercio                   FROM Transacciones WHERE Tipo_de_Comercio LIKE '%sme%' ")


# In[27]:


# Y la consulta opuesta
leerSQL("SELECT Fecha, Codigo_Postal, Tipo_de_Comercio FROM Transacciones                   WHERE Tipo_de_Comercio NOT LIKE 'es_hospital' ")


# In[28]:


leerSQL("SELECT Fecha, Codigo_Postal, Tipo_de_Comercio FROM Transacciones                   WHERE Tipo_de_Comercio NOT LIKE '%sme%'")


# #### **Extracción de datos NO nulos**

# In[29]:


leerSQL("SELECT * FROM Transacciones WHERE Tipo_de_Comercio IS NOT NULL ")


# #### **Unión de tablas**

# In[30]:


# Inner
leerSQL("SELECT * FROM TablaA C INNER JOIN TablaB P ON C.Id = P.Id")


# In[31]:


# Left
leerSQL("SELECT * FROM TablaA C LEFT JOIN TablaB P ON C.Id = P.Id")


# In[32]:


#Right
leerSQL("SELECT * FROM TablaA C RIGHT JOIN TablaB P ON C.Nombre = P.Nombre")


# In[33]:


#Outer
leerSQL("SELECT * FROM TablaA C FULL OUTER JOIN TablaB P ON C.Nombre = P.Nombre")


# ### Operaciones CRUD

# In[34]:


datos = leerSQL("SELECT * FROM Personas")


# In[35]:


datos


# #### **Inserción de datos en Azure a través de to_sql**

# In[36]:


# El proceso varía ligeramente de lo visto en el paso previo
from urllib.parse import quote_plus
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, event
import pyodbc

# cadena de conexión a azure sql
server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'

# crear la conexión
conn ='Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlc2bcurso.database.windows.net,1433;Database=CusoC2B;Uid=administrador;Pwd=Campus.5678@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
quoted = quote_plus(conn)
engine=create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

# carga de datos en la bbdd
datos.to_sql('prueba', engine, index=False, if_exists='append')


# In[37]:


datos


# #### **Inserción de datos en azure.  ¡Ojo! Es necesario que la tabla ya exista en la BBDD.**
# 

# In[38]:


server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'

db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()


# In[39]:


# Este proceso hace un append sobre la tabla Prueba

for index, row in datos.iterrows():
     cursor.execute("INSERT INTO Prueba (Id,Nombre,Ciudad) values(?,?,?)", row.Id, row.Nombre, row.Ciudad)
db.commit()


# In[40]:


leerSQL("SELECT * FROM Prueba")


# #### **Crear tablas**

# In[41]:


#Cerramos el cursor previo
db.close()


# In[42]:


# Supongamos que queremos crear una tabla, llamada Productos, con los siguientes campos:

# Variable      Tipo variable
# ----------------------------------
# idProducto    int (clave primaria)
# producto      nvarchar(50)
# precio        int

# Para generar la nueva tabla...


# In[43]:


server = 'sqlc2bcurso.database.windows.net'
database = 'CusoC2B'
username = 'administrador'
password = 'Campus.5678@'   
driver= '{ODBC Driver 18 for SQL Server}'

db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()


# In[44]:


# Generación de la tabla
cursor.execute('CREATE TABLE Productos (               idProducto int primary key,                producto nvarchar(50),                precio int)'
              )
db.commit()


# In[ ]:


db.close()

