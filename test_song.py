"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, False)
# TODO: write tests to show this initialisation works

# test mark_learned()
# TODO: write tests to show the mark_learned() method works
"""Check before learned"""
print(song2)
song2.mark_learned()
"""Check after learned"""
print(song2)
