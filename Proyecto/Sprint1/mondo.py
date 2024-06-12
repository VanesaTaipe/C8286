from pymongo import MongoClient
import pandas as pd

# Configurar la conexión a MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["twitter_db"]
collection = db["tweets"]

# Leer los datos desde el archivo CSV
tweets_df = pd.read_csv("tweets_sin_entrenamiento.csv")

# Convertir el DataFrame a una lista de diccionarios
tweets_data = tweets_df.to_dict(orient="records")

# Insertar los tweets en la colección de MongoDB
collection.insert_many(tweets_data)

print(f"Se han importado {len(tweets_data)} tweets desde el archivo CSV a MongoDB.")
