CREATE DATABASE musica;
USE musica;

CREATE TABLE canciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    song_name VARCHAR(255) NOT NULL,
    artist_name VARCHAR(255) NOT NULL,
    audio_path VARCHAR(255) NOT NULL,
    img_path VARCHAR(255) NOT NULL
);
