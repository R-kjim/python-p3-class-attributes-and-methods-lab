class Song:
    pass
    count=0
    artists=[]
    genres=[]
    genre_count={}
    artist_count={}

    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_count(cls):
        cls.count+=1
    
    @classmethod
    def add_to_genres(cls,genre):
        if genre in cls.genres:
            None
        else:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist in cls.artists:
            None
        else:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        pass
        cls.genre_count[genre]=cls.genre_count.get(genre,0)+1
    
    @classmethod
    def add_to_artist_count(cls,artist):
        cls.artist_count[artist]=cls.artist_count.get(artist,0)+1
            


light=Song("light","MadFun","Blues")
grenade=Song("renade","Bruno Mars","Rap")
shout=Song("Shout","Dzaddy","Rap")
print(Song.genres)
print(Song.artists)
print(Song.genre_count)

# music={}
# music.update({"rap":1})
# music.update({"pop":2})
# print(music)
# print([item for item in music.keys()])
