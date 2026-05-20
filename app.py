import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RegistrationForm(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
