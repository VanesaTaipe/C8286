#!/bin/bash

# Paso 1: Crear directorios temporales para almacenar los archivos del sitio web
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

# Paso 2: Copiar los directorios del sitio web y sample_app.py en el directorio temporal
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Paso 3: Crear un archivo Dockerfile
echo "FROM python" >> tempdir/Dockerfile  # Instalar Python en el contenedor
echo "RUN pip install flask" >> tempdir/Dockerfile  # Instalar Flask en el contenedor
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile  # Copiar directorio static
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile  # Copiar directorio templates
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile  # Copiar el script
echo "EXPOSE 8080" >> tempdir/Dockerfile  # Exponer el puerto 8080
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile  # Ejecutar el script Python

# Paso 4: Construir el contenedor Docker
cd tempdir
docker build -t sampleapp .

# Paso 5: Iniciar el contenedor y comprobar que se está ejecutando
docker run -t -d -p 8080:8080 --name samplerunning sampleapp

# Mostrar todos los contenedores Docker que se están ejecutando actualmente
docker ps -a

