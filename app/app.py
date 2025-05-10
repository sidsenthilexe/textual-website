from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, TabPane, TabbedContent, DataTable
from textual.containers import Container
from datetime import datetime
from pytz import timezone
from art import *

class Website(App):
    
    CSS_PATH = "app.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        # ascii art for title (next: should revert to normal text if the window is too small)
        title = Label("_|    _|  _|            _|_|_|  _|                        _|_|_|  _|        _|\n_|    _|                  _|        _|_|_|  _|_|        _|              _|_|_|\n_|_|_|_|  _|              _|        _|    _|    _|        _|_|    _|  _|    _|  \n_|    _|  _|              _|        _|    _|    _|            _|  _|  _|    _|  \n_|    _|  _|    _|      _|_|_|      _|    _|    _|      _|_|_|    _|    _|_|_|  ", id="title")
        title.border_title = "v0.0.2"
        yield title

        # subtitle
        yield Label("14 year old software/game developer, cycling enthusiast, and tech nerd\n──────────────────────────────────────────────────────────────────────", id="subtitle")

        with TabbedContent(id="allTabs"):
            with TabPane("General"):
                yield Label("", id="clock")
            with TabPane("Devices"):
                yield DataTable(id="devicesTable")
                
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "dracula"
        self.set_interval(0.1, self.update_clock)
        self.title = "Sid's Website"
        self.sub_title = "Built with Textual"

        table = self.query_one("#devicesTable", DataTable)
        table.add_columns("STATUS", "NAME", "TYPE", "LAST SEEN")
        table.add_rows(
            [
                ["up", "gondor", "MSI Katana GF66 11UE", "now"],
                ["down", "palantir", "iPhone SE (2nd generation)", "22:02"]
            ]
            )

    def update_clock(self) -> None:
        pacific = timezone("US/Pacific")
        now = datetime.now(pacific)
        city = "Sunnyvale, CA"
        clock = f"I'm currently in {city}, and my local time is " + now.strftime("%H:%M:%S") + f".{int(now.microsecond / 100000)}"
        self.query_one("#clock", Label).update(clock)

if __name__ == "__main__":
    Website().run()