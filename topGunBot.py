#!/usr/bin/env python


"""A bot which will respond to various TOP GUN character name commands and
mentions and respond with a random line spoken by that character in the film.
"""


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
    def iceman(self, mess, args):
        """Get a random Ice Man line."""
        return "(iceman) " + self.topgun.get_random("iceman")


    @botcmd
    def goose(self, mess, args):
        """Get a random Goose line."""
        return "(goose) " + self.topgun.get_random("goose")


    @botcmd
    def jester(self, mess, args):
        """Get a random Jester line."""
        return "(jester) " + self.topgun.get_random("jester")


    @botcmd
    def viper(self, mess, args):
        """Get a random Viper line."""
        return "(viper) " + self.topgun.get_random("viper")


    @botcmd
    def charlie(self, mess, args):
        """Get a random Charlie line."""
        return "(charlie) " + self.topgun.get_random("charlie")


    def callback_message(self, conn, mess):
        """Listen for TOP GUN mentions and interject random quotes from those
        characters who were mentioned.
        """
        message = ""
        if mess.getBody().find("(mav)") != -1:
            message = "(mav) " + self.topgun.get_random("maverick")
        if mess.getBody().find("(iceman)") != -1:
            message = "(iceman) " + self.topgun.get_random("iceman")
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
