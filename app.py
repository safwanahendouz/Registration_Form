import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RegistrationForm(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        head_label = Label(text="Registration Form", font_size=26, bold=True)
        layout.add_widget(head_label)

        return layout


if __name__ == '__main__':
    RegistrationForm().run()