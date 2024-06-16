# 🎵 Reproductor MP3 con Flet 🎵
¡Bienvenido al proyecto de Reproductor MP3! Este es un reproductor MP3 simple pero elegante, construido utilizando el framework Flet, que te permite disfrutar de tus canciones favoritas con una interfaz moderna y limpia. Este proyecto demuestra el poder de Python y Flet para construir aplicaciones de escritorio multiplataforma.

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://miro.medium.com/v2/resize:fit:640/1*dKU4uBSnJCs4jzkkuiALoQ.png" alt="Python Logo" width="150">
    </a>
    <a href="https://flet.io/">
        <img src="https://avatars.githubusercontent.com/u/102273996?v=4" alt="Flet Logo" width="100">
    </a>  
    
</p>
<p align="center">
    <a href="https://travis-ci.org/joemccann/dillinger">
        <img src="https://travis-ci.org/joemccann/dillinger.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://travis-ci.org/joemccann/dillinger">
        <img src="https://travis-ci.org/joemccann/dillinger.svg?branch=master" alt="Build Status">
    </a>
</p>
## 🌟 Características

- 🎶 **Gestión de Playlist**: Añade, elimina y organiza fácilmente tus canciones favoritas.
- 🖼️ **Visualización de Portadas**: Muestra la portada del álbum para cada canción en tu playlist.
- 🔊 **Reproducción de Audio**: Reproduce, pausa y salta pistas con controles intuitivos.
- 🚀 **Multiplataforma**: Funciona sin problemas en Windows, macOS y Linux.
- 📂 **Estructura de Directorios Simple**: Fácil de navegar y gestionar tus archivos de audio.

## 📸 Capturas de Pantalla
![Captura de Pantalla de Playlist](assets/screenshots/playlist.png)
![Captura de Pantalla de Canción Actual](assets/screenshots/current_song.png)

## 🔧 Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

- Python 3.11 o superior
- Paquete Flet

### Clonar el Repositorio

```bash
git clone https://github.com/T0NY24/Reproductor_MP3.git
cd reproductor-mp3-flet
```

### Instalar Dependencias

```bash
pip install flet
```
```bash
pip install flet flask requests
```
```bash
pip install flask flask_sqlalchemy mysqlclient requests

```

### Ejecutar la Aplicación

```bash
flet run main.py
```

## 🗂️ Estructura del Proyecto

```
reproductor-mp3-flet/
├── controlador/
│   └── controlador_musica.py
│
├── modelo/
│   └── audio_directory.py
│   └── song.py
│
├── vista/
│   └── playlist_view.py
│   └── current_song_view.py
│
├── server/
│   └── app.py
│
└── main.py

```

## 📜 Descripción del Código

### main.py

Este es el punto de entrada principal de la aplicación. Define las clases `Song` y `AudioDirectory`, así como las vistas `Playlist` y `CurrentSong`.

### Clase Song

La clase `Song` es una estructura de datos simple que contiene información sobre cada canción, incluyendo el título, el artista, la ruta del archivo de audio y la ruta del archivo de imagen.

### Clase AudioDirectory

La clase `AudioDirectory` contiene una playlist predefinida. Esto puede extenderse para cargar canciones dinámicamente desde un directorio o base de datos.

### Vista Playlist

La vista `Playlist` muestra la lista de canciones y permite al usuario seleccionar una canción para reproducir.

### Vista CurrentSong

La vista `CurrentSong` muestra la canción que se está reproduciendo actualmente junto con sus detalles y portada.

## 🚀 Uso

1. **Añadir Canciones**: Añade tus archivos MP3 e imágenes correspondientes a los directorios `assets/audio` y `assets/images`, respectivamente.
2. **Modificar Playlist**: Actualiza la clase `AudioDirectory` en `main.py` para incluir tus nuevas canciones.
3. **Ejecutar Aplicación**: Inicia la aplicación usando `flet run main.py` y ¡disfruta de tu música!

## 💡 Consejos

- Asegúrate de que tus archivos de audio e imagen estén nombrados adecuadamente para evitar confusiones.
- Personaliza la interfaz de usuario modificando los componentes de Flet en `main.py` según tus preferencias.
- Explora la documentación de Flet para obtener más características avanzadas y opciones de personalización.

## 🛠️ Mejoras Futuras

- **Carga Dinámica de Playlists**: Cargar canciones dinámicamente desde un directorio especificado.
- **Funcionalidad de Búsqueda**: Añadir una barra de búsqueda para encontrar rápidamente canciones en tu playlist.
- **Ecualizador**: Integrar un ecualizador para ajustar la salida de audio.
- **Visualización de Letras**: Mostrar las letras de la canción que se está reproduciendo.

## 📬 Contacto

Si tienes alguna pregunta, sugerencia o comentario, no dudes en contactarme en [anperezcue@uide.edu.ec].

## 📜 Licencia

Este proyecto no está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Disfruta de tu música! 🎧

---

