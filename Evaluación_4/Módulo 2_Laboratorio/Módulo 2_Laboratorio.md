Laboratorio: Acceso y análisis de datos mediante Amazon S3

**Tarea 1. Crear una plantilla y pila de CloudFormation**

En la Consola de administración de AWS , busque y seleccione Cloud9 en Servicio. Vistas desde Cloud9. A continuación, en la instancia Cloud9, seleccione Abrir IDE. Creamos el archivo create\_bucket.yml.

Para validar una plantilla de CloudFormation, ejecute el siguiente comando en la terminal IDE de AWS Cloud9.

```aws cloudformation validate-template --template-body file://create\_bucket.yml```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.001.png)

A continuación, creará una pila de CloudFormation a partir de la plantilla.

- Para crear una pila, ejecute el siguiente comando

```aws cloudformation create-stack --stack-name ade-my-bucket --template-body file://create\_bucket.yml```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.002.png)

Entonces, cuando abramos S3 habrá un nuevo nombre de bucket.

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.003.jpeg)

- Para verificar que la pila haya creado los recursos necesarios, ejecute el siguiente comando:

```aws s3api list-buckets```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.004.png)

A continuación, intentaremos eliminar el bukcet eliminando la pila.

- Para eliminar srack, ejecute el siguiente comando

```aws cloudformation delete-stack --stack-name ade-my-bucket```

Regrese a la consola de administración de AWS – servicios – CloudFormation – Stacks. Se puede ver que la pila que se creó anteriormente (ade-my-bucket) no figura en la pila.

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.005.jpeg)

- Regrese a la terminal AWS Cloud9. Para verificar que la pila creada se haya eliminado, ejecute el siguiente comando:

```aws s3api list-buckets```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.006.png)

Conclusión. En esta tarea 1, se creó una plantilla de CloudFormation utilizando la CLI de AWS en el terminal AWS Cloud9. Valide la plantilla y úsela para crear la pila. Después de asegurarse de que se haya creado el depósito, elimínalo con la eliminación de la pila de CloudFormation.

**Tarea 2. Carga de datos de muestra en un depósito S3**

Examine los datos en el grupo de conjuntos de datos, que se ha proporcionado en formato .csv.

- Descargue el archivo ejecutando el siguiente comando:

```wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACDSCI-1-DEV/lab-01-s3/c ode.zip -P /home/ec2-user/environment```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.007.png)

- Para extraer los archivos, ejecute el siguiente comando:![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.008.png)

```unzip code.zi|p` ``

- Para ver el contenido de lab1.csv:

```cat lab1.csv```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.009.png)

Copie datos en el depósito S3

- Obtener el nombre del depósito de laboratorio:

```aws s3api list-buckets```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.010.png)

- Para copiar el conjunto de datos a S3 bukcet, ejecute el siguiente comando.![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.011.png)![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.012.jpeg)
- Nota: <ade-s3lab-bucket--a5b63450> es el nombre: ade-s3lab-bucket--a5b63450```

```aws s3 cp lab1.csv s3://ade-s3lab-bucket--a5b63450```

- Para confirmar que el archivo se ha agregado al depósito, ejecute el siguiente comando:

```aws s3 ls s3://ade-s3lab-bucket--a5b63450```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.013.png)

Conclusión. En la tarea 2, se descarga y extrae el conjunto de datos de ejemplo. Los datos se verifican y luego se copian en un depósito de S3 mediante los comandos de AWS CLI.

**Tarea 3. Consultando los datos**

Utilice S3 Select para ejecutar consultas SQL en los datos cargados.

- Consola de administración de Buka AWS — servicios — S3
- Pilih lab1.csv — Acciones de objetos — consulta con selección de S3.

Utilizamos ```SELECT * FROM s3object s LIMIT 5```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.014.jpeg)![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.015.jpeg)

A continuación, haga coincidir la consulta para ver solo el nombre de las tres primeras filas.

- Reemplazar consulta

```SELECT 'First Name' FROM s3object s LIMIT 3```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.016.png)

Conclusión. En la tarea 3, la función S3 Select se utiliza para mostrar datos. Por lo tanto, puede encontrar rápidamente datos alojados en un depósito de S3.

**Tarea 4. Modificar las propiedades de cifrado y el tipo de almacenamiento de un objeto** Cambiar la clase de almacenamiento de los objetos almacenados en Amazon S3

- Acciones de objetos: editar clase de almacenamiento

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.017.jpeg)

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.018.png)

Conclusión. En la tarea 4, aprendimos cómo cifrar y cambiar la clase de almacenamiento de datos almacenados como objetos en Amazon S3. Al utilizar clases de almacenamiento de niveles inteligentes, asegúrese de que los costos se optimicen para todos los datos almacenados en los objetos de S3.

**Tarea 5. Comprimir y consultar el conjunto de datos**

Compresión de archivo

- Abra la terminal AWS Cloud9 y ejecute el siguiente comando:

```zip lab lab1.csv```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.019.png)

- A continuación, para comprimir archivos en formato GZIP, ejecute el siguiente comando: ```gzip -v lab1.csv```

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.020.png)

- Para mostrar una lista de objetos en un directorio ```ls -la```

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.021.png)

- Cargando la versión GZIP a un depósito S3

  ```aws s3 cp lab1.csv.gz s3://ade-s3lab-bucket--a5b63450 --cache-control max-age=6|0```
  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.022.png)

Utilice S3 select para confirmar archivos comprimidos

- Regresar a la consola de Amazon S3
- Pilih ```lab1.csv.gz``` - acciones de objeto - consulta con selección S3

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.023.jpeg)

- En la configuración de entrada, deje la configuración predeterminada, para Compresión seleccione GZIP
- En la consulta SQL, ejecute el siguiente comando:

```SELECT * FROM s3object s LIMIT 3```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.024.jpeg)

Conclusión. En esta tarea, aprenderá cómo comprimir archivos de datos en formato GZIP, que es más eficiente que ZIP para reducir el tamaño del archivo y ayudar a reducir los costos de almacenamiento.

**Tarea 6. Administrar y probar el acceso restringido para un miembro del equipo** Revisar el grupo de IAM y la política de IAM de DataSCienceGroup

- Servicios — IAM — Usuarios — DataScienceGroup

Para saber si Paulo puede acceder a los datos en Amazon S3, realice una prueba de acceso mediante un comando de la AWS CLI.

- Servicios - CloudFormation - pilas

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.025.jpeg)

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.026.jpeg)

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.027.jpeg)

- Crear una variable para la clave de acceso. ```AK=AKIA5HWRCRZ6ENWRNCVV```

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.028.png)

- Crear una variable para la clave de acceso secreta ```SAK=tndUkwLrrxWv7CQF47Yy1OwE2TJNBWe6QRxgA7D1```

  ![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.029.png)

- Pruebe si el usuario Paulo puede ejecutar comandos de AWS CLI para el servicio amazonEC2

Se mostrará un mensaje de error. Tenga en cuenta que la política de IAM adjunta al grupo de IAM en el que este usuario inició sesión no tiene permiso para Amazon EC2.

```AWS\_ACCESS\_KEY\_ID=$AK AWS\_SECRET\_ACCESS\_KEY=$SAK aws ec2 describe-instances --region us-east-1```

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.030.png)

- Pruebe si el usuario Paulo puede ejecutar comandos de AWS CLI en objetos de S3.

```AWS\_ACCESS\_KEY\_ID=$AK AWS\_SECRET\_ACCESS\_KEY=$SAK aws s3api get-object --bucket ade-s3lab-bucket--a5b6345 |0--key lab1.csv --region us-east-1 pulled\_lab.cs```
![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.031.jpeg)



- Ver el contenido del objeto S3![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.032.png)

```cat pulled\_lab.csv```

Conclusión. En la tarea 6, aprenda cómo revisar los permisos en la consola de IAM. Además, también aprendimos cómo utilizar los comandos SCLI de AWS en la terminal AWS Cloud9 para probar los permisos de los usuarios.

![](Aspose.Words.f36363a1-969b-45cb-9c71-aa50362e1d98.033.jpeg)
