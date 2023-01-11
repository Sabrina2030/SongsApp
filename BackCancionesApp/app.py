from flask import Flask, jsonify, request
from flask_caching import Cache
from favoritos import Favoritos
from funciones import buscar_canciones, obtener_albumes_canciones
from flask_cors import CORS


app = Flask(__name__)
favoritos = Favoritos()
cors = CORS(app, resources={r"/search_tracks": {"origins": "*"}})
cache = Cache(app, config={'CACHE_TYPE': 'simple'})



#endpoint : http://127.0.0.1:4000/search_tracks?name=metallica
@app.route("/search_tracks", methods=["GET"])
@cache.cached(timeout=3600)
def search_tracks():
    name = request.args.get("name")
    if not name:
        return "Error: No se ha especificado el nombre de la banda", 400

    resultados = buscar_canciones(name)
    
    albumes, canciones = obtener_albumes_canciones(resultados)

    respuesta = {
        'total_albumes': len(albumes),
        'total_canciones': canciones,
        'albumes': list(albumes.keys()),
        'canciones': resultados
    }
    
    return jsonify(respuesta)


#endpoint : http://127.0.0.1:4000/favoritos 
"""{
    "nombre_banda": "Radiohead",
    "cancion_id": 125,
    "usuario" : "sebastian",
    "ranking" : "5/5"
}"""
@app.route('/favoritos', methods=['POST'])
def agregar_favorito():
    datos = request.get_json()
    nombre_banda = datos['nombre_banda']
    cancion_id = datos['cancion_id']
    usuario = datos['usuario']
    ranking = datos['ranking']
    
    if nombre_banda and cancion_id and usuario and ranking:
        favoritos.agregar_favorito(nombre_banda, cancion_id, usuario, ranking)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error'})



@app.route('/favoritos', methods=['GET'])
def obtener_favoritos():
    return jsonify(favoritos.obtener_favoritos())
    


if __name__ == '__main__':
    app.run(debug=True, port=4000)

