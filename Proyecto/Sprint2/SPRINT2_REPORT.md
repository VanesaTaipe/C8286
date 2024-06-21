Informe: Sistema de Análisis de Sentimientos Multilingüe

1. Introducción

Este informe detalla el desarrollo y evaluación de un sistema de análisis de sentimientos multilingüe capaz de procesar textos en inglés, español y portugués. El objetivo principal fue crear una herramienta robusta para clasificar el sentimiento de textos en estas tres lenguas como positivo, negativo o neutro.

2. Metodología

2.1 Preprocesamiento de Datos
- Se implementó un proceso de preprocesamiento que incluye:
a. Detección de idioma: Utilizar langdetect es una buena elección para identificar el idioma de los textos. Asegúrate de considerar cómo manejar textos que podrían estar en varios idiomas o mezclados.

b. Tokenización específica: NLTK proporciona tokenizadores específicos para diferentes idiomas, lo cual es excelente para adaptar el procesamiento según el idioma detectado. Asegúrate de ajustar estos tokenizadores según las necesidades específicas de tu tarea.

c. Eliminación de stopwords adaptada: Es crucial adaptar la lista de stopwords según el idioma detectado para mejorar la calidad del análisis. Esto ayuda a eliminar palabras que no aportan significado al análisis de sentimientos.

d. Generación de bi-gramas: Es una buena práctica para capturar frases significativas y expresiones coloquiales que pueden afectar el sentimiento general del texto.

2.2 Modelos Implementados

a) BERT (Bidirectional Encoder Representations from Transformers)

Utilizar una variante multilingüe como XLM-RoBERTa es apropiado para manejar textos en diferentes idiomas. El fine-tuning específico para análisis de sentimientos con una configuración de 3 épocas y tamaño de batch de 8 es razonable. Asegúrate de monitorear el rendimiento del modelo durante el entrenamiento para ajustar estos hiperparámetros si es necesario.
   - Se utilizó XLM-RoBERTa, una variante multilingüe de BERT.
   - Se realizó fine-tuning para la tarea específica de análisis de sentimientos.
   - Configuración: 3 épocas, tamaño de batch de 8, warmup steps de 500.

b) Naive Bayes

Este es un buen modelo baseline para comparar con BERT. El uso de CountVectorizer con bi-gramas es adecuado para capturar características importantes del texto. Considera también evaluar otros clasificadores basados en árboles como RandomForest o SVM lineales, ya que a veces pueden superar a Naive Bayes dependiendo de la naturaleza de los datos.

   - Se implementó MultinomialNB como baseline y modelo complementario.
   - Se utilizó CountVectorizer con bi-gramas para la vectorización del texto.

Concepto clave:

Vectorización del texto: Esencial para convertir los textos en formatos numéricos comprensibles por los modelos de aprendizaje automático. CountVectorizer con bi-gramas es útil, pero considera también TfidfVectorizer para ponderar términos según su importancia relativa.

Fine-tuning: Asegúrate de ajustar adecuadamente los hiperparámetros durante el fine-tuning de BERT para optimizar el rendimiento del modelo en la tarea específica de análisis de sentimientos.

2.3 Entrenamiento y Evaluación
- El dataset se dividió en conjuntos de entrenamiento (80%) y prueba (20%).
- Se entrenaron ambos modelos con los datos preprocesados.
- Se evaluaron utilizando métricas estándar: precisión, recall, F1-score y matrices de confusión.

3. Resultados
   
![https://github.com/VanesaTaipe/C8286/blob/7075caba3ac54ea44e2981bfc1a6409fd110348f/Proyecto/Sprint2/imagenes/evaluacion.png]

3.1 Comparación de Rendimiento:

Precisión: Mide la proporción de predicciones positivas correctas sobre el total de predicciones positivas hechas por el modelo.

Recall: Indica la proporción de verdaderos positivos identificados correctamente respecto al total de casos positivos en los datos reales.

F1-score: Es una medida que combina precisión y recall en un solo número, útil cuando hay un desbalance entre las clases.

Accuracy: Proporciona la proporción de predicciones correctas sobre el total de predicciones realizadas por el modelo.

BERT (XLM-RoBERTa):

- Precisión: 0.88 significa que el 88% de las predicciones positivas hechas por BERT fueron correctas.
- Recall: 0.88 indica que el 88% de los verdaderos positivos en los datos reales fueron identificados por BERT.
- F1-score: 0.88 es un promedio ponderado de precisión y recall, proporcionando una medida única del rendimiento del modelo.
- Accuracy: 0.88 significa que el 88% de todas las predicciones hechas por BERT fueron correctas en general.

Naive Bayes:

- Precisión: 0.86 indica que el 86% de las predicciones positivas hechas por Naive Bayes fueron correctas.
- Recall: 0.85 significa que el 85% de los verdaderos positivos en los datos reales fueron identificados por Naive Bayes.
- F1-score: 0.85 es un promedio ponderado de precisión y recall para Naive Bayes.
  Accuracy: 0.85 significa que el 85% de todas las predicciones hechas por Naive Bayes fueron correctas en general.

3.2 Análisis por Clase
imagen
  
BERT: Muestra una distribución equilibrada de verdaderos positivos (TP) y falsos negativos (FN) en todas las clases, indicando una capacidad sólida para clasificar correctamente los sentimientos.

Naive Bayes: Tiene más falsos positivos (FP) y falsos negativos (FN) en comparación con BERT, lo que sugiere una menor precisión en la clasificación en algunas clases.
3.3 Pruebas Multilingües

Se realizaron pruebas con textos de ejemplo en los tres idiomas:
- Inglés: "This product is excellent, I love it."
- Español: "El servicio al cliente fue terrible, muy decepcionado."
- Portugués: "A qualidade é aceitável, mas pode melhorar."

Ambos modelos demostraron capacidad para manejar textos en los tres idiomas objetivo, con BERT mostrando una ligera ventaja en la captación de matices lingüísticos.

4. Discusión

4.1 Fortalezas del Sistema

- Capacidad multilingüe efectiva, manejando inglés, español y portugués.
- Alto rendimiento general en la clasificación de sentimientos.
- BERT muestra un rendimiento más equilibrado entre clases.
- Naive Bayes ofrece una alternativa eficiente en términos de recursos computacionales.

4.2 Limitaciones y Áreas de Mejora

- El dataset utilizado puede tener limitaciones en términos de diversidad y balance de clases.
- El tiempo de entrenamiento y recursos computacionales requeridos por BERT son significativos.
- La precisión en la detección de sentimientos neutros es ligeramente inferior a las otras categorías.

5. Conclusiones

El sistema desarrollado demuestra ser efectivo en el análisis de sentimientos multilingüe. BERT muestra un rendimiento ligeramente superior, especialmente en la captación de contextos complejos, mientras que Naive Bayes ofrece una alternativa eficiente con un rendimiento cercano.

BERT (XLM-RoBERTa) muestra un rendimiento más consistente y preciso en todas las clases de sentimientos en comparación con Naive Bayes.
Naive Bayes, aunque tiene ciertas fortalezas como una alta precisión en algunas clases, tiene limitaciones significativas en términos de recall y equilibrio general de métricas.
Las matrices de confusión proporcionan una perspectiva detallada sobre dónde cada modelo tiene dificultades y aciertos en la clasificación de sentimientos.

6. Futuras implimitaciones
   
Identificar los cuellos de botella en el rendimiento del sistema de análisis de sentimientos:

Por qué es importante:

Permite localizar las partes del sistema que limitan el rendimiento global.
Ayuda a priorizar los esfuerzos de optimización donde tendrán el mayor impacto.

Cómo implementarlo:

Utilizar herramientas de profiling como cProfile en Python para medir el tiempo de ejecución de diferentes partes del código.
Monitorear el uso de recursos (CPU, memoria, I/O) durante la ejecución del sistema.
Analizar los tiempos de respuesta en diferentes etapas del procesamiento (preprocesamiento, inferencia del modelo, post-procesamiento).


Implementar técnicas de paralelismo utilizando multiprocessing y threading:

Por qué es importante:

Permite aprovechar múltiples núcleos de CPU, acelerando significativamente el procesamiento.
Puede reducir dramáticamente el tiempo total de procesamiento para grandes volúmenes de datos.

Cómo implementarlo:

Usar multiprocessing para tareas intensivas en CPU como el preprocesamiento de texto o la inferencia de modelos.
Utilizar threading para operaciones I/O bound como la carga de datos o la escritura de resultados.
Implementar un pool de workers para procesar lotes de textos en paralelo.
