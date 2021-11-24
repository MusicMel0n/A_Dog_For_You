import kivy
kivy.require('2.0.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.scrollview import ScrollView


Builder.load_file('adogforyou.kv')

Window.size = (428, 926)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class MainScreen(Screen):
    pass

class ScreenFour(Screen):
    pass

class DirectMessages(Screen):
    pass

class QuizScreen(Screen):
    pass

class TrailScreen(Screen):
    pass

screen_manager =  ScreenManager()

screen_manager.add_widget(ScreenOne(name='home_screen'))
screen_manager.add_widget(ScreenTwo(name='login_screen'))
screen_manager.add_widget(MainScreen(name='main_screen'))
screen_manager.add_widget(ScreenFour(name='register_screen'))
screen_manager.add_widget(DirectMessages(name="direct_messages"))
screen_manager.add_widget(QuizScreen(name='quiz_screen'))
screen_manager.add_widget(TrailScreen(name="trail_screen"))


class adogforyouApp(App):
    a = 0
    b = str(a)
    def build(self):
        return screen_manager

app = adogforyouApp()

if __name__ in ('__main__', '__android__'):
    app.run()
