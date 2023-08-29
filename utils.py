import pandas as pd
from textblob import TextBlob

def verificar_tipo_datos(df):
    '''
    Verifica el tipo de dato contenido en cada columna de un dataframe.
    Tiene como parámetro el dataframe a evaluar y devuelve un resumen de el/los tipos de datos, 
    porcentaje de nulos y no nulos y cantidad de nulos por cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": [], "nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict["nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def analyze_sentiment(review):
    if review is None:
        return 1  # Neutral if review is None
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:  # Para negativos
        return 0  # Malo si el sentimiento es negativo
    elif polarity > 0.2:  # Para positivos
        return 2  # Positivo si el sentimiento es positivo
    else:
        return 1  # Neutral en otros casos