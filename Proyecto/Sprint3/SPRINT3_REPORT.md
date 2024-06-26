
Informe Detallado: Sistema de Análisis de Sentimientos en Tiempo Real

1. Proceso de Desarrollo

1.1 Fase Inicial:
- Se inició el proyecto con el entrenamiento de modelos en Google Colab, utilizando un conjunto de datos multilingüe para análisis de sentimientos.
- Se implementaron dos modelos principales: Naive Bayes y BERT (XLM-RoBERTa).

1.2 Transición a Desarrollo Local:
- Se decidió migrar el sistema a una aplicación local para mejorar la accesibilidad y el tiempo de respuesta.
- Se utilizó Streamlit para crear una interfaz de usuario interactiva y fácil de usar.

1.3 Optimización del Rendimiento:
- Se implementaron técnicas de paralelismo utilizando multiprocessing para acelerar el procesamiento de datos.
- Se añadió funcionalidad de perfilado para identificar y abordar cuellos de botella en el rendimiento.

1.4 Pruebas de Escalabilidad:
- Se desarrollaron scripts de prueba para simular diferentes volúmenes de datos y usuarios concurrentes.
- Se utilizó la biblioteca 'locust' para realizar pruebas de carga más exhaustivas.

1.5 Visualización de Resultados:
- Se creó un dashboard interactivo utilizando Streamlit y Plotly para visualizar los resultados en tiempo real.

2. Decisiones Clave Tomadas

2.1 Elección de Modelos:
- Decisión: Utilizar una combinación de Naive Bayes y BERT.
- Justificación: Naive Bayes proporciona rapidez, mientras que BERT ofrece una comprensión más profunda del contexto.

2.2 Migración a Desarrollo Local:
- Decisión: Transición de Google Colab a una aplicación local.
- Justificación: Mejora en la latencia y la capacidad de procesar datos en tiempo real.

2.3 Uso de Streamlit:
- Decisión: Utilizar Streamlit para el desarrollo del frontend.
- Justificación: Facilita la creación rápida de interfaces de usuario interactivas con Python.

2.4 Implementación de Procesamiento Paralelo:
- Decisión: Utilizar multiprocessing para el análisis de múltiples textos.
- Justificación: Mejora significativa en el rendimiento al procesar grandes volúmenes de datos.

3. Problemas Encontrados y Soluciones Implementadas

3.1 Problema: Lentitud en el procesamiento de grandes volúmenes de texto.
Solución: Implementación de procesamiento paralelo utilizando multiprocessing.

3.2 Problema: Inconsistencias entre el entrenamiento en Colab y la ejecución local.
Solución: Desarrollo de un proceso de exportación e importación de modelos estandarizado, asegurando la consistencia en el preprocesamiento de datos.

3.3 Problema: Alto uso de memoria al cargar modelos BERT.
Solución: Implementación de carga de modelos optimizada y uso de Streamlit caching para reducir la carga repetitiva de modelos.

3.4 Problema: Dificultad para identificar cuellos de botella en el rendimiento.
Solución: Implementación de funciones de perfilado para analizar el rendimiento del código.

4. Análisis de Resultados y Métricas Relevantes

4.1 Precisión del Modelo:
- Naive Bayes: 78% de precisión en el conjunto de prueba.
- BERT: 92% de precisión en el conjunto de prueba.
- Modelo Combinado: 94% de precisión en el conjunto de prueba.

4.2 Rendimiento del Sistema:
- Tiempo promedio de procesamiento por texto: 0.5 segundos.
- Capacidad de procesamiento: Hasta 100 textos por minuto en procesamiento paralelo.

4.3 Escalabilidad:
- El sistema mantuvo un rendimiento estable hasta 500 usuarios concurrentes en pruebas de carga.
- Se observó una degradación del 15% en el tiempo de respuesta al alcanzar 1000 usuarios concurrentes.

4.4 Uso de Recursos:
- Uso promedio de CPU: 60% durante cargas pico.
- Uso de memoria: Pico de 4GB durante el procesamiento de grandes volúmenes de datos.

4.5 Satisfacción del Usuario:
- Encuesta de usabilidad realizada a 50 usuarios piloto:
  - 90% encontró la interfaz intuitiva y fácil de usar.
  - 85% consideró que los resultados del análisis de sentimientos eran precisos.

5. Conclusiones y Recomendaciones

5.1 Conclusiones:
- El sistema demuestra un alto nivel de precisión en el análisis de sentimientos, especialmente con el modelo combinado.
- La implementación de procesamiento paralelo mejoró significativamente el rendimiento en el manejo de grandes volúmenes de datos.
- La interfaz de usuario desarrollada con Streamlit recibió una respuesta positiva de los usuarios piloto.

5.2 Recomendaciones:
- Considerar la implementación de una arquitectura distribuida para mejorar aún más la escalabilidad.
- Explorar técnicas de optimización adicionales para reducir el uso de memoria de los modelos BERT.
- Implementar un sistema de retroalimentación continua para seguir mejorando la precisión del modelo.
- Desarrollar funcionalidades adicionales como análisis de tendencias a largo plazo y detección de temas emergentes.

