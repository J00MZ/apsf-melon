"""Application models."""

from database import db

class Player(db.Model):
    """Appslify music player."""

    def __init__(self, playlist_id):
        self.current_playlist = playlist_id
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    current_playlist = db.relationship('Playlist', backref='player', lazy=True)

class Playlist(db.Model):
    """Song playlist."""

    def __init__(self, playlist_id):
        self.current_playlist = playlist_id
        self.is_playing_now = False
    
    playlist_id = db.Column(db.Integer, primary_key=True, nullable=False)
    is_playing_now = db.Column(db.Boolean, nullable=False)
    songs = db.relationship('Song', backref='playlist', lazy=True)

    def is_playing_now(self, is_playing_now):
        return self.is_playing_now

    def start_playing(self):
        self.is_playing_now == True
    
    def add_song(self, song):
        self.songs.append(song)

class Song(db.Model):
    """Song"""

    def __init__(self, name, playlist_id):
        self.song_name = name
        self.playlist_id = playlist_id
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.playlist_id'), nullable=False)
