[Twitter API] --> [Servicio de Extracción en Tiempo Real]
                                |
                                v
[Fuentes de Texto Multilingüe] --> [Servicio de Preprocesamiento]
(Inglés, Español, Portugués)     - Detección de idioma (langdetect)
                                 - Tokenización específica (NLTK)
                                 - Eliminación de stopwords
                                 - Generación de bi-gramas
                                 - Limpieza, Normalización
                                |
                                v
                        [Base de datos]
                           (MongoDB)
                                |
                                v
                    [Vectorización de Texto]
                 - CountVectorizer con bi-gramas
                 - TfidfVectorizer (opcional)
                                |
                         _______|_______
                        |               |
                        v               v
                 [Modelo BERT]    [Modelo Naive Bayes]
                (XLM-RoBERTa)     (MultinomialNB)
                        |               |
                        |_______________|
                                |
                                v
                [Sistema de Paralelización]
         - Multiprocessing para tareas CPU-intensivas
         - Threading para operaciones I/O
                                |
                                v
                 [Análisis de Rendimiento]
              - Precisión, Recall, F1-score
              - Matrices de confusión
                                |
                                v
               [Dashboard de Visualización]
              - Resultados por idioma
              - Comparación de modelos

[Sistema de Monitoreo y Optimización]
- Profiling (cProfile)
- Monitoreo de recursos
---> Retroalimentación a todos los componentes
