# Para crear una tarea programada que ejecute un script en python, seguir éstos pasos:
#
# Crear un archivo .bat con el siguiente contenido
# @echo off
# call "ruta para llegar a activate.bat dentro del directorio de instalación de anaconda" "carpeta de instalación de anaconda"
# python "archivo .py que contiene el código a ejecutar de manera programada.  debe incluir la ruta completa y nombre del script"



@echo off
call C:\Users\german\anaconda3\Scripts\activate.bat C:\Users\german\anaconda3
python C:\Users\german\Documents\00.Trabajo\01.C2B\37\print-hola.py
pause