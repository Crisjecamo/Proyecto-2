#!/usr/bin/env python
# coding: utf-8

# # Déjame escuchar la música

# <div class="alert alert-block alert-success">
# <b>Review General. (Iteración 1) </b> <a class="tocSkip"></a>
# 
# Cristopher, quería tomarme este tiempo al inicio de tu proyecto para comentarte mis apreciaciones generales de esta iteración de tu entrega.
# 
# Siempre me gusta comenzar dando la bienvenida al mundo de los datos a los estudiantes, te deseo lo mejor y espero que consigas lograr tus objetivos. Personalmente me gusta brindar el siguiente consejo, "Está bien equivocarse, es normal y es lo mejor que te puede pasar. Aprendemos de los errores y eso te hará mejor programador ya que podrás descubrir cosas a medida que avances y son estas cosas las que te darán esa experiencia para ser un gran cientifico de datos."
#     
# Ahora si yendo a esta notebook. Quería felicitarte Cristopher porque has logrado resolver todos los problemas que se presentaron, a la vez has tenido un gran manejo de las herramientas sobre el proceso y tu conclusión demuestra tu comprensión sobre el trabajo.
# 
# Tu trabajo está en condiciones de ser aprobado, te felicito nuevamente! Éxitos en tu camino dentro del mundo de los datos!
# 
# Saludos!

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[1]:


# Importar pandas
import pandas as pd


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[2]:


# Leer el archivo y almacenarlo en df
df = pd.read_csv('/datasets/music_project_en.csv')


# Muestra las 10 primeras filas de la tabla:

# In[3]:


# Obtener las 10 primeras filas de la tabla df
print(df.head(10))


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[4]:


# Obtener la información general sobre nuestros datos
print(df.info())


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Bien hecho, muy bien aplicados los métodos para obtener información! <div>

# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.ID
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.= el 'userID' aparte de que contiene mayusculas y minusculas no esta separado con un guion bajo de la siguiente manera 'user_id' y 'City' no esta correcto, esta incorrecto tiene espacios = '  City  '. 
# 
# 
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente descubrimiento Cristopher y ademas muy bien justificado!

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# 
# R= tenemos solo datos object, no se visualizan datos int64, float64 o bool, las filas simplemente almacenan datos object, sobre que dia y hora exacta han reproducido canciones en cada estado.
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`
# 
# R= a simple vista podemos deducir que con los datos que nos han proporcionado si podemos llegar a proporcionar respuestas a nuestra hipotesis. Ya que poseemos datos como el dia, la hora, y la ciudad en donde se esta reproduciendo cada cancion por cada usuario, por lo cual son suficientes para lograrlo.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# 
# R= pude percatarme de que existen valores nulos o ausentes en las columnas 'Track' - 63736, 'artist' - 57512, y 'genre' - 63881 ya que el numero total de filas en nuestra tabla es de 65079.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelentes observaciones Cristopher. Sigamos!

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[5]:


# Muestra los nombres de las columnas
print(df.columns)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Muy bien! Has aplicado correctamente el método .columns </div>

# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[6]:


# Bucle en los encabezados poniendo todo en minúsculas
new_col_names = [] #en esta nueva lista se colocaran los nuevos nombres en minuscula de las columnas.   

for old_names in df.columns: #se crea el bucle for para iterar sobre todos los encabezados de las columnas.
    names_lower = old_names.lower() #luego se le da la orden de colocar todos los encabezados de las columnas en minuscula.
    new_col_names.append(names_lower) #se guarda el resultado en la nueva lista new_col_names.
    
df.columns = new_col_names #por ultimo se le asignan los nuevos encabezados de las columnas a la tabla df con df.columns
print(df.columns) #se imprime el nuevo resultado de los nombres en las columnas, cual se puede apreciar que ya contiene los nombres de las columnas en minuscula.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Aquí lo has resuelto muy bien! Felicitaciones Cristopher!

# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[7]:


# Bucle en los encabezados eliminando los espacios
new_col_names = [] #en esta nueva lista se colocaran los nuevos nombres en minuscula de las columnas

for old_names in df.columns: #se crea el bucle for para iterar sobre todos los encabezados de las columnas.
    names_strip = old_names.strip() #luego se le da la orden de quitar todos los espacios al principio y al final de cada encabezado de lacolumna. .
    new_col_names.append(names_strip) #se guarda el resultado en la nueva lista new_col_names.
    
df.columns = new_col_names #por ultimo se le asignan los nuevos encabezados de las columnas a la tabla df con df.columns
print(df.columns) #se imprime el nuevo resultado de los nombres en las columnas, cual se puede apreciar que ya contiene los nombres de las columnas sin espacios al principio y al final.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Nuevamente bien hecho, buena implementación del loop, del método strip y del cambio en las columnas!

# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[8]:


# Cambiar el nombre de la columna "userid"
rename_userid ={         #se crea un diccionario con los nombres antiguos y los nuevos.
    'userid':'user_id'
}
df.rename(columns = rename_userid, inplace = True) #luego se llama al metodo rename para aplicar los cambios de los nuevos nombres.
print(df.columns) #por ultimo se imprime el resultado y se verifica de que 'userid' se a cambiado correctamente a la regla snake_case 'user_id'.


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[9]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#    
# Excelente implementación del método **rename()**, muy bien reuselto! Sigamos! 
#     

# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[10]:


# Calcular el número de valores ausentes
print(df.isna().sum()) #se utiliza el metodo 'isna' para encontrar valores ausentes en la tabla df y el metodo 'sum()' para sumar todos los valores ausentes.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Muy buena implementación para resolver la consigna. Sigue así!

# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[11]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track', 'artist', 'genre'] #aca se almacenan la lista de columnas con valores ausentes que queremos reemplazar.

for col in columns_to_replace: #se crea el blucle for para iterar en la lista que contiene las columnas. 
    df[col].fillna('unknown', inplace = True) #se utiliza el metodo 'fillna' para reemplazar los valores ausentes en las columnas selecionadas por 'unknown' y el argumento inplace que realiza la operación de eliminado sobre el mismo DataFrame, en lugar de crear y devolver uno nuevo .


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Felicitaciones! Implementaste una lógica de gran utilidad para evitar repeteciones en tu código y has completado con el valor 'unknown' como se ha solicitado, perfecto Cristopher!.</div>

# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[12]:


# Contar valores ausentes
print(df.isna().sum()) #se comprueba que efectivamente al imprimir nuevamente se observa que ya no existen valores ausentes.


# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[13]:


# Contar duplicados explícitos
print(df.duplicated().sum()) #verificamos cuantos duplicados explicitos existen con el metodo 'duplicated()' y elmetodo 'sum()' para sumarlos y nos de elresultado total.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Bien resuelto! Simple y conciso, perfecta la utilización del doble método corroborando los duplicados y sumandolos con sum(). </div>

# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[14]:


# Eliminar duplicados explícitos
df.drop_duplicates(inplace=True) #utilizamos el metodo drop_duplicates para elimnar los duplicados explicitos y tambien utilizamos el argumentos 'inplace=True' para no tener necesidad de reasignarlo.


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[15]:


# Comprobar de nuevo si hay duplicados

print(df.duplicated().sum()) #imprimimos nuevamente y comprobamos que efectivamente se han eliminado correctamente todos los duplicados explicitos.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente implementación del método **drop_duplicates()**, a la vez una recocmendación que es una buena práctica es la de utilizar el método **reset_index()**, una buena práctica siempre luego de eliminar duplicados.

# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[16]:


# Inspeccionar los nombres de géneros únicos
print(df['genre'].sort_values().unique()) #se ordenan los datos unicos extraidos de la columna 'genre' alfabeticamente. 


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Perfecto! Muy bien implementado Cristopher, a la vez felicitaciones por utilizar el método **.sort_values()** que nos permite ver de forma más clara los resultados.

# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[17]:


# Función para reemplazar duplicados implícitos
def replace_wrong_genres(wrong_genres, correct_genre): #creamos la funcion llamada replace_wrong_genres() con sus dos parametros wrong_genres, correct_genre.   
    for wrong_genres in wrong_genres: #creamos el bucle for para los nombres que estan mal escritos.
        df['genre'] = df['genre'].replace(wrong_genres, correct_genre) #se utiliza el metodo 'replace()' para cada nombre incorrecto.
    return df #devolvemos el DataFrame modificado.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Muy bien! Buena implementación lógica, has resuelto correctamente! 

# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[18]:


# Eliminar duplicados implícitos
duplicates = ['hip', 'hop', 'hip-hop'] #la lista con los generos mal escritos.
genre_correct = 'hiphop' #el genero escrito correctamente.
df = replace_wrong_genres(duplicates, genre_correct) #llamar a la funcion 'replace()' 


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[19]:


# Comprobación de duplicados implícitos
print(df['genre'].sort_values().unique()) #imprimimos y verificamos que los cambios se han realizado correctamente.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Nuevamente la implementación del reemplazo es correcta y la observación también. Felicitaciones!

# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# 
# los duplicados explicitos no son tan complicados de analizar solo se debe  utilizar el metodo duplicated() y el metodo sum() para conseguir el total de los duplicados explicitos y luego eliminarlos con el metodo drop_duplicates().
# 
# Lo que si me parecio un poco abrumador fue el conseguir los datos duplicados implicitos, ya que se debe tener de buen ojo para encontrarlos en listas tan grandes como estas, o simplemente no se si exista alguna forma de filtrarlas de mejor manera desde python para encontrar los datos incorrectos de una manera mas eficiente, aparte del metodo de darle los datos a la inteligencia artificial y solicitarle que busque justamente estos duplicados implicitos. 
# 
# Los metodos utilizados en los duplicados implicitos fueron el 'unique()' para que nos diera justamente los valores unicos de la columna 'genre' luego se creo una Funcion para corregir los datos incorrectos por los datos correctos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente! A medida que continúes con tus estudios aprenderás técnicas para como manejar mejor estos casos!

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[20]:


# Contar las canciones reproducidas en cada ciudad
songs_played_groups = df.groupby('city')['genre'].count() #agrupamos los datos por ciudad y canciones reproducidas con el metodo 'groupby()' y loego utilizamos el metodo 'count()' para contar cada cancion reproducidad y que nos de el total de cada ciudad.
print(songs_played_groups) #imprimimos la variable donde guardamos los metodos de agrupacion y conteo. para verificar sus totales.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente implementación, has agrupado correctamente aquellas columnas que debíamos agrupar! Sigamos! </div>

# `Comenta tus observaciones aquí`
# 
# Se observa una cantidad mayor de reproducciones de canciones en springfield (42.741 canciones) que en shelbyville (18.512 canciones)

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[21]:


# Calcular las canciones reproducidas en cada uno de los tres días
views_per_day = df.groupby('day')['genre'].count() #agrupamos los datos por canciones reproducidas por dia con el metodo 'groupby()' y loego utilizamos el metodo 'count()' para contar cada cancion reproducidad y que nos de el total de cada dia.
print(views_per_day) #imprimimos la variable donde guardamos los metodos de agrupacion y conteo. para verificar sus totales.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Nuevamente buena implementación, diferente agrupación. 

# `Comenta tus observaciones aquí`
# 
# Ahora podemos observar los datos de reproducciones por dia donde podemos darnos cuenta de que el dia con mas reproducciones de canciones es el dia viernes (21.840 canciones) seguido de el dia lunes (21.254 cancione) y por ultimo tenemos el dia miercoles (18.059 canciones).

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[22]:


def number_tracks(day, city): # Declara la función number_tracks() con dos parámetros: day= y city=.

    filtered_day_city = df[df['day'] == day] # Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=

    filtered_day_city = filtered_day_city[filtered_day_city['city'] == city] # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=

    count_total = filtered_day_city['user_id'].count() # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()
    
    return count_total


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente forma de resolverlo! Realizaste 2 filtros en una única sequencia que te brindarían el resultado posteriormente al utilizar .count(), bien hecho!.</div>

# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[23]:


total_monday = number_tracks('Monday', 'Springfield') # El número de canciones reproducidas en 'Springfield' el lunes
print(total_monday)


# In[24]:


total_monday = number_tracks('Monday', 'Shelbyville') # El número de canciones reproducidas en Shelbyville el lunes
print(total_monday)


# In[25]:


total_wednesday = number_tracks('Wednesday', 'Springfield') # El número de canciones reproducidas en Springfield el miércoles
print(total_wednesday)


# In[26]:


total_wednesday = number_tracks('Wednesday', 'Shelbyville') # El número de canciones reproducidas en Shelbyville el miércoles
print(total_wednesday)


# In[27]:


total_friday = number_tracks('Friday', 'Springfield')# El número de canciones reproducidas en Springfield el viernes
print(total_friday)


# In[28]:


total_friday = number_tracks('Friday', 'Shelbyville')# El número de canciones reproducidas en Shelbyville el viernes
print(total_friday)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Muy bien estas últimas implementaciones!

# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# 
# hasta el momentos podemos decir que las hiposis son parcialmente correctas, se evidencia con los datos obtenidos mayor reproducciones de canciones en especifico por dias de la semana, y se evidencia tambien la cantidad de reproducciones por ciudad ya que se obseva claramente mayores reproducciones en una ciudad que en la otra.

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`
# 
# luego de realizar los estudios a los datos obtenidos podemos evidenciar que en la ciudad de 'Springfield' se obtienen mayores reproducciones de musica en los 3 dias. en la ciudad de 'Shelbyville' se observa que el mayor numero de reproducciones se realizan los dias miercoles mientras que en 'Springfield' son los dias viernes. por lo cual podemos decir que hasta el momento se cumple la hipotesis parcialmente ya que los datos que tenemos son un poco escasos, no nos permiten realizar una conclucion de hipotesis por completo.  

# <div class="alert alert-block alert-success">
# <b>Comentario final. (Iteración 1) </b> <a class="tocSkip"></a>
# 
# Felicitaciones Cfistopher, hemos llegado al final de la notebook y tu desempeño fue increíble. Estas conclusiones reflejan y demuestran tu compromiso con el trabajo y lo valoramos, tanto tus aplicaciones de código como tus interpretaciones demuestran tu comprensión. Felicitaciones! 

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# [Volver a Contenidos](#back)
