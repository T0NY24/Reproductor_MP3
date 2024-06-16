from Modelo.audio_directory import AudioDirectory
from Modelo.song import Song

class ControladorMusica:
    def __init__(self):
        self.current_song: Song = None

    def set_current_song(self, song: Song):
        self.current_song = song

    def get_current_song(self) -> Song:
        return self.current_song

    def obtener_playlist(self):
        return AudioDirectory.playlist
