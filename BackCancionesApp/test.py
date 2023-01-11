from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # Lanza la aplicación en modo testing
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # Comprueba que el endpoint /search_tracks funciona correctamente
    def test_search_tracks(self):
        response = self.app.get('/search_tracks?name=metallica')
        self.assertEqual(response.status_code, 200)

    # comprueba que la informacion se trae correctamente
    def test_search_tracks_data(self):
        response = self.app.get('/search_tracks?name=metallica')
        self.assertEqual(response.json['total_albumes'], 3)
        self.assertEqual(response.json['total_canciones'], 25)
        self.assertEqual(response.json ['albumes'], ["Metallica", "Metallica (Remastered)", "...And Justice for All (Remastered)"])

    # Comprueba que el endpoint /favoritos funciona correctamente
    def test_favoritos(self):
        response = self.app.post('/favoritos', json={
            "nombre_banda": "Radiohead",
            "cancion_id": 125,
            "usuario" : "sebastian",
            "ranking" : "5/5"
        })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()







