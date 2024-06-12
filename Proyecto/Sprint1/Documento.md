# Análisis de sentimientos en redes sociales

**Introducción**<BR>
El proyecto "Análisis de sentimientos en redes sociales" tiene como objetivo desarrollar un sistema capaz de extraer y analizar los sentimientos expresados en Twitter utilizando técnicas de procesamiento del lenguaje natural (NLP). El sistema está optimizado para el procesamiento paralelo y en tiempo real, lo que permite obtener información valiosa y actualizada sobre las opiniones y emociones de los usuarios en la plataforma.
En este documento, se describen los detalles técnicos y los procedimientos llevados a cabo durante el Sprint 1 del proyecto, que se enfoca en la extracción y el preprocesamiento de datos de Twitter utilizando su API.
Configuración de la API de Twitter
API utilizada
Se utilizará la API de Twitter v2 para extraer tweets en tiempo real.
Obtención de credenciales y configuración de autenticación
Para acceder a la API de Twitter, se requieren las siguientes credenciales:

Consumer Key (API Key)
Consumer Secret (API Secret)
Access Token
Access Token Secret

A continuación, se detallan los pasos para obtener las credenciales y configurar la autenticación:

Crear una cuenta de desarrollador en https://developer.twitter.com/.
Crear una nueva aplicación y obtener las credenciales necesarias.
Configurar los permisos de la aplicación según los requisitos del proyecto.

Parámetros de consulta
Para extraer datos relevantes de la API de Twitter, se utilizarán los siguientes parámetros de consulta:

q: Palabras clave o hashtags para filtrar los tweets según las categorías de sentimiento (positivo, negativo y neutro).
lang: Idioma de los tweets (por ejemplo, "es" para español).
tweet.fields: Campos adicionales de los tweets a extraer (por ejemplo, "created_at", "author_id").

Extracción de datos
Script de extracción
Se desarrollará un script en Python para realizar peticiones a la API de Twitter y extraer datos en tiempo real. A continuación, se presenta una descripción general del script:

Utilizará la biblioteca tweepy para interactuar con la API de Twitter.
Realizará peticiones a la API de forma periódica para obtener nuevos tweets.
Procesará los datos extraídos y los almacenará en una base de datos.

Lógica de extracción en tiempo real
El script de extracción se ejecutará de forma continua para obtener datos en tiempo real. Se implementará la siguiente lógica:

Se establecerá una conexión persistente con la API de Twitter utilizando la funcionalidad de streaming.
Se filtrarán los tweets en función de las palabras clave o hashtags especificados para cada categoría de sentimiento.
Cada tweet recibido se procesará y almacenará en la base de datos.

Frecuencia de extracción y almacenamiento

La extracción de tweets se realizará en tiempo real mediante la conexión persistente con la API de streaming.
Los tweets extraídos se almacenarán en la base de datos inmediatamente después de ser recibidos y procesados.
Se extraerán un total de 5000 tweets por cada categoría de sentimiento (positivo, negativo y neutro), resultando en un total de 15000 tweets.

Instrucciones para ejecutar el script de extracción

Asegurarse de tener las credenciales de la API de Twitter configuradas correctamente.
Instalar las dependencias necesarias:
Copy codepip install tweepy pymongo

Ejecutar el script de extracción de Twitter:
Copy codepython twitter_extraction.py

El script se ejecutará de forma continua hasta que se alcance el número total de tweets deseado por categoría.

Preprocesamiento de datos
Técnicas de preprocesamiento aplicadas
Se aplicarán las siguientes técnicas de preprocesamiento a los datos extraídos:

Eliminación de caracteres especiales y signos de puntuación.
Conversión de texto a minúsculas.
Eliminación de stopwords (palabras comunes sin significado relevante).
Tokenización de texto en palabras individuales.
Lematización de palabras para obtener su forma base.
Manejo de emojis y emoticones, convirtiéndolos en representaciones textuales.
Extracción de hashtags y menciones de usuarios.

Limpieza y normalización de datos
Los datos extraídos pasarán por un proceso de limpieza y normalización para garantizar su calidad y consistencia:

Se eliminarán tweets duplicados.
Se manejarán caracteres especiales y se eliminarán aquellos que no sean relevantes.
Se normalizarán fechas y horas a un formato estándar.
Se manejarán valores faltantes o nulos de manera adecuada.

Estructura de los datos preprocesados
Los datos preprocesados se estructurarán en un formato adecuado para su posterior análisis:

Cada tweet se representará como un documento en la base de datos.
Se utilizarán campos específicos para almacenar información relevante, como:

user_id: Identificador del usuario que publicó el tweet.
created_at: Fecha y hora de creación del tweet.
likes: Número de "me gusta" del tweet.
source: Fuente del tweet (dispositivo o aplicación utilizada para publicar el tweet).
tweet: Texto del tweet.
sentiment: Categoría de sentimiento (positivo, negativo o neutro).



Almacenamiento de datos
Base de datos utilizada
Se utilizará MongoDB como base de datos para almacenar los datos extraídos y preprocesados. MongoDB es una base de datos NoSQL que permite una gran flexibilidad y escalabilidad en el manejo de datos no estructurados.
Esquema de la base de datos
La base de datos tendrá la siguiente estructura:

Base de datos: sentiment_analysis_db
Colección: tweets

Campos:

user_id: Identificador del usuario que publicó el tweet.
created_at: Fecha y hora de creación del tweet.
likes: Número de "me gusta" del tweet.
source: Fuente del tweet (dispositivo o aplicación utilizada para publicar el tweet).
tweet: Texto del tweet.
sentiment: Categoría de sentimiento (positivo, negativo o neutro).





Instrucciones para configurar y conectarse a la base de datos

Instalar MongoDB en el sistema siguiendo las instrucciones oficiales: https://docs.mongodb.com/manual/installation/
Asegurarse de que el servicio de MongoDB esté en ejecución.
En el script de Python, utilizar la biblioteca pymongo para conectarse a la base de datos:
pythonCopy codefrom pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['sentiment_analysis_db']
tweets_collection = db['tweets']

## Resolución de problemas

### Problemas comunes y soluciones conocidas

- **Error de autenticación con las APIs**:
  - Verificar que las credenciales de autenticación sean correctas.
  - Asegurarse de que los permisos de la aplicación estén configurados adecuadamente.
  - Revisar si hay restricciones de velocidad o límites de uso excedidos.

- **Problemas de conexión con la base de datos**:
  - Asegurarse de que el servicio de MongoDB esté en ejecución.
  - Verificar la cadena de conexión y los detalles de autenticación.
  - Comprobar si hay conflictos de puertos o problemas de red.

### Errores frecuentes y cómo manejarlos

- **Errores de tasa límite en las APIs**:
  - Implementar un mecanismo de manejo de errores y reintentos en los scripts de extracción.
  - Utilizar un retraso entre las solicitudes para evitar exceder los límites de velocidad.
  - Considerar el uso de técnicas de almacenamiento en caché para minimizar las solicitudes repetidas.

- **Datos mal formados o faltantes**:
  - Implementar verificaciones y manejo de errores en los scripts de preprocesamiento.
  - Utilizar valores predeterminados o estrategias de imputación para manejar datos faltantes.
  - Realizar validaciones y limpiezas adicionales según sea necesario.

