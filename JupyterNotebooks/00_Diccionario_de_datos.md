# Diccionario de datos para el proyecto

* **australian_user_reviews.json** es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, además de datos adicionales como si recomiendan o no ese juego, emoticones de gracioso y estadísticas de si el comentario fué útil o no para otros usuarios. También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.

Las variables que contiene son:

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

* **australian_users_items.json** es un dataset que contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.

Las variables que contiene son:  
    * **user_id**: contiene un identificador único del usuario.  
    * **items_count**: contiene un número entero que indica la cantidad de juegos que ha consumido el usuario.  
    * **steam_id**: es un número único para la plataforma.  
    * **user_url**: es la url del perfil del usuario  
    * **items**: contiene una lista de uno o mas diccionarios de los items que consume cada usuario.   Cada diccionario tiene las siguientes claves:  
    * **item_id**: es el identificados del item, es decir, del juego.  
    * **item_name**: es el nombre del contenido que consume, es decir, del juego.  
    * **playtime_forever**: es el tiempo acumulado que un usuario jugó a un juego.  
    * **playtime_2weeks**: es el tiempo acumulado que un usuario jugó a un juego en las últimas dos semanas.  

* **output_steam_games.json** es un dataset que contiene datos relacionados con los juegos en sí, como los título, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

Las variables que contiene son:  
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