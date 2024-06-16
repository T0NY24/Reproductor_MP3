from flask import Flask, jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Modelo.song import Song

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/musica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cancion(db.Model):
    __tablename__ = 'canciones'
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(255), nullable=False)
    artist_name = db.Column(db.String(255), nullable=False)
    audio_path = db.Column(db.String(255), nullable=False)
    img_path = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'song_name': self.song_name,
            'artist_name': self.artist_name,
            'audio_path': self.audio_path,
            'img_path': self.img_path
        }

@app.route('/playlist', methods=['GET'])
def get_playlist():
    canciones = Cancion.query.all()
    playlist = [cancion.to_dict() for cancion in canciones]
    return jsonify(playlist)

@app.route('/song', methods=['POST'])
def get_song():
    data = request.json
    song_name = data.get("song_name")
    cancion = Cancion.query.filter_by(song_name=song_name).first()
    if cancion:
        return jsonify(cancion.to_dict())
    return jsonify({"error": "Song not found"}), 404

@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.json
    new_song = Cancion(
        song_name=data['song_name'],
        artist_name=data['artist_name'],
        audio_path=data['audio_path'],
        img_path=data['img_path']
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify(new_song.to_dict()), 201

if __name__ == '__main__':
    db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)
