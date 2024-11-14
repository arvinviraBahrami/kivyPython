from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class WindowManager(BoxLayout):
    def slider_change(self):
        x=round( self.ids.slider.value,2)
        # x=int( self.ids.slider.value,2)
        self.ids.text_slider.text= str(x)


class MyApp(App):
   
    pass

MyApp().run()





#   username
#[                   ]
#
#  password
#[                   ]
##  [submit}
#
##-------------
#    welcome
#
##  [logout}