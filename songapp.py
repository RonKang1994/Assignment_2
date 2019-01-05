"""Mangage the Song App Class here"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.clock import mainthread
from songlist import SongList


class SongsToLearnApp(App):
    def build(self):
        self.title = "Song List"
        self.root = Builder.load_file('app.kv')
        return self.root

    def handle_sort(self):
        if self.root.ids.sort_label.text == "Year":
            self.root.ids.sort_label.text = "Title"
        elif self.root.ids.sort_label.text == "Title":
            self.root.ids.sort_label.text = "Artist"
        elif self.root.ids.sort_label.text == "Artist":
            self.root.ids.sort_label.text = "Year"

    def add_song_button(self):
        button = Button(text="B_")
        self.root.ids.songs.add_widget(button)

    def handle_add_song(self):
        pass

    def handle_clear(self):
        pass