import kivy
kivy.require('2.0.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

Builder.load_file('adogforyou.kv')

Window.size = (428, 926)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass

screen_manager =  ScreenManager()

screen_manager.add_widget(ScreenOne(name='home_screen'))
screen_manager.add_widget(ScreenTwo(name='login_screen'))
screen_manager.add_widget(ScreenThree(name='main_screen'))
screen_manager.add_widget(ScreenFour(name='register_screen'))

class adogforyouApp(App):
    def build(self):
        return screen_manager

app = adogforyouApp()

app.run()
