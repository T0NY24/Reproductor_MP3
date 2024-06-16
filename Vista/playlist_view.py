import flet as ft
from Modelo.audio_directory import AudioDirectory
from Modelo.song import Song

class PlaylistView(ft.View):
    def __init__(self, page: ft.Page, controlador):
        super().__init__(
            route="/playlist",
            horizontal_alignment="center"
        )
        self.page = page
        self.controlador = controlador
        self.playlist: list[Song] = AudioDirectory.playlist
        self.controls = [
            ft.Row(
                [ft.Text("Playlist", size=21, weight="bold")],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent")
        ]
        self.generate_playlist_ui()

    def generate_playlist_ui(self):
        for song in self.playlist:
            self.controls.append(
                self.generate_song_row(
                    song_name=song.song_name,
                    artist_name=song.artist_name,
                    song=song,
                )
            )

    def generate_song_row(self, song_name, artist_name, song: Song):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"Title: {song_name}"),
                    ft.Text(artist_name),
                ],
                alignment="spaceBetween",
            ),
            data=song,
            padding=10,
            on_click=self.toggle_song
        )

    def toggle_song(self, e):
        self.controlador.set_current_song(e.control.data)
        self.page.go("/song")
