from pathlib import Path

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class RegistrationForm(App):
    def build(self):
        self.title = "Registration Form"
        self.users_file = Path(__file__).with_name("users.txt")

        root = BoxLayout(orientation="vertical", padding=25, spacing=12)

        header = Label(
            text="Python User Registration Form",
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=50,
        )
        root.add_widget(header)

        form = BoxLayout(orientation="vertical", spacing=10)

        self.name_input = self._create_input("Name")
        self.email_input = self._create_input("Email")
        self.password_input = self._create_input("Password", password=True)
        self.confirm_password_input = self._create_input("Confirm Password", password=True)

        form.add_widget(self.name_input)
        form.add_widget(self.email_input)
        form.add_widget(self.password_input)
        form.add_widget(self.confirm_password_input)

        submit_button = Button(text="Submit", font_size=18, size_hint=(1, None), height=45)
        submit_button.bind(on_press=self.submit_form)
        form.add_widget(submit_button)

        self.status_label = Label(text="", font_size=15, size_hint_y=None, height=40)
        form.add_widget(self.status_label)

        root.add_widget(form)
        return root

    def _create_input(self, label_text, password=False):
        field = BoxLayout(orientation="vertical", size_hint_y=None, height=70)
        label = Label(text=label_text, font_size=16, size_hint_y=None, height=25)
        input_box = TextInput(
            multiline=False,
            font_size=16,
            size_hint=(1, None),
            height=35,
            password=password,
            write_tab=False,
        )
        field.add_widget(label)
        field.add_widget(input_box)
        return field

    def submit_form(self, instance):
        name = self.name_input.children[1].text.strip()
        email = self.email_input.children[1].text.strip()
        password = self.password_input.children[1].text.strip()
        confirm_password = self.confirm_password_input.children[1].text.strip()

        if not all([name, email, password, confirm_password]):
            self.show_popup("Please fill all fields.")
            return

        if "@" not in email or "." not in email:
            self.show_popup("Please enter a valid email address.")
            return

        if len(password) < 6:
            self.show_popup("Password must be at least 6 characters long.")
            return

        if password != confirm_password:
            self.show_popup("Passwords do not match.")
            return

        with self.users_file.open("a", encoding="utf-8") as file:
            file.write(f"{name},{email},{password}\n")

        self.status_label.text = f"Registration successful for {name}!"
        self.clear_form()
        self.show_popup("Registration successful!")

    def clear_form(self):
        self.name_input.children[1].text = ""
        self.email_input.children[1].text = ""
        self.password_input.children[1].text = ""
        self.confirm_password_input.children[1].text = ""

    def show_popup(self, message):
        popup_content = Label(text=message, font_size=16, halign="center")
        popup = Popup(
            title="Message",
            content=popup_content,
            size_hint=(0.8, 0.4),
        )
        popup.open()


if __name__ == "__main__":
    RegistrationForm().run()
