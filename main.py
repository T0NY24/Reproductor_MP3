import flet as ft
from Controlador.controlador_mp3 import ControladorMusica
from Vista.playlist_view import PlaylistView
from Vista.current_song_view import CurrentSongView

def main(page: ft.Page):
    controlador = ControladorMusica()
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()
        if page.route == "/playlist":
            playlist = PlaylistView(page, controlador)
            page.views.append(playlist)
        elif page.route == "/song":
            song_view = CurrentSongView(page, controlador)
            page.views.append(song_view)

        page.update()

    page.on_route_change = router
    page.go("/playlist")

ft.app(target=main, assets_dir="assets")
