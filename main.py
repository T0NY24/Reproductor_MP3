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
        self.playlist: list[Song] = AudioDirectory.playlist
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

        self.song = self.page.session.get("song")
        self.create_audio_track()

        print(self.song.song_name, self.song.artist_name)

        self.duration: int = 0
        self.start: int=0
        self.end: int=0

        self.is_playing: bool = False

        self.txt_start=ft.Text(self.format_time(self.start))
        self.txt_end=ft.Text(f"-{self.format_time(self.start)}")

        self.slider =ft.slider(
            min=0,
            thumb_color="transparent",on_change_end=None)
        
        self.back_btn=ft.TextButton(
            content=ft.Text(
                "Playlist",
                color="black"
                if self.page.theme_mode == ft.ThemeMode.LIGHT
                else "white",
            ),
            on_click=self.toogle_playlist,
        )
        self.play_btn=self.create_toggle_button(
            ft.icons.PLAY_ARROW_ROUNDED,2,self.play
        )
       # Los controles del Main
        self.controls=[
            ft.row(
                [self.back_btn],
                alignment="start"
            ),
            ft.Container(
                height=120,
                expand=True,
                border_radius=8,
                shadow=ft.BoxShadow(
                    spread_radius=6,
                    blur_radius=10,
                    color=ft.colors.with_opacity(0.35,"black")
                ),
                image_fit="cover",
                image_src=self.song.path_img,                
            ),
            ft.Divider(height=10,color="transparent"),
            ft.Column(),
            ft.Divider(height=10,color="transparent"),
            ft.Row(
                [
                    self.create_toggle_button(
                        ft.icons.REPLAU_10_SHARP,
                        0.9,
                        lambda e: self._update_position(-5000)
                ),
                    self.play_btn,
                    self.create_toggle_button(
                        ft.icons.FORWARD_10_SHARP,
                        0.9,
                        lambda e: self._update_position(5000)
                ),
            ],
            alignment="spaceEvenly"
            ),
        ft.Divider(height=10,color="transparent"),

        ]
    
    def play(self,e):
        pass
    def _update_position(self, e):
        pass
    def _update(self,delta: int):
        self.star+=1000
        self.end-=1000

        self._update_slider(delta)
    def create_audio_track(self): 
        self.audio=ft.audio(
            src=self.song.path_audio,
            on_position_change=lambda e: self._update(
                int(e.data)
            )
            
        )

        self.page.overlay.append(self.audio)
    def create_toggle_button(self,icon,scale,function):
        return ft.IconButton(
        on_click=function)
    def toogle_playlist(self,e):
        pass
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear() 
        if page.route == "/playlist":
            playlist = Playlist
            page.views.append(playlist(page))
        if page.route == "/song":
            song = CurrentSong(page)
            page.views.append(song)
        
        page.update()

    page.on_route_change = router
    page.go("/playlist")

ft.app(target=main, assets_dir="assets")
