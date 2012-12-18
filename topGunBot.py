#!/usr/bin/env python


"""A bot which will respond to various TOP GUN character name commands and
mentions and respond with a random line spoken by that character in the film.
"""

from errbot import BotPlugin, botcmd
from errbot.utils import get_sender_username
import config
import logging

from topGun import TopGun


def generate(character):
    f = lambda self, mess, args: "(%s) %s" % (character,
            self.topgun.get_random(character))
    f.__name__ = character
    f.__doc__ = "Get a random quote from %s." % character.title()
    return f


class TopGunBotBuilder(type):
    def __new__(mcs, name, bases, classDict):
        newClassDict = dict(classDict.items() +
                            [(character, botcmd(generate(character)))
                            for character in TopGun.CHARACTERS])
        return super(TopGunBotBuilder, mcs).__new__(mcs, name, bases,
                                                    newClassDict)


class TopGunBot(BotPlugin):
    __metaclass__ = TopGunBotBuilder
    min_err_version = "1.6.0"


    def __init__(self):
        super(BotPlugin, self).__init__()
        self.topgun = TopGun()


    def callback_message(self, conn, mess):
        """Listen for TOP GUN mentions and interject random lines from those
        characters who were mentioned.
        """
        if (mess.getFrom().getStripped() == config.BOT_IDENTITY["username"]) or (get_sender_username(mess) == config.CHATROOM_FN):
            logging.debug("Ignore a message from myself")
            return False

        message = ""
        for character in TopGun.CHARACTERS:
            if mess.getBody().find("(%s)" % character) != -1:
                message += "(%s) %s  " % (character, self.topgun.get_random(character))
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
