from kivy.app import App
from kivy.uix.widget import Widget

class MyWidgets(Widget):
   def btn_press(self):
       self.ids.label1.color=(100/55,90/205,160/255,1)

class MyApp(App):
    pass
MyApp().run()


# root ?  