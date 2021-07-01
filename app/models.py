"""Application models."""

from database import db

class Player(db.Model):
    """Appslify music player."""

    def __init__(self, playlist_id):
        self.current_playlist = playlist_id
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    current_playlist = db.relationship('Playlist', backref='player', uselist=False, lazy=True)

class Playlist(db.Model):
    """Song playlist."""

    def __init__(self, playlist_id):
        self.current_playlist = playlist_id
        self.is_playing_now = False
        self.current_playlist_iteration = 0
    
    playlist_id = db.Column(db.Integer, primary_key=True)
    is_playing_now = db.Column(db.Boolean, nullable=False)
    songs = db.relationship('Song', backref='playlist', lazy=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    current_playlist_iteration = db.Column(db.Integer, nullable=False)
    
    def add_song(self, song):
        self.songs.append(song)

    def start_playing(self):
        self.songs[0].start_playing()
        self.is_playing_now == True
    
    def is_playing_now(self, is_playing_now):
        return self.is_playing_now

    def get_current_song(self, song_id):
        current_song = self.songs['song_id']
        return current_song if current_song.is_playing_now() else False

    def shuffle_songs(self):
        pass
    
    def get_current_iteration(self):
        return self.current_playlist_iteration
    
    def start_new_iteration(self):
        self.current_playlist_iteration += self.current_playlist_iteration

class Song(db.Model):
    """Song"""

    def __init__(self, name, playlist_id):
        self.song_name = name
        self.playlist_id = playlist_id
        self.is_playing_now = False
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.playlist_id'), nullable=False)
    is_playing_now = db.Column(db.Boolean, nullable=False)

    def start_playing(self):
        self.is_playing_now == True

    def end_playing(self):
        self.is_playing_now == False
