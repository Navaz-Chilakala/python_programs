
from pytube import Playlist

# Function to download a YouTube playlist
def download_playlist(playlist_url, download_path):
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # Display the playlist title
    print(f'Downloading playlist: {playlist.title}')

    # Loop through each video in the playlist and download it
    for video in playlist.videos:
        print(f'Downloading video: {video.title}')
        video.streams.get_highest_resolution().download(download_path)
        print(f'Video {video.title} downloaded successfully!')

# URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLs5_Rtf2P2r68M58HkA1_ejfAK0OaP0q3'

# Path where the videos will be downloaded
download_path = r'D:\bhima'  # Use a raw string for the path

# Call the function to download the playlist
download_playlist(playlist_url, download_path)
