@ECHO OFF
SET SPOTIPY_CLIENT_ID="" 
SET SPOTIPY_CLIENT_SECRET=""
SET SPOTIPY_REDIRECT_URI="http://localhost:9999"

python3 run.py "<user_id>" "<your-playlist's-name>" 1

ECHO Ready. Press any key to close the program

PAUSE>NUL
