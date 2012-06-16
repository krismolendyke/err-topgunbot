from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd

from topGun import TopGun


class TopGunBot(BotPlugin):
    def __init__(self):
        super(BotPlugin, self).__init__()
        self.topgun = TopGun()


    @botcmd
    def mav(self, mess, args):
        """Get a random Maverick line."""
        return "(mav) " + self.topgun.get_random("maverick")


    @botcmd
    def ice(self, mess, args):
        """Get a random Ice Man line."""
        return "(iceman) " + self.topgun.get_random("iceman")


    def callback_message(self, conn, mess):
        """Listen for TOP GUN mentions and interject random quotes."""
        message = ""
        if mess.getBody().find("(mav)") != -1:
            message = "(mav) " + self.topgun.get_random("maverick")
        if mess.getBody().find("(iceman)") != -1:
            message = "(iceman) " + self.topgun.get_random("iceman")
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
