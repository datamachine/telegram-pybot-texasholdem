
import plugintypes

class TexasHoldEmPlugin(plugintypes.TelegramPlugin):
    patterns = {
        "^!command": "callback",
    }

    usage = [
        "!command: Help here",
    ]

    def callback(self, msg, matches):
        return "Response Here"

