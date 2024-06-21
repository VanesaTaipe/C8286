# **Informe del Sprint 1**

El proyecto "Análisis de sentimientos en redes sociales" tiene como objetivo desarrollar un sistema capaz de extraer y analizar los sentimientos expresados en Twitter utilizando técnicas de procesamiento del lenguaje natural (NLP). El sistema está optimizado para el procesamiento paralelo y en tiempo real, lo que permite obtener información valiosa y actualizada sobre las opiniones y emociones de los usuarios en la plataforma.
1. Extracción de Datos de Twitter
En este documento, se describen los detalles técnicos y los procedimientos llevados a cabo durante el Sprint 1 del proyecto, que se enfoca en la extracción y el preprocesamiento de datos de Twitter utilizando su API. Configuración de la API de Twitter API utilizada Se utilizará la API de Twitter v2 para extraer tweets en tiempo real. Obtención de credenciales y configuración de autenticación Para acceder a la API de Twitter, se requieren las siguientes credenciales:
1.1. Configuración de la API y Autenticación
Concepto: API v2 de Twitter y Bearer Token
- Se utilizó la API v2 de Twitter, que requiere un Bearer Token para la autenticación.
- El Bearer Token proporciona un nivel de seguridad mayor que los métodos de autenticación anteriores.

Decisión: Uso de Tweepy para la interacción con la API
- Se eligió Tweepy por su facilidad de uso y compatibilidad con la API v2.
- Código implementado:
  ```python
  client = tweepy.Client(bearer_token=bearer_token)
  ```

Problema: Manejo de límites de tasa (Rate Limits)
- La API de Twitter impone límites en el número de solicitudes por intervalo de tiempo.
Solución: Implementación de pausas y manejo de excepciones
- Se añadieron pausas entre solicitudes y se manejaron excepciones específicas de límite de tasa.

1.2. Estrategia de Búsqueda y Extracción
Concepto: Queries de búsqueda y campos de tweet
- Se construyeron queries complejas utilizando palabras clave para cada sentimiento.
- Se especificaron campos concretos a extraer: author_id, created_at, public_metrics, source, text.

Decisión: Extracción de 3009 tweets por categoría
- Se buscó un balance entre un tamaño de muestra significativo y las limitaciones de la API.
- Implementación:
  ```python
  tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["author_id", "created_at", "public_metrics", "source", "text"])
  ```

Problema: Limitación de 100 tweets por solicitud
Solución: Implementación de un bucle de paginación
- Se realizaron múltiples solicitudes, ajustando el número de resultados en la última solicitud.

2. Almacenamiento de Datos

2.1. Almacenamiento Inicial en CSV
Concepto: Serialización de datos en formato CSV
- Los datos se almacenaron inicialmente en un archivo CSV para facilitar la inspección y el procesamiento inicial.

Decisión: Uso de pandas para la manipulación de datos
- Pandas proporciona funciones eficientes para la lectura y escritura de CSV.
- Código implementado:
  ```python
  tweets_df = pd.DataFrame(tweets_data)
  tweets_df.to_csv("tweets_sin_entrenamiento.csv", index=False)
  ```

Problema: Preservación de la estructura de datos complejos
Solución: Aplanamiento de estructuras anidadas
- Se aplanaron estructuras como 'public_metrics' para facilitar su almacenamiento en CSV.

2.2. Migración a MongoDB
Concepto: Base de datos NoSQL orientada a documentos
- MongoDB permite almacenar documentos JSON complejos, ideal para tweets con estructura variable.

Decisión: Uso de PyMongo para la interacción con MongoDB
- PyMongo ofrece una API Pythonica para interactuar con MongoDB.
- Implementación:
  ```python
  client = MongoClient("mongodb://localhost:27017/")
  db = client["twitter_db"]
  collection = db["tweets"]
  collection.insert_many(tweets_data)
  ```

Problema: Garantizar la integridad de los datos durante la migración
Solución: Verificación post-inserción y manejo de excepciones
- Se implementó una verificación del número de documentos insertados contra el número de registros en el CSV.

3. Preprocesamiento de Datos

3.1. Limpieza de Texto
Concepto: Técnicas de procesamiento de lenguaje natural (NLP)
- Se aplicaron técnicas de NLP para limpiar y normalizar el texto de los tweets.

Decisión: Implementación de una pipeline de limpieza
- Se creó una secuencia de pasos de limpieza incluyendo:
  1. Eliminación de URLs
  2. Manejo de emojis
  3. Eliminación de menciones y hashtags
  4. Normalización de texto (minúsculas, eliminación de caracteres especiales)

Problema: Pérdida potencial de información semántica
Solución: Preservación selectiva y etiquetado
- Se preservaron ciertos elementos como emojis, convirtiéndolos a texto descriptivo.
- Se consideró el etiquetado de menciones y hashtags en lugar de su eliminación completa.

3.2. Manejo de Duplicados y Datos Irrelevantes
Concepto: Identificación y eliminación de datos redundantes o no representativos
- Los duplicados y tweets irrelevantes pueden sesgar el análisis de sentimientos.

Decisión: Implementación de criterios de unicidad y relevancia
- Se eliminaron duplicados basados en la combinación de 'user_id' y 'tweet'.
- Implementación:
  ```python
  data = data.drop_duplicates(subset=['user_id', 'tweet'])
  ```

Problema: Reducción significativa del tamaño del dataset
- El conjunto de datos se redujo de 9,028 a 1,201 tweets.
Solución: Análisis de impacto y ajuste de estrategias de recolección
- Se realizó un análisis de la distribución de sentimientos post-limpieza.
- Se consideraron técnicas de aumento de datos para compensar la reducción.

4. Análisis de Resultados y Métricas

4.1. Evaluación de la Calidad de los Datos
Concepto: Métricas de calidad para conjuntos de datos de texto
- Se implementaron métricas específicas para evaluar la calidad del dataset resultante.

Decisión: Cálculo de métricas clave
- Distribución de sentimientos
- Longitud promedio de tweets
- Diversidad léxica (número de palabras únicas / número total de palabras)

Problema: Desbalance en las categorías de sentimiento
Solución: Consideración de técnicas de balanceo
- Se evaluó la necesidad de aplicar técnicas como SMOTE (Synthetic Minority Over-sampling Technique) para balancear las clases.

4.2. Eficiencia del Preprocesamiento
Concepto: Optimización de rendimiento para escalabilidad
- Se midió y optimizó el tiempo de ejecución del proceso de preprocesamiento.

Decisión: Implementación de procesamiento por lotes
- Se dividió el procesamiento en lotes para manejar grandes volúmenes de datos eficientemente.

Problema: Tiempo de procesamiento para conjuntos de datos más grandes
Solución: Exploración de técnicas de paralelización
- Se investigó el uso de bibliotecas como multiprocessing para paralelizar el procesamiento.

5. Conclusiones y Próximos Pasos

- Se logró crear un pipeline robusto de extracción y preprocesamiento de datos de Twitter.
- La reducción significativa del dataset plantea desafíos para el análisis de sentimientos.
- Se identificó la necesidad de refinar las estrategias de extracción y limpieza para futuros proyectos.

Próximos pasos:
1. Implementar técnicas avanzadas de NLP para mejorar la limpieza y normalización del texto.
2. Explorar métodos de aumento de datos para compensar la pérdida de tweets durante la limpieza.
3. Desarrollar un sistema de clasificación de sentimientos más granular, posiblemente utilizando técnicas de aprendizaje profundo.
