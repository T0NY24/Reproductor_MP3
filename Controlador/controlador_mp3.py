import requests
from Modelo.song import Song

class ControladorMusica:
    def __init__(self):
        self.current_song: Song = None

    def set_current_song(self, song: Song):
        self.current_song = song

    def get_current_song(self) -> Song:
        return self.current_song

    def obtener_playlist(self):
        response = requests.get("http://127.0.0.1:5000/playlist")
        playlist_data = response.json()
        return [Song(**song) for song in playlist_data]

    def obtener_cancion(self, song_name: str):
        response = requests.post("http://127.0.0.1:5000/song", json={"song_name": song_name})
        if response.status_code == 200:
            song_data = response.json()
            return Song(**song_data)
        return None

    def agregar_cancion(self, song_name: str, artist_name: str, audio_path: str, img_path: str):
        response = requests.post("http://127.0.0.1:5000/add_song", json={
            "song_name": song_name,
            "artist_name": artist_name,
            "audio_path": audio_path,
            "img_path": img_path
        })
        if response.status_code == 201:
            song_data = response.json()
            return Song(**song_data)
        return None
