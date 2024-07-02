import joblib
import torch
import pickle
import matplotlib.pyplot as plt
from transformers import XLMRobertaForSequenceClassification
import time

# Cargar los modelos
nb_model = joblib.load('nb_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')
label_encoder = joblib.load('label_encoder.joblib')

# Cargar el modelo BERT
bert_model = XLMRobertaForSequenceClassification.from_pretrained('xlm-roberta-base')
state_dict = torch.load('bert_model.pth', map_location=torch.device('cpu'))

# Eliminar la clave inesperada si existe
state_dict.pop('roberta.embeddings.position_ids', None)

# Ajustar el tamaño de la capa de clasificación si es necesario
if state_dict['classifier.out_proj.weight'].size(0) != bert_model.classifier.out_proj.weight.size(0):
    num_labels = bert_model.config.num_labels
    state_dict['classifier.out_proj.weight'] = state_dict['classifier.out_proj.weight'][:num_labels, :]
    state_dict['classifier.out_proj.bias'] = state_dict['classifier.out_proj.bias'][:num_labels]

# Cargar el estado del diccionario modificado
bert_model.load_state_dict(state_dict, strict=False)

# Función para obtener el tamaño en MB
def get_size_mb(obj):
    return len(pickle.dumps(obj)) / (1024 * 1024)

# Calcular tamaños
nb_size = get_size_mb(nb_model)
vectorizer_size = get_size_mb(vectorizer)
label_encoder_size = get_size_mb(label_encoder)
bert_size = sum(p.numel() for p in bert_model.parameters()) * 4 / (1024 * 1024)

# Calcular escala
vocab_size = len(vectorizer.vocabulary_)
num_classes = len(label_encoder.classes_)
bert_params = sum(p.numel() for p in bert_model.parameters())

# Calcular rendimiento (tiempo de predicción para Naive Bayes)
def measure_nb_prediction_time(model, vectorizer, n_samples=1000):
    dummy_text = "This is a dummy text for prediction"
    start_time = time.time()
    for _ in range(n_samples):
        model.predict(vectorizer.transform([dummy_text]))
    end_time = time.time()
    return (end_time - start_time) / n_samples

nb_prediction_time = measure_nb_prediction_time(nb_model, vectorizer)

# Imprimir resultados
print("Escala de los modelos:")
print(f"Tamaño del vocabulario del vectorizador: {vocab_size}")
print(f"Número de clases en el codificador de etiquetas: {num_classes}")
print(f"Número de parámetros en el modelo BERT: {bert_params}")
print("\nRendimiento:")
print(f"Tiempo promedio de predicción del modelo Naive Bayes: {nb_prediction_time:.5f} segundos")
print("\nTamaño de los modelos:")
print(f"Tamaño del modelo Naive Bayes: {nb_size:.2f} MB")
print(f"Tamaño del vectorizador: {vectorizer_size:.2f} MB")
print(f"Tamaño del codificador de etiquetas: {label_encoder_size:.2f} MB")
print(f"Tamaño del modelo BERT: {bert_size:.2f} MB")

# Función para crear y guardar gráficos
def create_bar_chart(data, labels, title, filename, log_scale=True):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, data)
    plt.title(title)
    plt.xlabel('Modelos/Componentes')
    plt.ylabel('Valor')
    if log_scale:
        plt.yscale('log')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:,.2f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Crear gráficos
create_bar_chart([nb_size, vectorizer_size, label_encoder_size, bert_size],
                 ['Naive Bayes', 'Vectorizador', 'Codificador de etiquetas', 'BERT'],
                 'Tamaño de los modelos (MB)', 'model_sizes.png')

create_bar_chart([vocab_size, num_classes, bert_params],
                 ['Vocabulario', 'Clases', 'Parámetros BERT'],
                 'Escala de los modelos', 'model_scale.png')

create_bar_chart([nb_prediction_time, bert_size],
                 ['Tiempo predicción NB (s)', 'Tamaño BERT (MB)'],
                 'Rendimiento', 'model_performance.png', log_scale=False)

print("Gráficos guardados como 'model_sizes.png', 'model_scale.png', y 'model_performance.png'")
