"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
# """Sort by Year"""
# song_list.sort(1)
# print("Year Sort")
# print(song_list)
# """Sort by Title"""
# song_list.sort(2)
# print("Title Sort")
# print(song_list)
# """Sort by Artist"""
# song_list.sort(3)
# print("Artist Sort")
# print(song_list)

# test adding a new Song
# """add a new song"""
# song_list.add_song("Hello", "Art", 2012)
# print("New song added")
# print(song_list)

# test getting the number of required and learned songs (separately)
# song_list.cal_learn_n_req()

# test saving songs (check CSV file manually to see results)
# """Test saving new songs"""
# song_list.save_songs()
