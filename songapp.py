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
        # Used to identify which song button is pressed
        # self.song_button_id = []
        # using the SongList Class
        self.song_list = SongList()
        self.song_list.load_songs("songs.csv")
        self.create_song_list()
        # Used for sorting
        self.sort_codes = SORT_TYPE.keys()
        self.current_state = self.sort_codes[0]
        # Button variable for the learning of songs
        return self.root

    # Create the buttons based on the length of the song list
    def create_song_list(self):
        # # Clear all in order to remake
        # if not self.song_button_id:
        #     self.song_button_id.clear()
        self.root.ids.songs.clear_widgets()
        self.root.ids.req_learn.text = self.song_list.cal_learn_n_req()
        for i in range(len(self.song_list.songs)):
            # All the attributes of the button
            song_text = str(self.song_list.songs[i].__str__())
            button2 = Button(text=song_text, font_size = 15, text_size = (200, None))
            # button2.font_size = 15
            # button2.text_size = (200, None)
            if self.song_list.songs[i].is_required:
                button2.background_color = 0.0, 1.0, 0.0, 1.0
                button2.state = 'down'
            else:
                button2.background_color = 1.0, 0.0, 0.0, 1.0
            # Bind the Button to the function handle_song_learn()
            # button2.bind(on_release=lambda x: self.handle_song_learn(button2))
            button2.bind(on_release=self.handle_song_learn)
            # This line makes the buttons
            self.root.ids.songs.add_widget(button2)
            # # Save the buttons ids
            # self.song_button_id.append(button.ids)

    # Used to sort my list of songs (it destroys and recreates all the buttons)
    def handle_sort(self, current_state):
        if current_state == "Year":
            self.song_list.sort(1)
            self.create_song_list()
        elif current_state == "Title":
            self.song_list.sort(2)
            self.create_song_list()
        elif current_state == "Artist":
            self.song_list.sort(3)
            self.create_song_list()

    # Handles learning songs
    def handle_song_learn(self, check_button):
        for i in range(len(self.song_list.songs)):
            if check_button.text == str(self.song_list.songs[i].__str__()):
                if self.song_list.songs[i].is_required:
                    # Already learned
                    self.root.ids.message_id.text = self.song_list.songs[i].title + "\nis already learned"
                    self.create_song_list()
                else:
                    # Change to learned
                    self.root.ids.message_id.text = self.song_list.songs[i].title + "\nis now learned"
                    self.song_list.songs[i].is_required = True
                    self.create_song_list()
                    self.song_list.save_songs()


    # Used to add a song to the list of songs (forces a sort)
    def handle_add_song(self):
        if self.root.ids.input_title.text == '':
            self.root.ids.input_title.text = "All fields must be completed"
        if self.root.ids.input_artist.text == '':
            self.root.ids.input_artist.text = "All fields must be completed"
        if self.root.ids.input_year.text.isdigit() == False:
            self.root.ids.input_year.text = "Please enter a valid number"
            return
        elif int(self.root.ids.input_year.text) <= 1:
            self.root.ids.input_year.text = "Please enter a valid number"
            return
        if self.root.ids.input_title.text != '' and self.root.ids.input_artist.text != '' and int(self.root.ids.input_year.text) > 1 and self.root.ids.input_year.text.isdigit():
            self.song_list.add_song(self.root.ids.input_title.text, self.root.ids.input_artist.text, int(self.root.ids.input_year.text))
            self.root.ids.message_id.text = "You have learned " + self.root.ids.input_title.text
            # Recreate the list to add the new song
            self.create_song_list()
            # Forces a sort to ensure the list will be sorted
            self.handle_sort(self.current_state)
            # Save the new song to the CSV
            self.song_list.save_songs()

    # Clears all text in the input fields and the status bar
    def handle_clear(self):
        self.root.ids.message_id.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_title.text = ""
        self.root.ids.input_year.text = ""