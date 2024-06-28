import streamlit as st
import joblib
import torch
import pandas as pd
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer
from langdetect import detect

@st.cache_resource
def load_models():
    nb_model = joblib.load('nb_model.joblib')
    vectorizer = joblib.load('vectorizer.joblib')
    
    # Cargar el estado del modelo BERT
    state_dict = torch.load('bert_model.pth', map_location=torch.device('cpu'))
    
    # Determinar el número de clases basado en el estado guardado
    num_labels = state_dict['classifier.out_proj.weight'].size(0)
    
    # Inicializar el modelo BERT con el número correcto de etiquetas
    bert_model = XLMRobertaForSequenceClassification.from_pretrained('xlm-roberta-base', num_labels=num_labels)
    
    # Eliminar la clave inesperada
    if 'roberta.embeddings.position_ids' in state_dict:
        del state_dict['roberta.embeddings.position_ids']
    
    # Cargar el estado del modelo, ignorando las claves que no coinciden
    bert_model.load_state_dict(state_dict, strict=False)
    
    tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')
    label_encoder = joblib.load('label_encoder.joblib')
    
    return nb_model, vectorizer, bert_model, tokenizer, label_encoder

# Cargar los modelos al inicio del script
nb_model, vectorizer, bert_model, tokenizer, label_encoder = load_models()

def predict_sentiment(text):
    # Predicción con Naive Bayes
    text_vectorized = vectorizer.transform([text])
    nb_prediction = nb_model.predict(text_vectorized)
    nb_sentiment = label_encoder.inverse_transform(nb_prediction)[0]
    
    # Predicción con BERT
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    bert_prediction = torch.argmax(outputs.logits, dim=-1).item()
    bert_sentiment = label_encoder.inverse_transform([bert_prediction])[0]
    
    return bert_sentiment, nb_sentiment

# Interfaz de Streamlit
st.title("Análisis de Sentimientos")

# Entrada de texto
text_input = st.text_area("Ingrese los textos a analizar (uno por línea):")

if st.button("Analizar Sentimientos"):
    if text_input:
        texts = text_input.split('\n')
        for text in texts:
            if text.strip():  # Ignorar líneas vacías
                try:
                    # Detectar el idioma
                    lang = detect(text)
                    
                    # Realizar predicción
                    bert_sentiment, nb_sentiment = predict_sentiment(text)
                    
                    # Mostrar resultados
                    st.write(f"Texto: {text}")
                    st.write(f"Idioma detectado: {lang}")
                    st.write(f"Predicción BERT: {bert_sentiment}")
                    st.write(f"Predicción Naive Bayes: {nb_sentiment}")
                    
                    # Visualización
                    sentiments = ['Negativo', 'Neutro', 'Positivo']
                    chart_data = pd.DataFrame({
                        'Sentimiento': sentiments,
                        'BERT': [1 if bert_sentiment == s else 0 for s in sentiments],
                        'Naive Bayes': [1 if nb_sentiment == s else 0 for s in sentiments]
                    })
                    
                    st.bar_chart(chart_data.set_index('Sentimiento'))
                    st.write("---")  # Separador entre resultados
                    
                except Exception as e:
                    st.error(f"Error al procesar el texto '{text}': {str(e)}")
    else:
        st.warning("Por favor, ingrese textos para analizar.")

# Agregar información sobre el proyecto
st.sidebar.title("Acerca del Proyecto")
st.sidebar.info(
    "Este es un proyecto de análisis de sentimientos que utiliza "
    "modelos de aprendizaje profundo (BERT) y aprendizaje automático clásico (Naive Bayes) "
    "para clasificar el sentimiento de un texto dado en positivo, negativo o neutro. "
    "Puede analizar texto en español, inglés y portugués."
)

# Métricas del modelo (puedes ajustar estos valores según tus resultados reales)
st.sidebar.title("Métricas del Modelo")
st.sidebar.metric(label="Precisión BERT", value="88%")
st.sidebar.metric(label="Precisión Naive Bayes", value="85%")

# Instrucciones de uso
st.sidebar.title("Instrucciones de Uso")
st.sidebar.info(
    "1. Ingrese uno o más textos en el área de texto, uno por línea.\n"
    "2. Haga clic en 'Analizar Sentimientos'.\n"
    "3. Los resultados se mostrarán para cada texto, incluyendo:\n"
    "   - El idioma detectado\n"
    "   - La predicción de sentimiento de BERT\n"
    "   - La predicción de sentimiento de Naive Bayes\n"
    "   - Una visualización gráfica de los resultados"
)
