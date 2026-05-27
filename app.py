import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RegistrationForm(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        head_label = Label(text="Registration Form", font_size=26, bold=True ,height=40)
        # Adding label
        name_label = Label(text="Name:", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18)

        name_label = Label(text="Name:", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18)

        name_label = Label(text="Name:", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18)
        
        name_label = Label(text="Name:", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18)

        # Adding widgets to layout
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)

        return layout


if __name__ == '__main__':
    RegistrationForm().run()