from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, TabPane, TabbedContent, DataTable
from textual.containers import Container
from datetime import datetime, timedelta
from pytz import timezone
from art import *
import requests, dotenv, os, webbrowser

# TO DO
    # -Async request

class Website(App):
    
    CSS_PATH = "app.tcss"

    TS_CLIENT_ID = os.getenv("TS_CLIENT_ID")
    TS_CLIENT_SECRET = os.getenv("TS_CLIENT_SECRET")
    TS_TOKEN_URL = "https://api.tailscale.com/oauth/token"
    ts_access_token = None
    ts_token_expiry = None
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        # ascii art for title (next: should revert to normal text if the window is too small)
        title = Label("_|    _|  _|            _|_|_|  _|                        _|_|_|  _|        _|\n_|    _|                  _|        _|_|_|  _|_|        _|              _|_|_|\n_|_|_|_|  _|              _|        _|    _|    _|        _|_|    _|  _|    _|  \n_|    _|  _|              _|        _|    _|    _|            _|  _|  _|    _|  \n_|    _|  _|    _|      _|_|_|      _|    _|    _|      _|_|_|    _|    _|_|_|  ", id="title")
        title.border_title = "v0.0.3"
        yield title

        # subtitle
        yield Label("14 year old software/game developer, cycling enthusiast, and tech nerd\n──────────────────────────────────────────────────────────────────────", id="subtitle")

        with TabbedContent(id="allTabs"):
            with TabPane("General"):
                yield Label("", id="clock")
                yield Label("I'm currently working on this website", id = "workingOn")
            with TabPane("Devices"):
                yield DataTable(id="devicesTable")
                
        yield Footer()

    def on_click(self, event: events.Click) -> None:
        if event.control.id=="workingOn":
            webbrowser.open("https://github.com/sidsenthilexe/textual-website")



    def on_mount(self) -> None:
        self.theme = "dracula"
        # self.request_new_token()
        # self.set_interval(2700, self.check_token)
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
        zone = timezone("US/Pacific")
        now = datetime.now(zone)
        city = "Sunnyvale, CA"
        clock = f"I'm currently in {city}, and my local time is " + now.strftime("%H:%M:%S") + f".{int(now.microsecond / 100000)}"
        self.query_one("#clock", Label).update(clock)



    def request_new_token(self) -> None:
        try:
            response = requests.post(
                self.TS_TOKEN_URL,
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.TS_CLIENT_ID,
                    "client_secret": self.TS_CLIENT_SECRET,
                },
            )
            response.raise_for_status()
            token_data = response.json()
            self.ts_access_token = token_data["access_token"]
            expires_in = token_data.get("expires_in", 3600)
            self.ts_token_expiry = datetime.now() + timedelta(seconds=(expires_in-1000))
        except requests.RequestException as exception:
            print(exception)
            self.ts_access_token = None
    


    def check_token(self) -> None:
        if self.ts_access_token and self.ts_token_expiry and datetime.now() < self.ts_token_expiry:
            return
        self.request_new_token
    

if __name__ == "__main__":
    Website().run()