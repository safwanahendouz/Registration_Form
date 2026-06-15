import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationForm(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        head_Label = Label(text=" Python UserRegistration Form", font_size=26, bold=True, height=40)

        # Adding Label
        name_Label = Label(text="Name", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18, size_hint=(1, None), height=30)

        email_Label = Label(text="Email", font_size=18, height=30)
        self.email_input = TextInput(multiline=False, font_size=18, size_hint=(1, None), height=30)

        password_Label = Label(text="Password", font_size=18, height=30)
        self.password_input = TextInput(multiline=False, font_size=18, size_hint=(1, None), height=30)

        confirm_password_Label = Label(text="Confirm Password", font_size=18, height=30)
        self.confirm_password_input = TextInput(multiline=False, font_size=18, size_hint=(1, None), height=30)

        layout.add_widget(head_Label)
        layout.add_widget(name_Label)
        layout.add_widget(email_Label)
        layout.add_widget(password_Label)
        layout.add_widget(confirm_password_Label)
        # 
        layout.add_widget(self.name_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.confirm_password_input)
        submit_button = Button(text="Submit", font_size=18, size_hint=(1, None), height=40)





        return layout