import tweepy
import pandas as pd

# Token de portador de la API v2 de Twitter
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN3DuAEAAAAAGsz9%2BLVd98excFv%2Ft2f2AVl5zu4%3Doy83NcfAscaSSV8uZxI29TTFflhFEpJW3vW6gf91SBNLYA58O0"


# Crear una instancia del cliente de la API v2
client = tweepy.Client(bearer_token=bearer_token)

# Palabras clave relacionadas con sentimientos positivos, negativos y neutros
positive_keywords = ["feliz", "alegre", "emocionado", "agradecido", "encantado", "maravilloso", "excelente", "increíble", "fantástico", "asombroso", "disfrutando", "amando", "sonriendo", "riendo", "impresionante", "hermoso", "grandioso", "éxito", "logro", "victoria", "triunfo", "bendecido", "afortunado", "suerte", "optimista", "positivo", "inspirado", "motivado", "entusiasmado"]
negative_keywords = ["triste", "enojado", "frustrado", "decepcionado", "molesto", "terrible", "pésimo", "horrible", "asqueroso", "odio", "aburrido", "cansado", "estresado", "ansioso", "preocupado", "miedo", "solitario", "deprimido", "desanimado", "desesperado", "angustiado", "doloroso", "desafortunado", "lamentable", "negativo"]
neutral_keywords = ["normal", "común", "regular", "promedio", "típico", "ordinario", "estándar", "indiferente", "neutro", "imparcial", "objetivo", "balanceado", "justo", "equitativo", "moderado", "aceptable", "pasable", "suficiente", "adecuado", "satisfactorio", "razonable", "esperado", "predecible", "rutinario"]

# Construir las consultas de búsqueda para cada categoría de sentimiento
positive_query = " OR ".join(positive_keywords)
negative_query = " OR ".join(negative_keywords)
neutral_query = " OR ".join(neutral_keywords)

# Número total de tweets a extraer por categoría
total_tweets_per_category =3009

# Lista para almacenar los tweets extraídos
tweets_data = []

try:
    # Realizar la búsqueda de tweets para cada categoría de sentimiento
    for sentiment, query in [("Positivo", positive_query), ("Negativo", negative_query), ("Neutro", neutral_query)]:
        # Calcular el número de solicitudes necesarias para obtener el total de tweets deseado
        num_requests = (total_tweets_per_category - 1) // 100 + 1
        
        # Realizar múltiples solicitudes para obtener el total de tweets deseado
        for i in range(num_requests):
            # Calcular el número de tweets a extraer en la solicitud actual
            max_results = min(100, total_tweets_per_category - i * 100)
            
            # Realizar la búsqueda de tweets
            tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["author_id", "created_at", "public_metrics", "source", "text"])
            
            # Extraer los atributos deseados de los tweets y asignar la etiqueta de sentimiento
            for tweet in tweets.data:
                tweet_data = {
                    "user_id": tweet.author_id,
                    "created_at": tweet.created_at,
                    "likes": tweet.public_metrics["like_count"],
                    "source": tweet.source,
                    "tweet": tweet.text
                    #"sentiment": sentiment----
                }
                tweets_data.append(tweet_data)
    
    # Convertir los datos a un DataFrame de pandas
    tweets_df = pd.DataFrame(tweets_data)
    
    # Guardar los datos en un archivo CSV
    tweets_df.to_csv("tweets_sin_entrenamiento.csv", index=False)
    
    print(f"Se han extraído y guardado {len(tweets_data)} tweets en el archivo CSV.")

except BaseException as e:
    print('Error en la extracción de tweets:', str(e))
