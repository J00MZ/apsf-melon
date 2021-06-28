"""Application main app."""

from flask import Flask
import requests
import logging, coloredlogs

from utils import get_todays_date
from database import db, migrate
from models import Playlist, Song

app = Flask(__name__)
coloredlogs.install(level='DEBUG', isatty=True)
logger = logging.getLogger('app_log')
db.init_app(app)
migrate.init_app(app, db)
db.create_all(app=app)

def init_playlists():
    appslify_api_endpoint = 'https://run.mocky.io/v3/4f6aee07-4831-4279-aecf-292fc05ec439'
    response = requests.get(appslify_api_endpoint)
    for 

@app.route('/api/v1/show_full_list')
def show_full_list():
    app.logger.info('Showing all playlists')

    return(response.json())

@app.route('/api/v1/show_current_playlist')
def show_current_playlist():
    app.logger.info('Showing current playlist playing')
    playlist_id = get_todays_date()
    current_playlist = Playlist.query.get_or_404(playlist_id,
                           f'Sorry, couldn\'t find any Playlist with the id {playlist_id}')
    return(current_playlist)

@app.route('/api/v1/play')
def play_todays_playlist():
    date = get_todays_date()
    playlist = db.sess
    return(f"Playlist with ID [{playlist.id}] and date [{playlist.playlist_date}] is currently playing")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
