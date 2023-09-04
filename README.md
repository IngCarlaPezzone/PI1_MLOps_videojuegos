# Prueba de concepto para proyecto de Steam

## Introducción

Este proyecto simula el rol  de un MLOps Engineer, es decir, la combinación de un Data Engineer y Data Scientist, para la plataforma multinacional de videojuegos Steam. Para su desarrollo, se entregan unos datos y se solicita un Producto Mínimo Viable que muestre una API deployada en un servicio en la nube y la aplicación de dos modelos de Machine Learning, por una lado, un análisis de sentimientos sobre los comentarios de los usuarios de los juegos y, por otro lado, la recomendación de juegos a partir de dar el nombre de un juego y/o a partir de los gustos de un usuario en particular.

## Datos

Para este proyecto se proporcionaron tres archivos JSON:

* <span style="color: navy; font-weight: bold;">australian_user_reviews.json.</span> es un dataset que contiene:
    * **user_id**: es un identificador único para el usuario.
    * **user_url**: es la url del perfil del usuario en streamcommunity.
    * **reviews**: contiene una lista de diccionarios. Para cada usuario se tiene uno o mas diccionario con el review. Cada diccionario contiene:
        * **funny**: indica si alguien puso emoticón de gracioso al review.
        * **posted**: es la fecha de posteo del review en formato Posted April 21, 2011.
        * **last_edited**: es la fecha de la última edición.
        * **item_id**: es el identificador único del item, es decir, del juego.
        * **helpful**: es la estadística donde otros usuarios indican si fue útil la información.
        * **recommend**: es un booleano que indica si el usuario recomienda o no el juego.
        * **review**: es una sentencia string con los comentarios sobre el juego.

* <span style="color: navy; font-weight: bold;">australian_users_items.json.</span> es un dataset que contiene:
    * **user_id**: contiene un identificador único del usuario.
    * **items_count**: contiene un número entero que indica la cantidad de juegos que ha consumido el usuario.
    * **steam_id**: es un número único para la plataforma.
    * **user_url**: es la url del perfil del usuario
    * **items**: contiene una lista de uno o mas diccionarios de los items que consume cada usuario. Cada diccionario tiene las siguientes claves:
    * **item_id**: es el identificados del item, es decir, del juego.
    * **item_name**: es el nombre del contenido que consume, es decir, del juego.
    * **playtime_forever**: es el tiempo acumulado que un usuario jugó a un juego.
    * **playtime_2weeks**: es el tiempo acumulado que un usuario jugó a un juego en las últimas dos semanas.

* <span style="color: navy; font-weight: bold;">output_steam_games.json.</span> es un dataset que contiene:
    * **publisher**: es la empresa publicadora del contenido.
    * **genres**: es el género del item, es decir, del juego. Esta formado por una lista de uno o mas géneros por registro.
    * **app_name**: es el nombre del item, es decir, del juego.
    * **title**: es el título del item.
    * **url**: es la url del juego.
    * **release_date**: es la fecha de lanzamiento del item en formato 2018-01-04.
    * **tags**: es la etiqueta del contenido. Esta formado por una lista de uno o mas etiquetas por registro.
    * **reviews_url**: es la url donde se encuentra el review de ese juego.
    * **specs**: son especificaciones de cada item. Es una lista con uno o mas string con las especificaciones.
    * **price**: es el precio del item.
    * **early_access**: indica el acceso temprano con un True/False.
    * **id**: es el identificador único del contenido.
    * **developer**: es el desarrollador del contenido.


Proyecto Individual sobre se hace un MVP para recomendar un videojuego.  
🚧🚧🚧 En construcción... 🚧🚧🚧
