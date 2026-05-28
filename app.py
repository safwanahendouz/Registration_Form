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
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        head_label = Label(text="Registration Form", font_size=26, bold=True, height=40)
        # Adding label
        name_label = Label(text="Name:", font_size=18, height=30)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_label = Label(text="Email:", font_size=18, height=30)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_label = Label(text="Password:", font_size=18, height=30)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirm_label = Label(text="Confirm Password:", font_size=18, height=30)
        self.confirm_input = TextInput(multiline=False, font_size=18, password=True)

        # Adding widgets to layout
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)

        # Submit button
        submit_button = Button(text="Submit", font_size=18, height=50)
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)

        return layout

    def on_submit(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm = self.confirm_input.text

        # Validate inputs
        if not name or not email or not password or not confirm:
            self.show_popup("Error", "All fields are required!")
            return

        if password != confirm:
            self.show_popup("Error", "Passwords do not match!")
            return

        # Success
        self.show_popup("Success", f"Registration completed!\nName: {name}\nEmail: {email}")
        self.clear_inputs()

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message, font_size=16))
        
        close_button = Button(text="Close", size_hint_y=0.3)
        popup_layout.add_widget(close_button)
        
        popup = Popup(title=title, content=popup_layout, size_hint=(0.9, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def clear_inputs(self):
        self.name_input.text = ""
        self.email_input.text = ""
        self.password_input.text = ""
        self.confirm_input.text = ""


if __name__ == '__main__':
    RegistrationForm().run()

    