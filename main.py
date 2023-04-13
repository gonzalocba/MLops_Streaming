#importamos librerias
import pandas as pd
from fastapi import FastAPI

# app donde se realizarán las consultas.
app = FastAPI(title = "MLOPS - Streaming")

plataformas_df = pd.read_csv(r'streaming.csv')

# Uso de app
@app.get('/')
def index():
    return 'Panel de consultas streaming Amazon, Disney , Hulu y Netflix'

# Consulta N°1: Película o serie con mayor duración según el año, la plataforma de streaming y su tipo de duración (min o seasons).
@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
def get_max_duration(year: int, platform, duration_type):
    
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    getmaxduration = plataformas_df 
    
    # Se crean los filtros de  dependiendo la plataforma, el año y si es tipo 'min' o 'seasons'.
    if platform.lower() == 'amazon':
        if duration_type == 'min':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'movie') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'a' in x))]
        elif duration_type == 'seasons':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'tv show') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'a' in x))]
    
    elif platform.lower() == 'disney':
        if duration_type == 'min':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'movie') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'd' in x))]
        elif duration_type == 'seasons':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'tv show') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'd' in x))]
    
    elif platform.lower() == 'hulu':
        if duration_type == 'min':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'movie') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'h' in x))]
        elif duration_type == 'seasons':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'tv show') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'h' in x))] 
    
    elif platform.lower() == 'netflix':
        if duration_type == 'min':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'movie') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'n' in x))]
        elif duration_type == 'seasons':
            getmaxduration = getmaxduration[(getmaxduration['type'] == 'tv show') & (getmaxduration['release_year'] == year) & (getmaxduration['duration_type'] == duration_type) & (getmaxduration['id'].apply(lambda x: 'n' in x))]   
    
    # Retorno si se ingresa un valor plataforma diferente a verificar
    else: 
        print('No se encuentra la plataforma , por favor ingrese: amazon, disney, Hulu y Netflix')
        return None
    
    # Se crea el filtro para que se obtenga la fila de la película o serie que tiene más duración.
    gmd_p_copia = getmaxduration[getmaxduration['duration_int'] == (getmaxduration['duration_int'].max())]
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return f'En la plataforma {platform}, la pelicula con mayor duración del año {year} , con formato tiempo {duration_type} es: {gmd_p_copia.iloc[0,2]}'


# Consulta N°2: Cantidad de películas o series por plataforma con un puntaje mayor a X en un año determinado.
@app.get('/get_score_count/{platform}/{scored}/{year}')
def get_score_count(platform, scored: float, year: int):
   
    getscorec= plataformas_df
    
    # se filtra score mayor a ingresado por parametro
    getscorec = getscorec[(getscorec['mean_score'] >= scored) & (getscorec['release_year'] == year)]
    
     # se aplico filtro plataforma parametros 
     # apply () aplica función lambda a lo largo de un eje del DataFrame.
    if platform.lower() == 'amazon':
        getscorec = getscorec[getscorec['id'].apply(lambda x: 'a' in x)]

    elif platform.lower() == 'disney':
        getscorec = getscorec[getscorec['id'].apply(lambda x: 'd' in x)]
    
    elif platform.lower() == 'hulu':
        getscorec = getscorec[getscorec['id'].apply(lambda x: 'h' in x)]

    elif platform.lower() == 'netflix':
        getscorec = getscorec[getscorec['id'].apply(lambda x: 'n' in x)]

    # Retorno si se ingresa un valor plataforma diferente a verificar
    else:
        print('No se encuentra la plataforma , por favor ingrese: amazon, disney, Hulu y Netflix')
        return None
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return f'Las peliculas de {platform} con puntaje mayor o igual a {scored} del año {year} son: {getscorec.shape[0]}'

# Consulta N°3: Cantidad de películas o series que se pueden encontrar según la plataforma.
@app.get('/get_count_platform/{platform}')
def get_count_platform(platform):
    
    getcplataform = plataformas_df
    
    # se aplico filtro plataforma parametros 
     # apply () aplica función lambda a lo largo de un eje del DataFrame.
    if platform.lower() == 'amazon':
        getcplataform= getcplataform[getcplataform['id'].apply(lambda x: 'a' in x)]

    elif platform.lower() == 'disney':
        getcplataformc = getcplataform[getcplataform['id'].apply(lambda x: 'd' in x)]
    
    elif platform.lower() == 'hulu':
        getcplataformc = getcplataform[getcplataform['id'].apply(lambda x: 'h' in x)]

    elif platform.lower() == 'netflix':
        getcplataformc = getcplataform[getcplataform['id'].apply(lambda x: 'n' in x)]
    
    # Retorno si se ingresa un valor plataforma diferente a verificar
    else:
        print('No se encuentra la plataforma , por favor ingrese: Amazon, Disney, Hulu y Netflix')
        return None
    
    # Devuelve cantidad peliculas
    return f'En la plataforma {platform} existen {getcplataformc.shape[0]} peliculas'
    

#Consulta N°4: Actor que más se repite según la plataforma y el año de la producción cinematográfica.
@app.get('/get_actor/{platform}/{year}')
def get_actor(platform, year: int):
    ga_p = plataformas_df
    
    #se aplica filtro y valores columna cast se realiza value_counts() que devuelve una serie que contiene recuentos de valores únicos.
    if platform.lower() == 'amazon':
        ga_pc= ga_p[(ga_p['release_year'] == year) & (ga_p['id'].apply(lambda x: 'a' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()

    elif platform.lower() == 'disney':
        ga_pc = ga_p[(ga_p['release_year'] == year) & (ga_p['id'].apply(lambda x: 'd' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
    
    elif platform.lower() == 'hulu':
        ga_pc = ga_p[(ga_p['release_year'] == year) & (ga_p['id'].apply(lambda x: 'h' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()

    elif platform.lower() == 'netflix':
        ga_pc = ga_p[(ga_p['release_year'] == year) & (ga_p['id'].apply(lambda x: 'n' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
    
    # Retorno si se ingresa un valor plataforma diferente a verificar
    else:
        print('No se encuentra la plataforma , por favor ingrese: Amazon, Disney, Hulu y Netflix')
        return None
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return f' El actor/actriz que más se repite en la plataforma {platform} durante el año {year} es: {ga_pca}' 