# This is an app that it has as objective to help or auxiliary people to maintain their goals about keeping in their
# food recipe and healthy schedule rewarding with points and other things if the user make what it's programed

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()