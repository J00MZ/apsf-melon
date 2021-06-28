"""Application models."""

from database import db
from app import logger

class Playlist(db.Model):
    """Song playlist."""

    playlist_id = db.Column(db.Integer, primary_key=True, nullable=False)
    is_playing_now = db.Column(db.Boolean, nullable=False)
    songs = db.relationship('Song', backref='Playlist', lazy=True)

    def is_playing_now(self, is_playing_now):
        return self.is_playing_now

    def start_playing(self):
        logger.debug(f"Playlist with ID [{self.playlist_id}] and date [{self.playlist_date}] is currently playing")
        self.is_playing_now == True

    def get_playlist(self):
        return self

class Song(db.Model):
    """Song"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
