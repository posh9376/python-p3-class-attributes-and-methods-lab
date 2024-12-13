class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    def add_to_genres(self):
        if self.genre in Song.genres:
            return
        else:
            Song.genres.append(self.genre)
            if self.genre in Song.genre_count:
                Song.genre_count[self.genre] += 1
            else:
                Song.genre_count[self.genre] = 1

    def add_to_artists(self):
        if self.artist in Song.artists:
            return
        else:
            Song.artists.append(self.artist)
            if self.artist in Song.artist_count:
                Song.artist_count[self.artist] += 1
            else:
                Song.artist_count[self.artist] = 1