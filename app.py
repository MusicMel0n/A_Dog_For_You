#A dog for you app
#Made for Microsoft ty event
import kivy
kivy.require('2.0.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
from kivy.config import Config

Config.set('graphics', 'resizable', False)

WIN_WIDTH, WIN_HEIGHT = 428, 926

Builder.load_file('adogforyou.kv')

fixedSize = (WIN_WIDTH, WIN_HEIGHT)
Window.size = (WIN_WIDTH, WIN_HEIGHT)
Window.top = 100
Window.left = 740

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

class ComposeMessage(Screen):
    pass

class QuizForm(Screen):
    pass

class QuizResults(Screen):
    pass

screen_manager =  ScreenManager()

screen_manager.add_widget(ScreenOne(name='home_screen'))
screen_manager.add_widget(ScreenTwo(name='login_screen'))
screen_manager.add_widget(MainScreen(name='main_screen'))
screen_manager.add_widget(ScreenFour(name='register_screen'))
screen_manager.add_widget(DirectMessages(name="direct_messages"))
screen_manager.add_widget(QuizScreen(name='quiz_screen'))
screen_manager.add_widget(TrailScreen(name="trail_screen"))
screen_manager.add_widget(ComposeMessage(name="compose_message"))
screen_manager.add_widget(QuizForm(name="quiz_form"))
screen_manager.add_widget(QuizResults(name="quiz_results"))


class adogforyouApp(App):
    a = 0
    b = str(a)
    def build(self):
        return screen_manager

    def reSize(*args):
        Window.size = fixedSize
        return True
    Window.bind(on_resize = reSize)

app = adogforyouApp()

if __name__ in ('__main__', '__android__'):
    app.run()
