
Proyecto: Sistema de Análisis de Sentimientos en tiempo real 

Objetivo del proyecto:
Desarrollar un sistema de análisis de sentimientos capaz de procesar y clasificar textos, utilizando técnicas avanzadas de procesamiento del lenguaje natural y aprendizaje automático, e implementar un dashboard interactivo para facilitar su uso y visualización de resultados en tiempo real. Además usando técnicas de procesamiento paralelo para mejorar la eficiencia. 

Estructura del Proyecto:

Sprint 1: Extracción y Preprocesamiento de Datos
Objetivos:
1. Configurar y utilizar la API de Twitter para la extracción de datos.
2. Implementar un sistema de almacenamiento eficiente para los datos extraídos.
3. Desarrollar un pipeline de preprocesamiento de datos robusto.

Actividades:
1. Configuración de la API:
   - Configurar la API de Twitter v2 y autenticación mediante Bearer Token.
   - Implementar manejo de límites de tasa (Rate Limits).

2. Extracción de datos:
   - Implementar estrategias de búsqueda y extracción de tweets.
   - Desarrollar queries complejas para cada sentimiento.

3. Almacenamiento de datos:
   - Almacenamiento inicial de datos en formato CSV.
   - Migración de datos a MongoDB para un almacenamiento más flexible.

4. Preprocesamiento de datos:
   - Desarrollo de una pipeline de limpieza de texto.
   - Implementación de técnicas para manejar duplicados y datos irrelevantes.

5. Análisis de calidad:
   - Evaluación de la calidad de los datos extraídos y preprocesados.
   - Análisis de la eficiencia del preprocesamiento.

Entregables:
- Script de extracción de datos de Twitter.
- Pipeline de preprocesamiento de datos.
- Base de datos MongoDB con tweets procesados.
- Informe sobre la calidad de los datos y eficiencia del preprocesamiento.

Sprint 2: Desarrollo y Evaluación de Modelos de Análisis de Sentimientos
Objetivos:
1. Implementar y entrenar modelos de análisis de sentimientos.
2. Evaluar y comparar el rendimiento de los modelos implementados.
3. Optimizar los modelos para mejorar la precisión en la clasificación de sentimientos.
4. Implementar técnicas de procesamiento paralelo para mejorar la eficiencia.

Actividades:
1. Implementación de modelos:
   - Desarrollar un modelo baseline utilizando Naive Bayes.
   - Implementar y realizar fine-tuning de un modelo BERT (XLM-RoBERTa).

2. Optimización del procesamiento:
   - Implementar funciones de procesamiento paralelo (preprocess_parallel, parallel_train_models, parallel_predict).

3. Entrenamiento y evaluación:
   - Entrenar los modelos utilizando el conjunto de datos preprocesado.
   - Evaluar los modelos usando métricas estándar y matrices de confusión.


Entregables:
- Modelos entrenados (Naive Bayes y BERT).
- Código de implementación de modelos y funciones de procesamiento paralelo..

Sprint 3: Análisis Comparativo y Desarrollo del Dashboard
Objetivos:
1. Realizar un análisis comparativo profundo de los modelos implementados.
2. Desarrollar un dashboard interactivo para la visualización y uso de los modelos.
3. Implementar funcionalidades de análisis en tiempo real en el dashboard.

Actividades:
1. Análisis comparativo detallado:
   - Evaluar el tamaño en memoria de los modelos y componentes.
   - Medir y comparar el tiempo de predicción de los modelos.

2. Desarrollo del dashboard:
   - Crear una interfaz usando Streamlit para entrada de texto multilingüe.
   - Implementar visualización de resultados de análisis de sentimientos.
   - Desarrollar gráficos comparativos de los resultados de ambos modelos.

3. Optimización del rendimiento:
   - Implementar procesamiento en tiempo real en el dashboard.
   - Optimizar el manejo eficiente de solicitudes.

4. Integración de información adicional:
   - Incluir métricas de rendimiento y detalles técnicos en el dashboard.

Entregables:
- Dashboard interactivo implementado en Streamlit.
- Código fuente del dashboard y de las funcionalidades de análisis en tiempo real.
- Informe final del proyecto con documentación completa del desarrollo y resultados obtenidos.
- Repositorio de GitHub con toda la documentación, código y resultados del proyecto.

Requisitos de Software:
- Python 3.x
- Tweepy
- NLTK
- pandas
- scikit-learn
- PyTorch
- Transformers (Hugging Face)
- MongoDB
- Streamlit
- multiprocessing
