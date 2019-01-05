"""
Name: Ron Kang
Brief Project Description: Used to create a song list with Kivy
GitHub URL: https://github.com/RonKang1994/Assignment_2
"""

from kivy.app import App
from songlist import SongList
from songapp import SongsToLearnApp

# Create your main program in this file, using the SongsToLearnApp class
def main():
    """Used to show the GUI"""
    SongsToLearnApp().run()


main()