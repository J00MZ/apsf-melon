"""Application main app."""

from flask import Flask
import requests
import logging, coloredlogs

from utils import get_todays_date
from database import db, migrate
from models import Player, Playlist, Song

app = Flask(__name__)
coloredlogs.install(level='DEBUG', isatty=True)
logger = logging.getLogger('app_log')
db.init_app(app)
migrate.init_app(app, db)
db.create_all(app=app)

def init_player():
    appslify_api_endpoint = 'https://run.mocky.io/v3/4f6aee07-4831-4279-aecf-292fc05ec439'
    response = requests.get(appslify_api_endpoint)
    playlists = response.json()
    logger.debug(f'Got from endpoint playlists: {playlists}')
    for plist, songs in playlists.items():
        logger.debug(f'Creating playlist with key [{plist}]')
        pl = Playlist(plist)
        for song in songs:
            new_song = Song(song, pl.playlist_id)
            logger.debug(f"Adding Song {song.song_name} to playlist")
            pl.add_song(new_song)
    
    logger.info('Showing current playlist playing')

    return(Player(get_todays_date()))

player = init_player()

@app.route('/api/v1/show_full_list')
def show_full_list():
    return(logger.info('Showing all playlists'))

@app.route('/api/v1/show_current_playlist')
def show_current_playlist():
    logger.info('Showing current playlist playing')
    playlist_id = get_todays_date()
    current_playlist = Playlist.query.get_or_404(playlist_id,
                           f'Sorry, couldn\'t find any Playlist with the id {playlist_id}')
    return(current_playlist)

@app.route('/api/v1/play')
def play():
    plist_id = get_todays_date()
    logger.debug(f"Playlist with ID [{plist_id}] should be currently playing")
    current_plist = Playlist.query.get_or_404(plist_id,
                           f'Sorry, couldn\'t find any Playlist with the id {plist_id}')
    logger.debug(f"Playlist includes songs {current_plist.songs}")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
