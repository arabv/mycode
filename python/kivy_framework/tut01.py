import kivy
kivy.require("1.9.1")

from kivy.app import app
from kivy.uix.label import label
class MyApp(App):
    def build(self):
        return Label(text="Hello world!")

if __name__=="__main__":
    MyApp().run()
