import streamlit as st
import numpy as np
import joblib
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
from langdetect import detect
import pandas as pd

# Descargar recursos de NLTK si no están disponibles
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

@st.cache_resource
def load_models():
    nb_model = joblib.load('nb_model.joblib')
    vectorizer = joblib.load('vectorizer.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
    
    bert_model = AutoModelForSequenceClassification.from_pretrained('xlm-roberta-base', num_labels=len(label_encoder.classes_))
    state_dict = torch.load('bert_model.pth', map_location=torch.device('cpu'))
    if 'roberta.embeddings.position_ids' in state_dict:
        del state_dict['roberta.embeddings.position_ids']
    bert_model.load_state_dict(state_dict, strict=False)
    
    bert_tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-base')
    
    return nb_model, vectorizer, bert_model, bert_tokenizer, label_encoder

nb_model, vectorizer, bert_model, bert_tokenizer, label_encoder = load_models()

def get_stopwords():
    languages = ['english', 'spanish', 'portuguese']
    return {lang: set(stopwords.words(lang)) for lang in languages}

STOP_WORDS = get_stopwords()

def preprocess_text_with_ngrams(text, n=2):
    try:
        lang = detect(text)
        if lang not in ['en', 'es', 'pt']:
            lang = 'en'
    except:
        lang = 'en'
    lang_map = {'en': 'english', 'es': 'spanish', 'pt': 'portuguese'}
    nltk_lang = lang_map[lang]
    tokens = word_tokenize(text.lower(), language=nltk_lang)
    tokens = [token for token in tokens if token.isalpha() and token not in STOP_WORDS[nltk_lang]]
    n_grams = list(ngrams(tokens, n))
    n_gram_strings = ['_'.join(gram) for gram in n_grams]
    all_features = tokens + n_gram_strings
    return ' '.join(all_features)

def predict_sentiment(text):
    lines = text.split('\n')
    nb_sentiments = []
    bert_sentiments = []
    for line in lines:
        preprocessed_text = preprocess_text_with_ngrams(line)
        
        # Predicción con Naive Bayes
        nb_prediction = nb_model.predict(vectorizer.transform([preprocessed_text]))[0]
        nb_sentiment = label_encoder.inverse_transform([nb_prediction])[0]
        nb_sentiments.append(nb_sentiment)
        
        # Predicción con BERT
        bert_inputs = bert_tokenizer(line, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            bert_output = bert_model(**bert_inputs).logits
        bert_prediction = torch.argmax(bert_output, dim=1).item()
        bert_sentiment = label_encoder.inverse_transform([bert_prediction])[0]
        bert_sentiments.append(bert_sentiment)
    
    return nb_sentiments, bert_sentiments

st.title('Análisis de Sentimientos')
st.write('Ingresa un texto y obtén las predicciones de Naive Bayes y BERT:')
text_input = st.text_area('Texto', height=200)

if st.button('Analizar'):
    if text_input:
        nb_sentiments, bert_sentiments = predict_sentiment(text_input)
        for i, (nb_sentiment, bert_sentiment) in enumerate(zip(nb_sentiments, bert_sentiments)):
            st.write(f'Línea {i+1}:')
            st.write(f'Predicción de Naive Bayes: {nb_sentiment}')
            st.write(f'Predicción de BERT: {bert_sentiment}')
        
        # Crear DataFrame de resultados
        chart_data = pd.DataFrame({'Sentimiento': nb_sentiments + bert_sentiments})
        chart_data['Modelo'] = ['Naive Bayes'] * len(nb_sentiments) + ['BERT'] * len(bert_sentiments)
        
        # Mostrar gráfica de barras
        st.write("---")
        st.subheader("Resumen de los Resultados")
        st.bar_chart(chart_data.set_index('Sentimiento'), height=400)
    else:
        st.write('Por favor, ingresa un texto para analizar.')

st.sidebar.title("Acerca del Proyecto")
st.sidebar.info(
    "Este es un proyecto de análisis de sentimientos que utiliza "
    "modelos de aprendizaje profundo (BERT) y aprendizaje automático clásico (Naive Bayes) "
    "para clasificar el sentimiento de un texto dado en positivo, negativo o neutro. "
    "Puede analizar texto en español, inglés y portugués."
)

st.sidebar.title("Métricas del Modelo")
st.sidebar.metric(label="Precisión BERT", value="88%")
st.sidebar.metric(label="Precisión Naive Bayes", value="85%")

st.sidebar.title("Instrucciones de Uso")
st.sidebar.info(
    "1. Ingrese uno o más textos en el área de texto.\n"
    "2. Haga clic en 'Analizar Sentimientos'.\n"
    "3. Los resultados se mostrarán para cada línea de texto, incluyendo:\n"
    "   - La predicción de sentimiento de BERT\n"
    "   - La predicción de sentimiento de Naive Bayes\n"
    "4. Se mostrará una gráfica de barras con un resumen de los resultados."
)
