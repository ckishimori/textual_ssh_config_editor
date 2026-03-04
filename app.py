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
        yield Input(placeholder="Host")
        yield Input(placeholder="Hostname")
        yield Input(placeholder="Username")
        yield Input(placeholder="Port")
        yield Button("Add")
        yield Footer()

    def on_mount(self):
        self.title = "Textual SSH config editor"

def main():
    app = SSHConfigEditor()
    app.run()

if __name__ == "__main__":
    main()