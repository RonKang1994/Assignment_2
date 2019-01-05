# create your Song class in this file


class Song:
    def __init__(self, title="", artist="", year=0, is_required=True):
        self.title = title
        self.artist = artist
        self.year = int(year)
        self.is_required = is_required

    def __str__(self):
        if self.is_required:
            return "\"{}\", {}, {}, (Learned)".format(self.title, self.artist, self.year)
        else:
            return "\"{}\", {}, {}".format(self.title, self.artist, self.year)

    """Mark the song as learned(change is_required to True)"""
    def mark_learned(self):
        if self.is_required:
            print("Alredy Learned")
        else:
            self.is_required = True
            print("Learned")

