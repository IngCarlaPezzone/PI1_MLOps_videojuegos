# Importaciones
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import pandas as pd
import pandas as pd
import operator
from api_functions import presentacion

# Se instancia la aplicación
app = FastAPI()


# Dataframes a usar
# df_reviews = pd.read_csv('data/df_reviews_unido.csv')
# df_gastos_items = pd.read_csv('data/df_gastos_items_unido.csv')
# df_genre_ranking = pd.read_csv('data/df_genre_ranking_unido.csv')
# df_playtime_forever = pd.read_csv('data/df_playtime_forever_unido.csv')
# df_items_developer = pd.read_csv('data/df_items_developer_unido.csv')
# df = pd.read_csv('data/df_merged.csv')

user_sim_df = pd.read_parquet('data_render/user_sim_df.parquet')
df_reviews = pd.read_parquet('data_render/df_reviews.parquet')
df_gastos_items = pd.read_parquet('data_render/df_gastos_items.parquet')
df_genre_ranking = pd.read_parquet('data_render/df_genre_ranking.parquet')
df_playtime_forever = pd.read_parquet('data_render/df_playtime_forever.parquet')
df_items_developer = pd.read_parquet('data_render/df_items_developer.parquet')
df = pd.read_parquet('data_render/df.parquet')
piv_norm = pd.read_parquet('data_render/piv_norm.parquet')

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.
    '''
    return presentacion()

@app.get(path = '/userdata',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el user_id en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la cantidad de dinero gastado por el usuario, el porcentaje de recomendación que realiza el usuario y cantidad de items que tiene el mismo.
                        </font>
                        """,
         tags=["Consultas Generales"])
def userdata(user_id: str = Query(..., 
                                description="Identificador único del usuario", 
                                example="EchoXSilence")):
    '''
    Esta función devuelve información sobre un usuario según su 'user_id'.
         
    Args:
        user_id (str): Identificador único del usuario.
    
    Returns:
        dict: Un diccionario que contiene información sobre el usuario.
            - 'cantidad_dinero' (int): Cantidad de dinero gastado por el usuario.
            - 'porcentaje_recomendacion' (float): Porcentaje de recomendaciones realizadas por el usuario.
            - 'total_items' (int): Cantidad de items que tiene el usuario.
    '''
    # Filtra por el usuario de interés
    usuario = df_reviews[df_reviews['user_id'] == user_id]
    # Calcula la cantidad de dinero gastado para el usuario de interés
    cantidad_dinero = df_gastos_items[df_gastos_items['user_id']== user_id]['price'].iloc[0]
    # Busca el count_item para el usuario de interés    
    count_items = df_gastos_items[df_gastos_items['user_id']== user_id]['items_count'].iloc[0]
    
    # Calcula el total de recomendaciones realizadas por el usuario de interés
    total_recomendaciones = usuario['reviews_recommend'].sum()
    # Calcula el total de reviews realizada por todos los usuarios
    total_reviews = len(df_reviews['user_id'].unique())
    # Calcula el porcentaje de recomendaciones realizadas por el usuario de interés
    porcentaje_recomendaciones = (total_recomendaciones / total_reviews) * 100
    
    return {
        'cantidad_dinero': int(cantidad_dinero),
        'porcentaje_recomendacion': round(float(porcentaje_recomendaciones), 2),
        'total_items': int(count_items)
    }
    
    
@app.get(path = '/countreviews',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese las fechas de inicio y fin en formato YYYY-MM-DD en los box abajo.<br>
                        3. Scrollear a "Resposes" para ver el resultado de la clasificación.
                        </font>
                        """,
         tags=["Consultas Generales"])
def countreviews(fecha_inicio: str = Query(..., 
                                description="Fechas de inicio para filtar la información", 
                                example='2011-11-05'), 
                 fecha_fin: str = Query(..., 
                                description="Fechas de Fin para filtar la información", 
                                example='2012-12-24')):
    '''
    Esta función devuelve estadísticas sobre las reviews realizadas por los usuarios entre dos fechas.
         
    Args:
        fecha_inicio (str): Fecha de inicio para filtrar la información en formato YYYY-MM-DD.
        fecha_fin (str): Fecha de fin para filtrar la información en formato YYYY-MM-DD.
    
    Returns:
        dict: Un diccionario que contiene estadísticas de las reviews entre las fechas especificadas.
            - 'total_usuarios_reviews' (int): Cantidad de usuarios que realizaron reviews entre las fechas.
            - 'porcentaje_recomendaciones' (float): Porcentaje de recomendaciones positivas (True) entre las reviews realizadas.
    '''
    # Filtra el dataframe entre las fechas de interés
    user_data_entre_fechas = df_reviews[(df_reviews['reviews_date'] >= fecha_inicio) & (df_reviews['reviews_date'] <= fecha_fin)]
    # Calcula la cantidad de usuarios que dieron reviews entre las fechas de interés
    total_usuarios = user_data_entre_fechas['user_id'].nunique()
    # Calcula el total de recomendaciones entre las fechas de interes (True + False)
    total_recomendacion = len(user_data_entre_fechas)
    # Calcula la cantidad de recomendaciones positivas que que hicieron entre las fechas de interés
    total_recomendaciones_True = user_data_entre_fechas['reviews_recommend'].sum()
    # Calcula el porcentaje de recomendación realizadas entre el total de usuarios
    porcentaje_recomendaciones = (total_recomendaciones_True / total_recomendacion) * 100
    
    return {
        'total_usuarios_reviews': int(total_usuarios),
        'porcentaje_recomendaciones': round(float(porcentaje_recomendaciones),2)
    }


@app.get(path = '/genre',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el género del juego en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la posición del ranking donde se encuentra.
                        </font>
                        """,
         tags=["Consultas Generales"])
def genre(genero: str = Query(..., 
                            description="Género del videojuego", 
                            example='Simulation')):
    '''
    Esta función devuelve la posición de un género de videojuego en un ranking basado en la cantidad de horas jugadas.
         
    Args:
        genero (str): Género del videojuego.
    
    Returns:
        dict: Un diccionario que contiene la posición del género en el ranking.
            - 'rank' (int): Posición del género en el ranking basado en las horas jugadas.
    '''
    # Busca el ranking para el género de interés
    rank = df_genre_ranking[df_genre_ranking['genres'] == genero]['ranking'].iloc[0]
    return {
        'rank': int(rank)
    }


@app.get(path = '/userforgenre',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el género en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver Top 5 de usuarios con más horas de juego en el género dado, con su URL y user_id.
                        </font>
                        """,
         tags=["Consultas Generales"])
def userforgenre(genero: str = Query(..., 
                            description="Género del videojuego", 
                            example='Simulation')):
    '''
    Esta función devuelve el top 5 de usuarios con más horas de juego en un género específico, junto con su URL de perfil y ID de usuario.
         
    Args:
        genero (str): Género del videojuego.
    
    Returns:
        dict: Un diccionario que contiene el top 5 de usuarios con más horas de juego en el género dado, junto con su URL de perfil y ID de usuario.
            - 'user_id' (str): ID del usuario.
            - 'user_url' (str): URL del perfil del usuario.
    '''
    # Filtra el dataframe por el género de interés
    data_por_genero = df_playtime_forever[df_playtime_forever['genres'] == genero]
    # Agrupa el dataframe filtrado por usuario y suma la cantidad de horas
    top_users = data_por_genero.groupby(['user_url', 'user_id'])['playtime_horas'].sum().nlargest(5).reset_index()
    
    # Se hace un diccionario vacío para guardar los datos que se necesitan
    top_users_dict = {}
    for index, row in top_users.iterrows():
        # User info recorre cada fila del top 5 y lo guarda en el diccionario
        user_info = {
            'user_id': row['user_id'],
            'user_url': row['user_url']
        }
        top_users_dict[index + 1] = user_info
    
    return top_users_dict

@app.get(path = '/developer',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del desarrollador en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la cantidad de items y porcentaje de contenido Free por año de ese desarrollador.
                        </font>
                        """,
         tags=["Consultas Generales"])
def developer(desarrollador: str = Query(..., 
                            description="Desarrollador del videojuego", 
                            example='Valve')):
    '''
    Esta función devuelve información sobre una empresa desarrolladora de videojuegos.
         
    Args:
        desarrollador (str): Nombre del desarrollador de videojuegos.
    
    Returns:
        dict: Un diccionario que contiene información sobre la empresa desarrolladora.
            - 'cantidad_por_año' (dict): Cantidad de items desarrollados por año.
            - 'porcentaje_gratis_por_año' (dict): Porcentaje de contenido gratuito por año según la empresa desarrolladora.
    '''
    # Filtra el dataframe por desarrollador de interés
    data_filtrada = df_items_developer[df_items_developer['developer'] == desarrollador]
    # Calcula la cantidad de items por año
    cantidad_por_año = data_filtrada.groupby('release_anio')['item_id'].count()
    # Calcula la cantidad de elementos gratis por año
    cantidad_gratis_por_año = data_filtrada[data_filtrada['price'] == 0.0].groupby('release_anio')['item_id'].count()
    # Calcula el porcentaje de elementos gratis por año
    porcentaje_gratis_por_año = (cantidad_gratis_por_año / cantidad_por_año * 100).fillna(0).astype(int)

    result_dict = {
        'cantidad_por_año': cantidad_por_año.to_dict(),
        'porcentaje_gratis_por_año': porcentaje_gratis_por_año.to_dict()
    }
    
    return result_dict


@app.get('/sentiment_analysis',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el año en box abajo.<br>
                    3. Scrollear a "Resposes" para ver la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
                    </font>
                    """,
         tags=["Consultas Generales"])
def sentiment_analysis(anio: str = Query(..., 
                                         description="Año para filtrar los sentimientos de las reseñas", 
                                         example="2009")):
    '''
    Realiza un análisis de sentimiento en base al año ingresado.
    
    Args:
        anio (str): El año para filtrar las reseñas.
    
    Returns:
        dict: Un diccionario con el recuento de categorías de sentimiento.
    '''
    # Filtra las reseñas del año específico
    anio_reviews = df_reviews[df_reviews['release_anio'] == anio]
    
    # Inicializa un diccionario para contar las categorías de sentimiento
    sentiment_counts = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    
    # Itera a través de las reseñas del año seleccionado
    for _, row in anio_reviews.iterrows():
        sentiment = row['sentiment_analysis']
        sentiment_category = ''
        
        # Maneja valores no numéricos en la columna 'release_anio'
        try:
            # Asigna la categoría de sentimiento correspondiente
            if sentiment == 0:
                sentiment_category = 'Negative'
            elif sentiment == 1:
                sentiment_category = 'Neutral'
            elif sentiment == 2:
                sentiment_category = 'Positive'
            
            # Incrementa el contador correspondiente en el diccionario
            sentiment_counts[sentiment_category] += 1
        except ValueError:
            # Maneja el valor no numérico (como 'Sin Dato Disponible')
            pass
    
    return sentiment_counts


# Cargar la matriz desde el archivo CSV
item_sim_df = pd.read_csv('data/item_sim_df.csv')

@app.get('/recomendacion_usuario',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el id del usuario en box abajo.<br>
                    3. Scrollear a "Resposes" para ver los juegos recomendados para ese usuario.
                    </font>
                    """,
         tags=["Recomendación"])
def top_game(game):
    count = 1
    similar_games = []
    for item in item_sim_df.sort_values(by=game, ascending=False).item_name[1:6]:
        similar_games.append({count: item})
        count += 1
    return {'Similar games': similar_games}





@app.get('/recomendacion_usuario2',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el id del usuario en box abajo.<br>
                    3. Scrollear a "Resposes" para ver los juegos recomendados para ese usuario.
                    </font>
                    """,
         tags=["Recomendación"])
def similar_user_recs(user):
    
    if user not in piv_norm.columns:
        return('No data available on user {}'.format(user))
    
    sim_users = user_sim_df.sort_values(by=user, ascending=False).user_id[1:11]
    best = []
    most_common = {}
    
    for i in sim_users:
        i = str(i)
        max_score = piv_norm.loc[:, i].max()
        best.append(piv_norm[piv_norm.loc[:, i]==max_score].item_name.tolist())
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    recomendaciones = {}  # Inicializa un diccionario vacío
    contador = 1  # Inicializa un contador en 1

    for juego, _ in sorted_list:
        if contador <= 5:  # Verifica si el contador es menor o igual a 5
            recomendaciones[contador] = juego  # Asigna el número de contador como clave y el juego como valor
            contador += 1  # Incrementa el contador
        else:
            break
    # print(recomendaciones)
    return recomendaciones 