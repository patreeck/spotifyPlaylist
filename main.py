import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

SPOTIFY_CLIENT_ID = "YOUR SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR SPOTIFY_CLIENT_SECRET"
REDIRECT_URI = 'http://example.com'
URL = 'https://www.billboard.com/charts/hot-100/'

SCOPE = 'playlist-modify-private'  # Example scope for reading a user's library

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Pratik',
    )
)
user_id = sp.current_user()["id"]

date = input("Which year you want to travel to ? Type date in this format YYYY-MM-DD :\n")
# print(date)

res = requests.get(url=f'{URL}/{date}')
html_content = res.text
soup = BeautifulSoup(html_content, "html.parser")

song_title = soup.find_all(name='h3', id='title-of-a-story', class_="a-font-primary-bold-s")
# print(song_title)
all_songs = []
for song in song_title:
    # print(song.text)
    all_songs.append(song.text.strip())

song_list = all_songs[2:]
# print(song_list)
song_uris = []
year = date.split("-")[0]
# print(year)
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
