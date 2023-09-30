#!/usr/bin/env python
# coding: utf-8

# # CONEXIONES A BASES DE DATOS

# # 1.Acceso y consumo de datos en MongoDB

# In[1]:


get_ipython().system('pip install pymongo')
get_ipython().system('pip install pymongo[srv]')


# In[2]:


# Información extendida sobre PyMongo
# https://pymongo.readthedocs.io/en/stable/index.html


# In[1]:


from pymongo import MongoClient


# In[2]:


# Conexión con la base de datos.
client = MongoClient('mongodb+srv://bootcamp:GkVGYsyqN45Wtz0o@cluster0.byk0e.mongodb.net/?retryWrites=true&w=majority')


# ### Consultas a los datos

# In[3]:


# Bases de datos existentes en mongo
client.list_database_names()


# In[4]:


# Colecciones existentes en BBDD1
colecciones = client.bbdd1.list_collection_names()
colecciones


# In[5]:


# Consultamos la BBDD importada
output = list(client.bbdd1.people.find({}))
print("Total documentos: ", len(output))
print(output)
print('\n')
print(output[0])


# In[6]:


import pandas as pd
import json


# In[7]:


pd.json_normalize(output[0])


# In[8]:


pd.json_normalize(output)


# In[10]:


pd.json_normalize(output).explode('hobbies')


# In[10]:


# Listar aquella gente con 34 años
list(client.bbdd1.people.find({'age' : 34}))


# In[9]:


# Listar aquella gente con más de 34 años (>=)
filtro = {'age' : {'$gte': 34}}
list(client.bbdd1.people.find(filtro))


# In[12]:


# Listar aquella gente con entre 34 y 43 años (>= y <=)
filtro = {'age' : {'$in': [34, 43]}}
list(client.bbdd1.people.find(filtro))


# In[15]:


# Listar aquella gente de 34 ó 43 años
filtro = {'$or': [{'age' : 34},{'age' : 43}]}
list(client.bbdd1.people.find(filtro))


# In[17]:


# Listar aquellos usuarios que cumplan las 2 condiciones
filtro = {'$and' : [{'age' : 34},{'isActive': True}]}
list(client.bbdd1.people.find(filtro))


# In[18]:


# Listar aquellos usuarios cuyo campo hobbies no sea nulo
filtro = {'hobbies' : {'$exists': True}}
list(client.bbdd1.people.find(filtro))


# In[20]:


# Localizar los usuarios cuyo nombre empiece por s
filtro = {'name' : {'$regex' : 's.*'}}
list(client.bbdd1.people.find(filtro))


# In[22]:


# Listar los usuarios cuyo hobbie sea padel O surf
filtro = {'$or': [{'hobbies':'padel'},{'hobbies':'surf'}]}
list(client.bbdd1.people.find(filtro))


# In[23]:


# Listar los usuarios cuyo hobbie sea padel O surf, ordenados por edad de manera descendente
filtro = {'$or': [{'hobbies':'padel'},{'hobbies':'surf'}]}
list(client.bbdd1.people.find(filtro).sort('age', -1))


# In[25]:


# Listar los usuarios cuyo hobbie sea padel Y surf
filtro = {'hobbies':['padel','surf']}
list(client.bbdd1.people.find(filtro))


# In[26]:


# Listar los documentos, donde aparezcan todos los elementos especificados en la búsqueda
# Ojo, pq este filtro devuelve distintos resultados al anterior
filtro = {'hobbies': {'$all': ['padel','surf']}}
list(client.bbdd1.people.find(filtro))


# ### Inserciones

# In[31]:


# Insertar un nuevo documento, cuyo nombre sea pedro y su edad 52
documento = {'name': 'pedro', 'age':52}
client.bbdd1.people.insert_one(documento)
list(client.bbdd1.people.find({'name':'pedro'}))


# In[32]:


# Insertar varios documentos.  
documentos = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

client.bbdd1.people.insert_many(documentos)
list(client.bbdd1.people.find())


# ### Eliminación documento/s

# In[33]:


# Eliminamos los documentos añadidos en los pasos anteriores
# Eliminar un documento
client.bbdd1.people.delete_one(documento)
list(client.bbdd1.people.find())


# In[34]:


# Eliminar varios documentos.
# Eliminar aquellos documentos con un _id < 4 (filtrado de datos)
filtro = {'_id': {'$lt': 4}}
client.bbdd1.people.delete_many(filtro)
list(client.bbdd1.people.find())


# In[35]:


# Eliminar varios documentos de una vez (filtrado de datos)
# Eliminaremos todos aquellos documentos que 
filtro = {'address': {'$exists': True}}
client.bbdd1.people.delete_many(filtro)
list(client.bbdd1.people.find())


# # 2.SQLite

# In[9]:


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect

engine = create_engine('sqlite://', echo=False)


# In[10]:


engine


# In[11]:


# Creamos un dataset, para añadir a la BBDD puesto que está vacía
df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
df


# In[12]:


# Insertamos la tabla recién creada en la BBDD.  Hay que tener en cuenta que la BBDD está vacía.
df.to_sql('users', con=engine)

# Consultamos la inserción
engine.execute("SELECT * FROM users").fetchall()


# In[13]:


df1 = pd.DataFrame({'name' : ['User 4', 'User 5']})
df1.to_sql('users', con=engine, if_exists='append') # Las opciones disponibles son fail, append, replace
engine.execute("SELECT * FROM users").fetchall()

#fail: Si la tabla no existe, devuelve ValueError
#replace: Borra la tabla existente y crea una nueva con los nuevos datos
#append: Añade nuevos elementos a la tabla existente


# In[14]:


df2 = pd.DataFrame({'name' : ['User 6', 'User 7']})
df2.to_sql('users', con=engine, if_exists='append')
engine.execute("SELECT * FROM users").fetchall()


# In[35]:


# Visualizar los nombres de las tablas que contiene la base de datos
nombre_tabla = inspect(engine).get_table_names()
print(nombre_tabla)


# ## Using Raw SQL

# In[18]:


# Realizamos consulta
rs = engine.execute("SELECT * FROM users")


# In[11]:


# Carga directa en dataframe desde la BBDD
df = pd.DataFrame(rs.fetchall())
print(df.head())


# In[12]:


# Create 
engine.execute("CREATE TABLE IF NOT EXISTS Clientes (id text, nombre text, apellidos text,edad text, email text)")  
engine.execute("INSERT INTO Clientes (id, nombre, apellidos, edad, email) VALUES ('1','Ramón', 'García Hernandez','44', 'ragahe@yahoo.es')")
engine.execute("INSERT INTO Clientes (id, nombre, apellidos, edad, email) VALUES ('2','María Jose', 'Fernandez Chaparro','57', 'majofe@hotmail.com')")
engine.execute("INSERT INTO Clientes (id, nombre, apellidos, edad, email) VALUES ('3','Pedro', 'Pombo Villanuva','20', 'pepovi@gmail.es')")
engine.execute("INSERT INTO Clientes (id, nombre, apellidos, edad, email) VALUES ('4','Isabel', 'Segura Oliveras','36', 'isseol@yahoo.es')")
#con.close()


# In[13]:


# Read
results = engine.execute("SELECT * FROM Clientes")  
for r in results:  
    print(r)


# In[14]:


# Update
engine.execute("UPDATE Clientes SET nombre='María' WHERE id='3'")
results = engine.execute("SELECT * FROM Clientes")  
for r in results:  
    print(r)


# In[15]:


# Delete
engine.execute("DELETE FROM Clientes WHERE id='3'")  
results = engine.execute("SELECT * FROM Clientes")  
for r in results:  
    print(r)


# ## Using SQL Expression Language

# In[19]:


from sqlalchemy import Table, Column, String, MetaData, Integer


# In[20]:


meta = MetaData(engine)


# In[21]:


clientes_table =  Table('Clientes2', meta,
                            Column('id',String),
                            Column('nombre',String),
                            Column('apellidos',String),
                            Column('edad',Integer),
                            Column('email',String))


# In[22]:


clientes_table # El dato todavía no está en la BBDD sólo en local


# In[27]:


meta.tables.keys()


# #### Operaciones CRUD

# In[21]:


with engine.connect() as con:
    
    #Creamos la tabla en la BBDD
    clientes_table.create()
    # Insertamos un registro
    insert_st = clientes_table.insert().values(id= '1',nombre = 'Ramón', apellidos = 'García Hernandez',edad = 44, email = 'ragahe@yahoo.es')
    con.execute(insert_st)
    
    #Lectura
    select_st = clientes_table.select()
    results = con.execute(select_st)
    for r in results:
        print(r)
        
#Cerramos la conexión con la base de datos
con.close()


# In[22]:


with engine.connect() as con:
    
    #Actualización
    update_st =  clientes_table.update().where(clientes_table.c.nombre=='Ramón').values(edad=50)
    con.execute(update_st)

    
    #Lectura
    select_st = clientes_table.select()
    results = con.execute(select_st)
    for r in results:
        print(r)
        
#Cerramos la conexión con la base de datos
con.close()


# In[23]:


with engine.connect() as con:
    
    #Borrado
    delete_st = clientes_table.delete().where(clientes_table.c.id == "1")
    con.execute(delete_st)
    
    #Lectura
    select_st = clientes_table.select()
    results = con.execute(select_st)
    for r in results:
        print(r)
        
#Cerramos la conexión con la base de datos
con.close()

