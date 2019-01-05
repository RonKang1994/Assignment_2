"""Mangage the Song App Class here"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from songlist import SongList

# Used for sorting
SORT_TYPE = {'Year': "Sort_Year", 'Title': "Sort_Title", 'Artist': "Sort_Artist"}

class SongsToLearnApp(App):
    # Used for sorting
    current_state = StringProperty()
    sort_codes = ListProperty()

    def build(self):
        self.title = "Song List"
        self.root = Builder.load_file('app.kv')
        self.song_list = SongList()
        self.song_list.load_songs("songs.csv")
        self.create_song_list()
        self.sort_codes = SORT_TYPE.keys()
        self.current_state = self.sort_codes[0]
        return self.root

    def create_song_list(self):
        self.root.ids.songs.clear_widgets()
        self.root.ids.req_learn.text = self.song_list.cal_learn_n_req()
        for i in range(len(self.song_list.songs)):
            song_text = str(self.song_list.songs[i].__str__())
            button = Button(text=song_text)
            button.font_size = 15
            button.text_size = (200, None)
            if self.song_list.songs[i].is_required:
                button.background_color = 0.0, 1.0, 0.0, 1.0
            else:
                button.background_color = 1.0, 0.0, 0.0, 1.0
            self.root.ids.songs.add_widget(button)

    def handle_sort(self, current_state):
        print(current_state)
        if current_state == "Year":
            self.song_list.sort(1)
            self.create_song_list()
        elif current_state == "Title":
            self.song_list.sort(2)
            self.create_song_list()
        elif current_state == "Artist":
            self.song_list.sort(3)
            self.create_song_list()

    def handle_add_song(self):
        if self.root.ids.input_title.text == '':
            self.root.ids.input_title.text = "All fields must be completed"
        if self.root.ids.input_artist.text == '':
            self.root.ids.input_artist.text = "All fields must be completed"
        if self.root.ids.input_year.text.isdigit() == False:
            print("test")
            self.root.ids.input_year.text = "Please enter a valid number"
            return
        elif int(self.root.ids.input_year.text) <= 1:
            print("test2")
            self.root.ids.input_year.text = "Please enter a valid number"
            return
        if self.root.ids.input_title.text != '' and self.root.ids.input_artist.text != '' and int(self.root.ids.input_year.text) > 1800 and self.root.ids.input_year.text.isdigit():
            self.song_list.add_song(self.root.ids.input_title.text, self.root.ids.input_artist.text, int(self.root.ids.input_year.text))
            if self.root.ids.sort_label.text == "Year":
                self.song_list.sort(1)
                self.create_song_list()
            elif self.root.ids.sort_label.text == "Title":
                self.song_list.sort(2)
                self.create_song_list()
            elif self.root.ids.sort_label.text == "Artist":
                self.create_song_list(3)
                self.create_song_list()

    def handle_clear(self):
        pass