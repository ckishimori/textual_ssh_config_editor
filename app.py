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

    def __init__(self, conf):
        super().__init__()
        self.conf = conf

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
            self.conf.add(
                self.query_one("#host_field").value,
                HostName=self.query_one("#hostname_field").value,
                User=self.query_one("#username_field").value,
                Port=self.query_one("#port_field").value
            )
            self.conf.save()

def main():
    conf = read_ssh_config(expanduser("~/.ssh/config"))
    app = SSHConfigEditor(conf)
    app.run()

if __name__ == "__main__":
    main()