#! /usr/bin/env bash
export SPOTIPY_CLIENT_ID="" 
export SPOTIPY_CLIENT_SECRET=""
export SPOTIPY_REDIRECT_URI="http://localhost:9999"

python3 ./run.py "<user_id>" "<your-playlist's-name>" "<timeout_insecond_int>"
