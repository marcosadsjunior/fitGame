# This is an app that it has as objective to help or auxiliary people to maintain their goals about keeping in their
# food recipe and healthy schedule rewarding with points and other things if the user make what it's programed

import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class FitGameApp(App):

    def build(self):
        return Builder.load_file('fitgame.kv')


if __name__ == '__main__':
    FitGameApp().run()