Informe: Análisis Comparativo de Modelos de Aprendizaje Automático para Clasificación de Textocon daskhboard en tiempo real

1. Introducción

Este informe detalla el desarrollo y evaluación de un sistema de clasificación de texto que compara dos enfoques diferentes: un modelo Naive Bayes tradicional y un modelo BERT (Bidirectional Encoder Representations from Transformers) avanzado. El objetivo principal fue analizar y comparar estos modelos en términos de tamaño, escala y rendimiento para la tarea de clasificación de texto. Este análisis es crucial para entender las ventajas y desventajas de cada enfoque en diferentes escenarios de aplicación.

2. Metodología

2.1 Modelos Implementados

a) BERT (Bidirectional Encoder Representations from Transformers)
   - Se utilizó la variante XLM-RoBERTa, un modelo pre-entrenado multilingüe.
   - Se realizaron ajustes en el estado del diccionario del modelo para asegurar la compatibilidad con la arquitectura cargada.
   - Este modelo representa el estado del arte en procesamiento de lenguaje natural, capaz de capturar contextos complejos y relaciones semánticas.

b) Naive Bayes
   - Se implementó un clasificador Naive Bayes como modelo baseline.
   - Se utilizó en conjunto con un vectorizador para la representación de texto.
   - Este modelo, aunque más simple, es conocido por su eficiencia y buen rendimiento en tareas de clasificación de texto.

2.2 Componentes Auxiliares

   - Vectorizador: Utilizado para transformar el texto en una representación numérica, crucial para el funcionamiento del modelo Naive Bayes.
   - Codificador de etiquetas: Empleado para codificar las clases de salida, permitiendo una representación numérica de las categorías.

2.3 Evaluación

Se evaluaron los modelos utilizando las siguientes métricas:

a) Tamaño en memoria de los modelos y componentes:
   - Razón: Esta medición es crucial para entender los requisitos de recursos computacionales de cada modelo. Afecta la viabilidad de despliegue en dispositivos con recursos limitados, los costos de almacenamiento y distribución, y el tiempo de carga del modelo.

b) Escala de los modelos:
   - Tamaño del vocabulario: Indica la riqueza y diversidad del lenguaje que el modelo puede manejar.
   - Número de clases: Refleja la complejidad de la tarea de clasificación.
   - Número de parámetros: Indicador de la complejidad y capacidad del modelo para capturar relaciones en los datos.

c) Tiempo de predicción (para el modelo Naive Bayes):
   - Razón: Crucial para evaluar la eficiencia del modelo en tiempo real. Se mide específicamente para Naive Bayes como punto de referencia para comparar con modelos más complejos.

3. Resultados

3.1 Comparación de Tamaños:

```
Tamaño del modelo Naive Bayes: [nb_size] MB
Tamaño del vectorizador: [vectorizer_size] MB
Tamaño del codificador de etiquetas: [label_encoder_size] MB
Tamaño del modelo BERT: [bert_size] MB
```

3.2 Escala de los Modelos:

```
Tamaño del vocabulario del vectorizador: [vocab_size]
Número de clases en el codificador de etiquetas: [num_classes]
Número de parámetros en el modelo BERT: [bert_params]
```

3.3 Rendimiento:

```
Tiempo promedio de predicción del modelo Naive Bayes: [nb_prediction_time] segundos
```

3.4 Visualizaciones:

Se generaron tres gráficos de barras para visualizar:
- Tamaño de los modelos (MB)
- Escala de los modelos
- Rendimiento (comparando tiempo de predicción de Naive Bayes y tamaño de BERT)

4. Análisis

4.1 Comparación de Tamaños:
- El modelo BERT es significativamente más grande que el modelo Naive Bayes y los componentes auxiliares.
- El tamaño del modelo BERT refleja su complejidad y capacidad para capturar patrones lingüísticos sofisticados.
- Naive Bayes, junto con sus componentes, ofrece una solución mucho más ligera, ideal para aplicaciones con restricciones de recursos.

4.2 Escala de los Modelos:
- BERT tiene un número mucho mayor de parámetros en comparación con el tamaño del vocabulario y el número de clases.
- El gran número de parámetros de BERT le permite modelar relaciones complejas en el lenguaje, pero también aumenta el riesgo de sobreajuste en conjuntos de datos pequeños.
- El vocabulario del vectorizador para Naive Bayes, aunque más limitado, puede ser suficiente para muchas tareas de clasificación de texto.

4.3 Rendimiento:
- El tiempo de predicción de Naive Bayes es muy rápido, lo que lo hace ideal para aplicaciones en tiempo real o con grandes volúmenes de datos.
- Aunque no se midió directamente, se espera que BERT tenga un tiempo de predicción más largo debido a su complejidad, lo que podría ser un factor limitante en algunas aplicaciones.

5. Implementación del Dashboard

Para hacer que los modelos sean accesibles y fáciles de usar, se desarrolló un dashboard interactivo utilizando Streamlit. Este dashboard permite a los usuarios interactuar directamente con los modelos de análisis de sentimientos.

5.1 Características principales del dashboard:

a) Entrada de texto:
   - Los usuarios pueden ingresar texto en un área de texto de múltiples líneas.
   - El sistema puede procesar texto en inglés, español y portugués.

b) Análisis de sentimientos:
   - Al hacer clic en el botón "Analizar", el sistema procesa el texto ingresado.
   - Se realizan predicciones utilizando tanto el modelo Naive Bayes como el modelo BERT.
   - Los resultados se muestran para cada línea de texto ingresada.

c) Visualización de resultados:
   - Los resultados se presentan de forma textual para cada línea.
   - Se incluye una gráfica de barras que resume los resultados de ambos modelos.

d) Información adicional:
   - Una barra lateral proporciona información sobre el proyecto.
   - Se muestran métricas de precisión para ambos modelos.
   - Se incluyen instrucciones de uso para guiar a los usuarios.

5.2 Funcionamiento del dashboard:

a) Carga de modelos:
   - Los modelos (Naive Bayes y BERT) se cargan al inicio utilizando la función `@st.cache_resource`.
   - Esto optimiza el rendimiento al evitar recargar los modelos en cada interacción.

b) Preprocesamiento de texto:
   - Se implementa una función de preprocesamiento que incluye:
     * Detección de idioma
     * Tokenización
     * Eliminación de stopwords
     * Generación de n-gramas

c) Predicción de sentimientos:
   - Se realiza la predicción para cada línea de texto ingresada.
   - Se utilizan tanto el modelo Naive Bayes como el BERT para cada predicción.

d) Visualización:
   - Los resultados se muestran tanto en formato de texto como en una gráfica de barras.
   - La gráfica proporciona una comparación visual rápida de las predicciones de ambos modelos.

5.3 Ventajas del dashboard:

- Accesibilidad: Permite a usuarios sin conocimientos técnicos interactuar con modelos avanzados de NLP.
- Comparación directa: Muestra las predicciones de dos modelos diferentes lado a lado.
- Multilingüe: Capaz de procesar texto en múltiples idiomas sin necesidad de configuración adicional.
- Visualización intuitiva: La gráfica de barras ofrece una comprensión rápida de los resultados.

5.4 Áreas de mejora potencial:

- Implementar la medición del tiempo de predicción para el modelo BERT.
- Añadir opciones para que los usuarios seleccionen diferentes modelos o ajusten parámetros.
- Incorporar funcionalidades para el análisis de textos más largos o conjuntos de datos completos.

6. Conclusiones y Trabajo Futuro

-  Realizar una comparación directa de la precisión de clasificación entre Naive Bayes y BERT en varios conjuntos de datos.
- Medir el tiempo de inferencia de BERT para una comparación más completa del rendimiento.
- Explorar técnicas de compresión de modelos para reducir el tamaño de BERT sin sacrificar significativamente el rendimiento.
- El dashboard desarrollado demuestra la viabilidad de implementar modelos de NLP complejos en una interfaz fácil de usar. Esto abre posibilidades para aplicaciones prácticas en diversos campos, desde el análisis de redes sociales hasta el servicio al cliente automatizado.



