# SpotifyPlaylistToLiked
Import any of your playlists to your library or 'Liked Songs' while keeping the original order.
The need for this arise when Spotfy changed from 'Starred tracks' to the 'Your library' and 'Liked songs' system.
I needed to import Starred tracks to my library in the original adding order.

This Python-projects solves it by improting the songs from a chosen playlist while adding a timeout while adding indidual songs.
The default timeout is 1 second, because the Spotify-API timestamps only support one second precision.

**You need to register for Spotify Web-Api by registering an app at [My Dashboard](https://developer.spotify.com/dashboard/applications)**

### Requirements
* Requirements: Python 3 and [Spotipy](https://github.com/plamere/spotipy)

 Clone this repository : 
```bash
git clone https://github.com/JoonaHa/SpotifyPlaylistToLiked
```
 Chanced to the cloned directory  : 
```bash
cd SpotifyPlaylistToLiked
```
Install Spotipy :
```bash
python3 -m pip install spotipy
```
Or use the requirements.txt file :
```bash
python3 -m pip install -r requirements.txt
```
Set argument and enviroment variables in run.sh:

You will find ``` SPOTIPY_CLIENT_ID``` and ```SPOTIPY_CLIENT_SECRET```
from your Spotify app's dahsboard. 

Remember to also add ```http://localhost:9999``` **Redirect URIs**
```bash
export SPOTIPY_CLIENT_ID="" 
export SPOTIPY_CLIENT_SECRET=""
export SPOTIPY_REDIRECT_URI="http://localhost:9999"

python3 ./run.py "<user_id>" "<your-playlist's-name>" 1
```
Make run.sh executable : 
```bash
chmod +x run.sh
```

Run the wrapper-file:
```bash
./runs.sh
```

