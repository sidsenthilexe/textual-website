from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Label, Digits, LoadingIndicator
from textual.containers import Container
from datetime import datetime
from pytz import timezone

class Website(App):
    CSS_PATH = "app.tcss"

    def on_mount(self) -> None:
        self.theme = "dracula"
        self.set_interval(0.1, self.update_clock)
        self.title = "Sid's Website"
        self.sub_title = "Built with Textual"
    
    def compose(self) -> ComposeResult:
        # yield LoadingIndicator()
        yield Header()

        lbl = Label("👋 Hi, I'm Sid!", id="header")
        lbl.border_title = "v0.0.1"
        yield lbl

        yield Label("14 year old software/game developer, cycling enthusiast, and tech nerd", id="subtitle")

        yield Label("", id="clock")

        yield Footer()

    def update_clock(self) -> None:
        pacific = timezone("US/Pacific")
        now = datetime.now(pacific)
        city = "Sunnyvale, CA"
        clock = f"I'm currently in {city}, and my local time is " + now.strftime("%H:%M:%S") + f".{int(now.microsecond / 100000)}"
        self.query_one("#clock", Label).update(clock)

if __name__ == "__main__":
    Website().run()