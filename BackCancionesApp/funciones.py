import requests

# Función que realiza la búsqueda de canciones en la API de Itunes y retorna los primeros 25 resultados
def buscar_canciones(nombre_banda):
    url = 'https://itunes.apple.com/search'
    params = {
        'term': nombre_banda,
        'entity': 'song'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        resultados = response.json()
        return resultados['results'][0:25]
    else:
        return []


# Función que calcula el número de álbumes y canciones presentes en los resultados de la búsqueda
def obtener_albumes_canciones(resultados):
    albumes = {}
    canciones = 0
    for resultado in resultados:
        album = resultado['collectionName']
        if album not in albumes:
            albumes[album] = 0
        albumes[album] += 1
        canciones += 1
    return albumes, canciones
