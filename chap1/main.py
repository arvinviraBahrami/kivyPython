# print("hello world ")

# class person:
#     def __init__(self,fristName,lastName):
#         self.fristName=fristName
#         self.lastName=lastName
        
# class student(person):
#     def __init__(self,fristName,lastName):
#         self.fristName=fristName
#         self.lastName=lastName


from kivy.app import App
from kivy.uix.label import Lable
from kivy.uix.widget import Widget


class myWidgets(Widget):
    def __init__(self):
        self.add_widget(Lable(text="hi"))
        self.add_widget(Lable(text="22555"))

class kivyapp(App):
    def Build(self):
        obj2=myWidgets()
        return obj2
obj1=kivyapp()
obj1.run() 