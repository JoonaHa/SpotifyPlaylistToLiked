#! /usr/bin/env python3
import sys
import time
import spotipy
import spotipy.util as util
#from spotipy.oauth2 import SpotifyClientCredentials

SCOPE = 'user-library-modify'


def get_playlist_tracks(spotify, playlist_id):
    playlist_response = spotify.playlist_tracks(playlist_id, fields=['total'])
    track_count = playlist_response['total']
    songs = []
    while len(songs) < track_count:
        respone_items = spotify.playlist_tracks(
                playlist_id, limit=100,
                offset=len(songs))['items']
        songs += respone_items

    return songs


def get_playlist_id(spotify, playlist_name):
    results = spotify.current_user_playlists()['items']
    return list(filter(lambda x: x['name'] == playlist_name, results))[0]['id']


def get_args():
    if len(sys.argv) > 3:
        username = sys.argv[1]
        playlist_name = sys.argv[2]

        try:
            timeout = int(sys.argv[3])
        except ValueError:
            print(
                    "Usage: " + sys.argv[0] +
                    " <user_id> <playlist> <timeout_insecond_int>")
            sys.exit(-1)

    else:
        print(
            "Usage: " + sys.argv[0] +
            " <user_id> <playlist> <timeout_insecond_int>")
        sys.exit(-1)
    return username, playlist_name, timeout


def main():
    username, playlist_name, timeout = get_args()
    token = util.prompt_for_user_token(username, show_dialog=True, scope=SCOPE)
    spotify = spotipy.Spotify(token)
    user_name = spotify.current_user()['display_name']

    playlist_id = get_playlist_id(spotify, playlist_name)
    tracks = get_playlist_tracks(spotify, playlist_id)

    for i in tracks:
        time.sleep(timeout)
        track = i['track']
        print(track['artists'][0]['name'] + " - " + track['name'])
        spotify.current_user_saved_tracks_add([track['id']])

    print(
            "\nAdded " + str(len(tracks)) + " tracks to user's "
            + user_name + " library from playlist " + playlist_name + "\n")


if __name__ == '__main__':
    main()
