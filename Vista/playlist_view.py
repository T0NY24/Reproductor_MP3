import flet as ft
from Modelo.song import Song

class PlaylistView(ft.View):
    def __init__(self, page: ft.Page, controlador):
        super().__init__(
            route="/playlist",
            horizontal_alignment="center"
        )
        self.page = page
        self.controlador = controlador
        self.playlist: list[Song] = self.controlador.obtener_playlist()
        self.controls = [
            ft.Row(
                [ft.Text("Playlist", size=21, weight="bold")],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent"),
            self.create_add_song_controls()
        ]
        self.generate_playlist_ui()

    def create_add_song_controls(self):
        self.song_name_input = ft.TextField(label="Song Name")
        self.artist_name_input = ft.TextField(label="Artist Name")
        self.audio_path_input = ft.TextField(label="Audio Path")
        self.img_path_input = ft.TextField(label="Image Path")
        add_button = ft.ElevatedButton(
            text="Add Song",
            on_click=self.add_song
        )
        return ft.Column(
            [
                self.song_name_input,
                self.artist_name_input,
                self.audio_path_input,
                self.img_path_input,
                add_button
            ]
        )

    def add_song(self, e):
        song_name = self.song_name_input.value
        artist_name = self.artist_name_input.value
        audio_path = self.audio_path_input.value
        img_path = self.img_path_input.value
        song = self.controlador.agregar_cancion(song_name, artist_name, audio_path, img_path)
        if song:
            self.playlist.append(song)
            self.update_playlist_ui()
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Song '{song_name}' added successfully!"))
            self.page.snack_bar.open = True
            self.page.update()

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

    def update_playlist_ui(self):
        self.controls = [
            ft.Row(
                [ft.Text("Playlist", size=21, weight="bold")],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent"),
            self.create_add_song_controls()
        ]
        self.generate_playlist_ui()
        self.page.update()

    def toggle_song(self, e):
        song = self.controlador.obtener_cancion(e.control.data.song_name)
        if song:
            self.controlador.set_current_song(song)
            self.page.go("/song")
