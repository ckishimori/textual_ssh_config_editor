from sshconf import read_ssh_config
from os.path import expanduser
from textual.app import App
from textual.widgets import (
    Button,
    Footer,
    Header,
    Input
)

class SSHConfigEditor(App):
    def compose(self):
        yield Header()
        yield Input(placeholder="Host", id="host_field")
        yield Input(placeholder="Hostname", id="hostname_field")
        yield Input(placeholder="Username", id="username_field")
        yield Input(placeholder="Port", id="port_field")
        yield Button("Add", id="add_button")
        yield Footer()

    def on_mount(self):
        self.title = "Textual SSH config editor"

    def on_button_pressed(self, event):
        if event.button.id == "add_button":
            print(self.query_one("#host_field").value)

def main():
    app = SSHConfigEditor()
    app.run()

if __name__ == "__main__":
    main()