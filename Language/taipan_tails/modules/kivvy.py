from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class TaipanKivvy:
    # Expose Kivy classes directly
    Widget = Widget
    Button = Button
    Label = Label
    BoxLayout = BoxLayout
    GridLayout = GridLayout
    TextInput = TextInput
    Window = Window
    Color = Color
    Rectangle = Rectangle
    Clock = Clock
    App = App
    
    @staticmethod
    def create_app(title="Taipan App"):
        class GameApp(App):
            def build(self):
                self.title = title
                return None
        return GameApp()
    
    @staticmethod
    def create_button(text, on_press=None):
        return Button(text=text, on_press=on_press)
    
    @staticmethod
    def create_label(text):
        return Label(text=text)
    
    @staticmethod
    def create_layout(orientation='vertical'):
        return BoxLayout(orientation=orientation)
    
    @staticmethod
    def create_grid(cols=2):
        return GridLayout(cols=cols)
    
    @staticmethod
    def create_input():
        return TextInput(multiline=False)
    
    @staticmethod
    def create_widget():
        return Widget()

def init_module():
    return TaipanKivvy()
