<p align=center><img src=http://math.prep.soyhenry.com/_src/assets/logo.png><p>

# PROYECTO INDIVIDUAL PI MLops 

## *Breve descripción del proyecto.*
Modelo Data Engineer y ML que soluciona problema de negocio mediante un sistema de recomendación de servicios streaming

#### Problemática:
El ciclo de vida de un proyecto de Machine Learning parte desde el tratamiento de datos denominado ETL 
analisis de estos datos mediante una Analisis exploratorio EDA finalizando con entrenamiento de un modelo mediante tecnicas
de Machine Learning con el resultado final de un modelo de ML que genera un sistema de recomendacion en base a datos similares 

#### Propuesta Solucion:
Se establecen 4 pasos para cubrir estas etapas del ciclo del proyecto de machine learning 

<hr> 

`PASO 1`
#### Proceso Analisis exploratio de datos EDA:
Este proceso se realiza para obtener una vista general del conjunto de datos, verificar la calidad de los datos mediante diferentes 
parámetros como valores nulos, outliers y visualizaciones de los datos para una comprensión mas rápida y efectiva 

`PASO 2`
#### Proceso Extracción, transformación y carga (ETL)

#### EXTRACCIÓN DE DATOS
Se trabajo con 4 datasets de empresas de streaming (Amazon prime, disney plus, hulu, netflix)
con datos referidos a contenido , titulos , genero espacio temporal entre otros 
Por otro se cuenta con 8 datasets referidos a ratings, votaciones de usuarios relacionados con los 4 dataset precedentes
por medio de un ID

#### TRANSFORMACIONES
Se realizo proceso de ETL que consiste en limpiar y organizar datos en bruto y prepararlos para el almacenamiento, 
el análisis de datos y el machine learning (ML) para despues combinarlos en 1 solo dataset

`PASO 3`
#### DESARROLLO DE FUNCIONES
Desarrollo de las consultas solicitadas:
Se realizaron 6 consultas sobre el dataset resultante de la combinacion de los provistos en primera instancia

1. Película (sólo película, no serie, ni documentales, etc) con mayor duración según año, plataforma y tipo de duración
2. Cantidad de películas (sólo películas, no series, ni documentales, etc) según plataforma, con un puntaje mayor a XX en determinado año
3. Cantidad de películas (sólo películas, no series, ni documentales, etc) según plataforma
4. Actor que más se repite según plataforma y año
5. La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año
6. La cantidad total de contenidos/productos (todo lo disponible en streaming, series, documentales, peliculas, etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula). 

`PASO 4`
#### Proceso creacion API y DEPLOYMENT
Se utilizo libreria de python FastApi para la creación y el alojamiento de aplicacion (API) para ejecutar las funciones citadas supra en un entorno web 
Se realizo deployment mediante Render que permite el despliegue de la aplicación para evaluar su funcionamiento en un entorno web

<hr> 
#### Uso API
Como funcionan las consultas

En el despliegue (entorno web) se cuenta con 7 bloques donde se ingresaran variables para ser procesadas arrojando un resultado segun el objetivo de cada una de las funciones supra

Mediante la siguiente URL se accede al entorno web
https://

<hr> 
#### Video explicativo
En el presente video se realiza una explicacion de los pasos realizados como propuesta de solucion a la problematica planteada
https://

<hr> 
#### Tecnologias utilizadas

Lenguaje Python
Librerias scikit-learn machine learning
Numpy
Pandas
FastApi
Uvicornio

<br>

<div>
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" style="width: 133px; height: 100px; display: inline-block;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png" style="width: 133px; height: 100px; display: inline-block;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png" style="width: 133px; height: 100px; display: inline-block;">
  <img src="https://www.kindpng.com/picc/m/574-5747046_python-pandas-logo-transparent-hd-png-download.png" style="width: 133px; height: 100px; display: inline-block;">
  <img src="https://repository-images.githubusercontent.com/260928305/92388600-8d1c-11ea-9993-a726466b5099" style="width: 133px; height: 100px; display: inline-block;">
  <img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" style="width: 133px; height: 100px; display: inline-block;">
</div>

