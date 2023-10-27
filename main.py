from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
import webbrowser
import requests


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class WindowInfo(Screen):
    pass


class WindowEnchente(Screen):
    pass


class WindowAr(Screen):
    pass


def invalidLogin():
    pop = Popup(title='Login Invalido',
                content=Label(text='Usuario ou senha invalidos.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Por favor preencha todos os campos com informações validas!.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("users.txt")
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), WindowEnchente(name="enchente"), WindowAr(name="ar")]
for screen in screens:
    sm.add_widget(screen)
    sm.current = "login"



class MyMainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return sm

    def fechar(self):
        self.stop()


if __name__ == "__main__":
    MyMainApp().run()