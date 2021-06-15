# SpotifyPlaylistToLiked
Import any of your playlists to 'Your library' to the  'Liked Songs' section while keeping the original order of songs.
The need for this arise when Spotify changed from 'Starred tracks' to the 'Your library' and 'Liked songs' system.
I needed to import Starred tracks to Liked songs in the original adding order.

This Python-projects solves it by improting the songs from a chosen playlist while adding a timeout between songs.
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
--- 
### Linux
Set argument and enviroment variables in run.sh:

You will find ``` SPOTIPY_CLIENT_ID``` and ```SPOTIPY_CLIENT_SECRET```
from your Spotify app's dahsboard. 

Script expects that your python3 path is set.
Give your user_id number and the given playlist you want to import as arguments
Remember to also add ```http://localhost:9999``` **Redirect URIs**
```bash
#! /usr/bin/env bash
export SPOTIPY_CLIENT_ID=""
export SPOTIPY_CLIENT_SECRET=""
export SPOTIPY_REDIRECT_URI="http://localhost:9999"

python3 ./run.py "<user_id>" "<your-playlist's-name>" 1
```
Make run.sh executable : 
```bash
chmod +x run.sh
```
Run the wrapper-file :
```bash
./runs.sh
```
---
### Windows
There is  a run.bat file for **Windows** where you can set the needed environment variables.

You will find ``` SPOTIPY_CLIENT_ID``` and ```SPOTIPY_CLIENT_SECRET```
from your Spotify app's dahsboard. 

Script expects that your python3 path is set.
Give your user_id number and the given playlist you want to import as arguments
Remember to also add ```http://localhost:9999``` **Redirect URIs**
```bat
@ECHO OFF
SET SPOTIPY_CLIENT_ID="" 
SET SPOTIPY_CLIENT_SECRET=""
SET SPOTIPY_REDIRECT_URI="http://localhost:9999"

python3 run.py "<user_id>" "<your-playlist's-name>" 1

ECHO Ready. Press any key to close the program

PAUSE>NUL

```
Run the wrapper-file :

```bat
run.bat
```
