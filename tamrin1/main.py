from kivy.app import App
from kivy.uix.screenmanager import ScreenManager ,Screen

class WindowManager(ScreenManager):
   pass

class Window1(Screen):
  def btn_peress(self):
     self.manager.current="window2"
class Window2(Screen):
   def btn_peress(self):
     self.manager.current="window1"

class MyApp(App):
    pass

MyApp().run()

