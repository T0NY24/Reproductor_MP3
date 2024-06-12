import flet as ft

# Crear la clase Song
class Song(object):
    def __init__(self, song_name: str, artist_name: str, audio_path: str, img_path: str):
        self.song_name = song_name
        self.artist_name = artist_name
        self.audio_path = audio_path
        self.img_path = img_path
    

# Crear la clase AudioDirectory
class AudioDirectory(object):
    playlist = [
        Song("cielo", "mora", "cielo.mp3", "img0.jpg"),
        Song("title", "Bad Bunny", "title.mp3", "img1.jpg"),
        Song("Monaco", "Bad Bunny", "2.mp3", "img2.jpg")
    ]

# Clase para la lista de reproducción
class Playlist(ft.View):
    def __init__(self, page: ft.Page):
        super(Playlist, self).__init__(
            route="/playlist",
            horizontal_alignment="center"
        )
        
        self.page = page
        self.playlist = AudioDirectory.playlist
        self.controls = [
            ft.Row(
                [ft.Text("Playlist", size=21, weight="bold")],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent")
        ]
        self.generate_playlist_ui()

    # Método para generar la interfaz de usuario de la lista de reproducción
    def generate_playlist_ui(self):
        for song in self.playlist:
            self.controls.append(
                self.generate_song_row(  # Cambiado de create_song_row a generate_song_row
                    song_name=song.song_name,
                    artist_name=song.artist_name,
                    song=song,
                )
            )

    # Método para generar una fila de canción
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
            on_click=self.toggle_song  # Necesitas implementar este método
        )

    # Método para cambiar la canción
    def toggle_song(self, e):
        e.page.session.set("song", e.control.data)
        self.page.go("/song")
        pass
class CurrentSong(ft.View):
    def __init__(self, page: ft.Page):
        super(CurrentSong, self).__init__(
            route="/song",
            horizontal_alignment="center",
            padding=20,
            vertical_alignment="center",
        )
        
        self.page = page

        self.song=self.page.session.get("song")

        print(self.song.name, self.song.artist)
    

        
            

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear() 
        if page.route == "/playlist":
            playlist = Playlist
            page.views.append(playlist(page))
        if page.route =="/song":
            song = CurrentSong(page)
            page.views.append(song)
        
        page.update()

    page.on_route_change = router
    page.go("/playlist")

ft.app(target=main, assets_dir="assets")
