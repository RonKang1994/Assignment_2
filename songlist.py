# create your SongList class in this file
"""Import Song class to use here"""
from song import Song
"""Used to help with sorting"""
from operator import itemgetter, attrgetter, methodcaller

class SongList(Song):
    def __init__(self):
        super().__init__(title="", artist="", year=0, is_required=False)
        self.songs = []
        """Number of songs learned and required"""
        self.song_learned = 0
        self.song_required = 0

    def __str__(self):
        if len(self.songs) > 0:
            """Print out the entire list of songs"""
            for song in self.songs:
                if song == self.songs[-1]:
                    return "{}\n".format(song)
                else:
                    print(song)
        else:
            """No Songs at all"""
            return "Empty"


    """Load in songs form a .txt or .csv file"""
    def load_songs(self, song_file):
        temp_song_list = []
        song_data = open(song_file, 'r')
        for line in song_data:
            temp_song_list.append(line.split(','))
        for row in temp_song_list:
            row[-1] = row[-1].strip('\n')
        song_data.close()
        for data in temp_song_list:
            if data[-1] == 'y':
                song = Song(data[0], data[1], int(data[2]), True)
                self.songs.append(song)
            else:
                song = Song(data[0], data[1], int(data[2]), False)
                self.songs.append(song)


    """Used to sort the song list is various ways"""
    def sort(self, sort_type):
        if sort_type == 1:
            """1 Sort by Year"""
            self.songs.sort(key=lambda Song: Song.year)
        elif sort_type == 2:
            """2 Sort by Title"""
            self.songs.sort(key=lambda Song: Song.title)
        elif sort_type == 3:
            """3 Sort by Artist"""
            self.songs.sort(key=lambda Song: Song.artist)
