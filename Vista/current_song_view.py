import flet as ft
from Modelo.song import Song

class CurrentSongView(ft.View):
    def __init__(self, page: ft.Page, controlador):
        super().__init__(
            route="/song",
            horizontal_alignment="center",
            padding=20,
            vertical_alignment="center",
        )
        self.page = page
        self.controlador = controlador
        self.song: Song = self.controlador.get_current_song()
        self.create_audio_track()

        self.duration: int = 0
        self.start: int = 0
        self.end: int = 0

        self.is_playing: bool = False

        self.txt_start = ft.Text(self.format_time(self.start))
        self.txt_end = ft.Text(f"-{self.format_time(self.end)}")

        self.slider = ft.Slider(
            min=0,
            max=100,
            thumb_color="transparent",
            on_change_end=lambda e: self.toggle_seek(
                round(float(e.data))
            )
        )

        self.back_btn = ft.TextButton(
            content=ft.Text(
                "Playlist",
                color="black"
                if self.page.theme_mode == ft.ThemeMode.LIGHT
                else "white",
            ),
            on_click=self.toggle_playlist,
        )

        self.play_btn = self.create_toggle_button(
            ft.icons.PLAY_ARROW_ROUNDED, 2, self.toggle_play_pause
        )

        self.controls = [
            ft.Row(
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
                    color=ft.colors.with_opacity(0.35, "black")
                ),
                image_fit="cover",
                image_src=self.song.img_path,
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Column(
                [
                    ft.Row([self.txt_start, self.txt_end],
                           alignment="spaceBetween"),
                    self.slider,
                ]
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                [
                    self.create_toggle_button(
                        ft.icons.REPLAY_10_SHARP,
                        0.9,
                        lambda e: self._seek_position(-5000)
                    ),
                    self.play_btn,
                    self.create_toggle_button(
                        ft.icons.FORWARD_10_SHARP,
                        0.9,
                        lambda e: self._seek_position(5000)
                    ),
                ],
                alignment="spaceEvenly"
            ),
            ft.Divider(height=10, color="transparent"),
        ]

    def play(self, e):
        self.slider.max = 100
        self.audio.play()
        self.is_playing = True            
             
        self.play_btn.icon = ft.icons.PAUSE_CIRCLE_ROUNDED
        self.play_btn.update()
        self.duration = self.audio.get_duration()
        self.end = self.duration
        self.slider.max = self.duration

    def toggle_play_pause(self, event=None):
        if self.is_playing:
            self.play_btn.icon = ft.icons.PLAY_ARROW_ROUNDED
            self.audio.pause()
        else:
            self.play_btn.icon = ft.icons.PAUSE_CIRCLE_ROUNDED
            try:
                self.audio.resume()
            except Exception:
                self.audio.play()
        self.is_playing = not self.is_playing
        self.play_btn.update()

    def _update_start_end(self):
        if self.start < 0:
            self.start = 0
        if self.end > self.duration:
            self.end = self.duration

    def _seek_position(self, delta: int):
        self._update_start_end()
        pos_change = 0
        if delta > 0:
            if delta == 5000:
                pos_change = 5000
            elif delta == -5000:
                pos_change = -5000
            pos: int = self.start + pos_change
            self.audio.seek(pos)
            self.start += pos_change
            self.end -= pos_change
            self._update_slider(self.start)

    def _update_slider(self, delta):
        self.slider.value = delta
        self.slider.update()

    def _update_time_stamps(self, start: int, end: int):
        self.txt_start.text = self.format_time(start)
        self.txt_end.text = f"-{self.format_time(end)}"
        self.txt_start.update()
        self.txt_end.update()

    def toggle_seek(self, delta):
        self.start = delta
        self.end = self.duration - delta

        self.audio.seek(self.start)
        self._update_slider(delta)

    def _update(self, delta: int):
        self.start = delta
        self.end = self.duration - delta

        self._update_slider(delta)
        self._update_time_stamps(self.start, self.end)

    def format_time(self, value: int):
        milliseconds = value
        minutes, seconds = divmod(milliseconds / 1000, 60)
        formatted_time = "{:02}:{:02}".format(int(minutes), int(seconds))
        return formatted_time

    def create_audio_track(self):
        self.audio = ft.Audio(
            src=self.song.audio_path,
            on_position_changed=lambda e: self._update(
                int(e.data)
            )
        )

        self.page.overlay.append(self.audio)

    def create_toggle_button(self, icon, scale, function):
        return ft.IconButton(
            icon=icon,
            icon_size=scale * 24,
            on_click=function
        )

    def toggle_playlist(self, e):
        self.audio.pause()
        self.page.session.clear()
        self.page.go("/playlist")
