Informe: Sistema de Análisis de Sentimientos Multilingüe

1. Introducción

Este informe detalla el desarrollo y evaluación de un sistema de análisis de sentimientos multilingüe capaz de procesar textos en inglés, español y portugués. El objetivo principal fue crear una herramienta robusta para clasificar el sentimiento de textos en estas tres lenguas como positivo, negativo o neutro.

2. Metodología

2.1 Preprocesamiento de Datos

- Se implementó un proceso de preprocesamiento que incluye:
  
  a. Detección de idioma: Se utilizó la biblioteca `langdetect` para identificar el idioma de los textos. Este paso es crucial para adaptar el procesamiento posterior según el idioma detectado.
  
  b. Tokenización: Se utilizaron los tokenizadores específicos de idioma de la librería NLTK. Esto permite dividir el texto en unidades léxicas (tokens) de manera más precisa para cada lengua.
  
  c. Eliminación de stopwords: Se eliminaron las stopwords específicas de cada idioma (inglés, español y portugués) utilizando las listas proporcionadas por NLTK. Esto ayuda a reducir el ruido y se enfoca en las palabras más relevantes para el análisis de sentimientos.
  
  d. Generación de bi-gramas: Se generaron bi-gramas (secuencias de dos palabras) a partir de los tokens. Esto permite capturar frases y expresiones significativas que pueden afectar el sentimiento general del texto.

2.2 Modelos Implementados

a) BERT (Bidirectional Encoder Representations from Transformers)

   - Se utilizó la variante multilingüe XLM-RoBERTa, que ha sido entrenada en múltiples idiomas y puede manejar textos en diferentes lenguas.
     
   - Se realizó un fine-tuning del modelo pre-entrenado para adaptarlo específicamente a la tarea de análisis de sentimientos.

    
   - Configuración: 3 épocas de entrenamiento, tamaño de batch de 8, warmup steps de 300. Estos hiperparámetros se ajustaron para optimizar el rendimiento del modelo en la tarea específica.


b) Naive Bayes

   - Se implementó el clasificador MultinomialNB como modelo baseline, que es una opción simple y eficiente para la clasificación de textos.
     
   - Se utilizó CountVectorizer con bi-gramas para la vectorización del texto, lo que permite capturar información sobre la co-ocurrencia de palabras.

2.3 Entrenamiento y Evaluación

- El conjunto de datos se dividió en conjuntos de entrenamiento (80%) y prueba (20%).
  
- Se entrenaron ambos modelos (BERT y Naive Bayes) utilizando los datos preprocesados.
  
- Se evaluaron los modelos utilizando métricas estándar de clasificación: precisión, recall, F1-score y matrices de confusión. Estas métricas permiten analizar el rendimiento de los modelos en diferentes aspectos.

3. Resultados
   
 ![Texto alternativo](https://github.com/VanesaTaipe/C8286/blob/00665968e32ddff4282dffc6d15a63367e410ea3/Proyecto/Sprint2/imagenes/imagen.png)

3.1 Comparación de Rendimiento:
```

Reporte de clasificación BERT:
              precision    recall  f1-score   support

           0       0.89      0.88      0.88        82
           1       0.92      0.83      0.88        59
           2       0.87      0.93      0.90       100

    accuracy                           0.89       241
   macro avg       0.89      0.88      0.89       241
weighted avg       0.89      0.89      0.89       241

```

```
Reporte de clasificación Naive Bayes:
              precision    recall  f1-score   support

           0       0.90      0.73      0.81        82
           1       0.78      0.78      0.78        59
           2       0.79      0.91      0.85       100

    accuracy                           0.82       241
   macro avg       0.82      0.81      0.81       241
weighted avg       0.82      0.82      0.82       241

```

Modelo BERT:

Clase 0:

Precisión de 0.89: Significa que el 89% de las muestras que el modelo BERT clasificó como clase 0 realmente pertenecen a la clase 0. Recuerdo de 0.88: Significa que el modelo BERT logró identificar correctamente el 88% de todas las muestras que realmente pertenecen a la clase 0. Puntuación F1 de 0.88: Es una métrica equilibrada entre precisión y recuerdo, lo que indica un buen rendimiento general para esta clase.

Clase 1:

Precisión de 0.92: Significa que el 92% de las muestras que el modelo BERT clasificó como clase 1 realmente pertenecen a la clase 1. Recuerdo de 0.83: Significa que el modelo BERT logró identificar correctamente el 83% de todas las muestras que realmente pertenecen a la clase 1. Puntuación F1 de 0.88: Nuevamente, un buen rendimiento general para esta clase.

Clase 2:

Precisión de 0.87: Significa que el 87% de las muestras que el modelo BERT clasificó como clase 2 realmente pertenecen a la clase 2. Recuerdo de 0.93: Significa que el modelo BERT logró identificar correctamente el 93% de todas las muestras que realmente pertenecen a la clase 2. Puntuación F1 de 0.90: Excelente rendimiento general para esta clase.

Exactitud general (Accuracy): 0.89, lo que significa que el modelo BERT clasificó correctamente el 89% de todas las muestras. Promedios Macro y Ponderado: Reflejan el rendimiento promedio del modelo en todas las clases.

3.2 Análisis por Clase(Matriz de confusion)

 ![Texto alternativo](https://github.com/VanesaTaipe/C8286/blob/00665968e32ddff4282dffc6d15a63367e410ea3/Proyecto/Sprint2/imagenes/matri.png)

El análisis de las matrices de confusión permite visualizar cómo se comportan los modelos en la clasificación de cada clase (positivo, negativo y neutro). 

BERT muestra una distribución más equilibrada de verdaderos positivos (TP) y falsos negativos (FN) en todas las clases, lo que indica que tiene una mayor capacidad para clasificar correctamente los sentimientos. Por otro lado, Naive Bayes presenta más falsos positivos (FP) y falsos negativos (FN) en comparación con BERT, lo que sugiere una menor precisión en la clasificación de algunas clases.

3.3 Pruebas Multilingües

Se realizaron pruebas con textos de ejemplo en los tres idiomas (inglés, español y portugués), y ambos modelos demostraron capacidad para manejar textos en estas lenguas. Sin embargo, BERT mostró una ligera ventaja en la captación de matices lingüísticos, lo que le permite una clasificación más precisa en algunos casos.


4. Conclusiones
- BERT (XLM-RoBERTa) demuestra un rendimiento más consistente y preciso en todas las clases de sentimientos en comparación con Naive Bayes.
- Naive Bayes, aunque tiene ciertas fortalezas como una alta precisión en algunas clases, presenta limitaciones significativas en términos de recall y equilibrio general de métricas.
- Las matrices de confusión proporcionan una perspectiva detallada sobre dónde cada modelo tiene dificultades y aciertos en la clasificación de sentimientos.

6. Futuras Implementaciones
   - Identificar los cuellos de botella en el rendimiento del sistema de análisis de sentimientos:
     - Utilizar herramientas de profiling como `cProfile` en Python para medir el tiempo de ejecución de diferentes partes del código.
     - Monitorear el uso de recursos (CPU, memoria, I/O) durante la ejecución del sistema.
     - Analizar los tiempos de respuesta en diferentes etapas del procesamiento (preprocesamiento, inferencia del modelo, post-procesamiento).
   - Implementar técnicas de paralelismo utilizando `multiprocessing` y `threading`:
     - Usar `multiprocessing` para tareas intensivas en CPU como el preprocesamiento de texto o la inferencia de modelos.
     - Utilizar `threading` para operaciones I/O bound como la carga de datos o la escritura de resultados.
     - Implementar un pool de workers para procesar lotes de textos en paralelo.
     - Realizar un dashboard 

