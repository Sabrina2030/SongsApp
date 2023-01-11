class Favoritos:
    def __init__(self):
        self.favoritos = []
    
    def agregar_favorito(self, banda, cancion_id, usuario, ranking):
        self.favoritos.append({
            'nombre_banda': banda,
            'cancion_id': cancion_id,
            'usuario': usuario,
            'ranking': ranking
        })
    
    def obtener_favoritos(self):
        return self.favoritos

