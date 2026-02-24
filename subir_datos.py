import pandas as pd
from pymongo import MongoClient

# Leer el archivo CSV
df = pd.read_csv('ventas_ejemplo_550.csv')

# Convertir la columna 'fecha' a tipo Fecha (Datetime)
df['fecha'] = pd.to_datetime(df['fecha'])

# Convertir los datos a formato JSON
datos_json = df.to_dict(orient='records')

# Conexión a MongoDB Atlas
URI = "mongodb+srv://jaq23369_db_user:jz1XAaA96VZGTl1N@bd2j.qfg17ws.mongodb.net/?appName=BD2J"
cliente = MongoClient(URI)

# Seleccionar Base de Datos y Colección
db = cliente['Laboratorio04_DB'] 
coleccion = db['ventas_ejemplo']

# Inserción masiva (Bulkwrite)
try:
    coleccion.insert_many(datos_json)
    print(f"Se insertaron {len(datos_json)} registros en MongoDB Atlas.")
except Exception as e:
    print("Ocurrió un error:", e)