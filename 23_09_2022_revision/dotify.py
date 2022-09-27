class Track:
    """
    This is a Track object
    Required Properties:
        Title
        Artist
        Duration
    """

    def __init__(self, title, artist, duration):
        """
        A constructor function. It is used to initialize the object.

        :param title: The title of the song
        :param artist: The artist of the song
        :param duration: The duration of the song in seconds. This should be a float
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    """
    This is a Playlist object
    Required Properties:
        Tracks
        Title
        Creator
    """

    def __init__(self, tracks, title, creator):
        """
        This function takes in three arguments, tracks, title, and creator, and assigns them to the
        instance variables tracks, title, and creator.

        :param tracks: A list of Track objects
        :param title: The title of the playlist
        :param creator: The name of the person who created the playlist
        """
        self.tracks = tracks
        self.title = title
        self.creator = creator

    def add_track(self, track):
        """
        It adds a track to the playlist

        :param track: The track to add to the playlist
        """
        self.tracks.append(track)
        print(f"Added track {track}")


top_100 = Playlist([], "Top 100", "Billboard")

top_pops = Playlist([], "Top of the Pops", "Billboard")

eurovision = Playlist([], "Eurovision", "The EU")
eurovision.add_track(Track("Ievan Polkka", "Loituma", "2:43"))
eurovision.add_track(Track("Husavik", "Will Ferrell, My Marrianne", "3:22"))
eurovision.add_track(Track("Vitas", "The 7th Element", "4:09"))

playlists = [top_100, top_pops, eurovision]
