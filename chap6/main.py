from kivy.app import App
from kivy.uix.screenmanager import ScreenManager ,Screen
# from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import FadeTransition

class WindowManager(ScreenManager):
   pass

class Window1(Screen):
   def btn_peress(self):
   #   self.manager.transition=SlideTransition(duration=0.7,direction="left")
     self.manager.transition=FadeTransition(duration=0.7)
     self.manager.current="window2"
     
class Window2(Screen):
   def btn_peress(self):
   #   self.manager.transition=SlideTransition(duration=0.7,direction="right")
     self.manager.transition=FadeTransition(duration=0.7)
     self.manager.current="window1"

class MyApp(App):
   
    pass

MyApp().run()

