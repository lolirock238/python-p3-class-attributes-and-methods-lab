class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """Initialize a new song with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class-level tracking
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre histogram count."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist histogram count."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage and testing
if __name__ == "__main__":
    # Create some songs
    ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
    halo = Song("Halo", "Beyonce", "Pop")
    crazy_in_love = Song("Crazy in Love", "Beyonce", "Pop")
    hotline_bling = Song("Hotline Bling", "Drake", "Rap")
    run_the_world = Song("Run the World", "Beyonce", "Pop")
    
    # Test instance attributes
    print("Song name:", ninety_nine_problems.name)
    print("Song artist:", ninety_nine_problems.artist)
    print("Song genre:", ninety_nine_problems.genre)
    print()
    
    # Test class attributes and methods
    print("Total song count:", Song.count)
    print("All artists:", Song.artists)
    print("All genres:", Song.genres)
    print("Genre count:", Song.genre_count)
    print("Artist count:", Song.artist_count)