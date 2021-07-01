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

def init_player(app, db):
    appslify_api_endpoint = 'https://run.mocky.io/v3/4f6aee07-4831-4279-aecf-292fc05ec439'
    response = requests.get(appslify_api_endpoint)
    playlists = response.json()
    logger.debug(f'Got from endpoint playlists: {playlists}')
    with app.app_context():
        for plist_id, songs in playlists.items():
            logger.debug(f'Creating playlist with key [{plist_id}]')
            pl = Playlist(int(plist_id))
            for song in songs:
                new_song = Song(song, plist_id)
                logger.debug(f"Adding Song [{new_song.song_name}] to playlist")
                pl.add_song(new_song)
            db.session.add(pl)
            db.session.commit()
    
    logger.info('Showing current playlist playing')
    todays_date = get_todays_date()
    if todays_date == Playlist.query.filter_by(playlist_id=todays_date).first():
        playlist_date = todays_date
    else:
        latest_playlist = Playlist.query.order_by(Playlist.playlist_id).first().playlist_id
        playlist_date = latest_playlist
    with app.app_context():
        new_player = Player(playlist_date)
        db.session.add(new_player)
        db.session.commit()
    return(new_player)

player = init_player(app, db)

@app.route('/api/v1/show_playlists')
def show_full_list():
    playlists = Playlist.query.order_by(Playlist.playlist_id).all()
    logger.info(f'Showing all playlists')
    return(playlists)

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
    current_plist.start_playing()
    current_plist.songs[0].start_playing()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
