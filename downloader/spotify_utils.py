from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e7982a5028f94fa5884bf864352abb50",
                                                           client_secret="1114f775e3634c40bf5e40a886d7cb89"))

def get_songs_from_playlist(playlist_url):
    playlist = sp.playlist_items(playlist_url)
    songs = []
    for item in playlist['items']:
        track = item['track']
        songs.append({
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name']
        })
    return songs
