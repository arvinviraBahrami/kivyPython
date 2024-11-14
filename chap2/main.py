from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyWidgets(Widget):
    def __init__(self):
        super().__init__()
        self.add_widget(Label(text="firstName:", bold=False,pos=(50,520),font_size=30,color=(60/255,90/255,160/255,1)))
        self.add_widget(TextInput(multiline=False,pos=(200,550),size=(300,38),font_size=30))
        self.add_widget(Label(text="lastName:", bold=False,pos=(50,570),font_size=30,color=(60/255,90/255,160/255,1)))
        self.add_widget(TextInput(multiline=False,pos=(200,600),size=(300,38),font_size=30))
        self.add_widget(Button(text="click me!",pos=(20,450),size=(480,58),font_size=30))
        self.add_widget(Button(text="location button",pos=(60,200),size=(200,58),font_size=30,on_press=self.btn_press))

    def btn_press(self,instance):
        print(instance.pos)

class MyApp(App):
    def build(self):
        return MyWidgets()

MyApp().run()
