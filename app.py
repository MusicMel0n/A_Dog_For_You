import kivy
kivy.require('2.0.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (428, 926)

class CustomWidget(Widget):
    pass

class adogforyouapp(App):
    def build(self):
        return CustomWidget()

dogforyou = adogforyouapp()

dogforyou.run()
