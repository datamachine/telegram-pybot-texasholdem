from telex.plugin import TelexPlugin

class TexasHoldEmPlugin(TelexPlugin):
    patterns = {
        "^!command": "callback",
    }

    usage = [
        "!command: Help here",
    ]

    def callback(self, msg, matches):
        return "Response Here"

