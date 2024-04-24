# Billboard Hot 100 Scraper & Spotify Playlist Creator

This Python script allows you to scrape the Billboard Hot 100 chart for a specified date and create a private Spotify playlist with the top songs from that date.

## Features

- **Web Scraping Billboard Data**: Utilizes BeautifulSoup to extract song titles from the Billboard Hot 100 chart based on a specified date.
- **Integration with Spotify API**: Uses the `spotipy` library to interact with the Spotify API for playlist creation and song addition.
- **OAuth 2.0 Authorization**: Implements Spotify OAuth 2.0 authorization flow to access user's Spotify account and manage playlists.
- **Automated Song Search**: Searches for each song on Spotify to obtain its unique URI for playlist addition.
- **Error Handling**: Skips songs that are not found on Spotify and informs the user.

## Usage

1. **Authorization**:
   - Make sure you have a Spotify Developer account.
   - Replace `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` in the script with your own Spotify application credentials.
   - Set up a Redirect URI (e.g., `http://example.com`) in your Spotify Developer dashboard and update `REDIRECT_URI` in the script accordingly.

2. **Dependencies**:
   - Install required Python packages using pip:
     ```bash
     pip install requests beautifulsoup4 spotipy
     ```

3. **Execution**:
   - Run the script in your Python environment:
     ```bash
     python spotifyPlaylist.py
     ```
   - Input the desired date when prompted in the format `YYYY-MM-DD`.
   - The script will create a private Spotify playlist named `[date] Billboard 100` and add the top songs from the specified date to the playlist.

## Customization

- **Billboard URL (`URL`)**: Modify the `URL` variable in the script to scrape data from a different Billboard chart if needed.
- **Scope (`SCOPE`)**: Update the `SCOPE` variable to customize the level of access required for your Spotify application.
- **Error Handling**: Extend error handling logic to handle specific scenarios based on your use case.

## Notes

- Ensure the `cache_path` (`token.txt`) is writable to store Spotify authentication tokens.
- Handle potential errors gracefully, such as songs not found on Spotify, to maintain a smooth user experience.


![image](https://github.com/patreeck/spotifyPlaylist/assets/163764755/7cac0e2e-ee11-4f83-942f-efc0d5c93fc3)

<img width="702" alt="image" src="https://github.com/patreeck/spotifyPlaylist/assets/163764755/49a7ec9d-27e6-4876-beca-fa1134c7004d">



