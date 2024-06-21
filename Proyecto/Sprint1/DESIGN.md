graph TD
    A[Twitter API] --> B[Servicio de Extracción en Tiempo Real]
    C[Fuentes de Texto Multilingüe<br>Inglés, Español, Portugués] --> D[Servicio de Preprocesamiento]
    B --> D
    D --> |Detección de idioma langdetect<br>Tokenización específica NLTK<br>Eliminación de stopwords<br>Generación de bi-gramas<br>Limpieza, Normalización| E[Base de datos MongoDB]
    E --> F[Vectorización de Texto<br>CountVectorizer con bi-gramas<br>TfidfVectorizer opcional]
    F --> G[Modelo BERT XLM-RoBERTa]
    F --> H[Modelo Naive Bayes MultinomialNB]
    G --> I[Sistema de Paralelización]
    H --> I
    I --> |Multiprocessing para tareas CPU-intensivas<br>Threading para operaciones I/O| J[Análisis de Rendimiento]
    J --> |Precisión, Recall, F1-score<br>Matrices de confusión| K[Dashboard de Visualización]
    K --> |Resultados por idioma<br>Comparación de modelos| L[Sistema de Monitoreo y Optimización]
    L --> |Profiling cProfile<br>Monitoreo de recursos| M[Retroalimentación a todos los componentes]
    M --> A
    M --> B
    M --> C
    M --> D
    M --> E
    M --> F
    M --> G
    M --> H
    M --> I
    M --> J
    M --> K
