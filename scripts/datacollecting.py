import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import pandas as pd

# Spotify API credentials
client_id = ''
client_secret = ''

# Genius API credentials
genius_token = ''

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get playlist tracks
# playlist_id = '37i9dQZF1DXbSbnqxMTGx9'
playlist_ids = [
    # '7qACZGMjyo64TdUdKAegjp',
    # '3HYK6ri0GkvRcM6GkKh0hJ',
    # '4mijVkpSXJziPiOrK7YX4M',
    # '0ZVSWcJIf7cvycEn9HUvps',
    # '6MXkE0uYF4XwU4VTtyrpfP',
    # '5EyFMotmvSfDAZ4hSdKrbx',
    # '71kedeh6L7P0equUL0vOqe',
    # '6gS3HhOiI17QNojjPuPzqc',
    # '37i9dQZF1DXbSbnqxMTGx9',
    # '7dowgSWOmvdpwNkGFMUs6e'
    '1tMiLQpYeZJpD6DyrCaDaB'
]
genres = [
    # 'blues', 
    # 'classical', 
    # 'Country',
    # 'disco', 
    'hiphop', 
    # 'jazz',
    # 'metal', 
    # 'pop', 
    # 'reggae',
    # 'rock'
]
# Initialize Genius API
genius = lyricsgenius.Genius(genius_token)

for i in range(len(playlist_ids)):
    try: 
        results = sp.playlist_tracks(playlist_ids[i])
    except: 
        print("could not get the playlist")
        continue
    # Initialize DataFrame to store results
    columns = ['Artist', 'Track', 'Lyrics', 'Genre']
    df = pd.DataFrame(columns=columns)
    # Extract track information and lyrics
    for item in results['items']:
            track = item['track']
            artist = track['artists'][0]['name']
            track_name = track['name']
            track_id = track['id']            
            # Fetch lyrics
            try:
                song = genius.search_song(track_name, artist)
            except:
                print("genius call failed")
                continue
            if song:
                lyrics = song.lyrics
                print("Artist:", artist)
                print("Track:", track_name)
                # print("Lyrics:", lyrics)
                if len(lyrics) > 3000: 
                    continue
                lyrics.replace(",", "")
                
            else:
                df = df._append({'Artist': artist, 'Track': track_name, 'Lyrics': -1, 'Genre': genres[i]}, ignore_index=True)
                print("Lyrics not found for:", artist, "-", track_name)
    # Save DataFrame to CSV file
    df.to_csv('playlist_lyrics_'+ genres[i] +'2.csv', index=False)
