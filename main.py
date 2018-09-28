from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
import kivy.uix.textinput
from kivy.uix.label import Label
from kivy.uix.button import Button
import webbrowser
class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["username"].text == "suman" and self.ids["password"].text == "suman":
            self.manager.current = "user"
        else:
            content = Button(text='Invalid credentials!')
            popup = Popup(content=content, size=(0.25,0.25))
            popup.open()


class UserPage(Screen):
    pass
#    def qrgen(self):
#        url=

class ProfilePage(Screen):
    pass

class QRoperation(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file("login.kv")

class LoginApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    LoginApp().run()
