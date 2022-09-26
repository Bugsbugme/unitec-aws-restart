import dotify
from fastapi import FastAPI

app = FastAPI()

# API Endpoints:
#   /playlists = returns list of playlists
#   /playlists/{id} = returns playlist id

# A decorator that is used to define the route of the API.
@app.get("/")
def welcome():
    """
    It returns the string "Welcome to Dotify!" in bold
    :return: The string "Welcome to Dotify!"
    """
    return "<b>Welcome to Dotify!</b>"


@app.get("/playlists")
def playlists():
    """
    It returns the playlists from the dotify module
    :return: A list of playlists
    """
    return dotify.playlists


@app.get("/playlists/{playlist_id}")
def playlist_by_id(playlist_id):
    """
    It takes a playlist ID as an argument, and returns the playlist with that ID.

    :param playlist_id: The ID of the playlist you want to get
    :return: A list of songs
    """
    playlist_id = int(playlist_id)
    playlist_length = len(dotify.playlists)
    if playlist_id > playlist_length or playlist_id < 0:
        return "Invalid Playlist ID"
    else:
        return dotify.playlists[playlist_id]
