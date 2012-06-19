#!/usr/bin/env python


"""A bot which will respond to various TOP GUN character name commands and
mentions and respond with a random line spoken by that character in the film.
"""
from copy import copy
from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd

from topGun import TopGun

CHARACTERS =['maverick', 'iceman', 'goose', 'jester', 'viper', 'charlie', ]

def generate(character):
    f = lambda self, mess, args: "(%s) "% character + self.topgun.get_random(character)
    f.__name__ = character
    f.__doc__ = "Get a random quote from %s" % character
    return f

class TopGunBotBuilder(type):
    def __new__(mcs, name, bases, classDict):
        newClassDict = dict(classDict.items() + [(character,botcmd(generate(character))) for character in CHARACTERS])
        return super(TopGunBotBuilder, mcs).__new__(mcs, name, bases, newClassDict)

class TopGunBot(BotPlugin):
    __metaclass__ = TopGunBotBuilder

    def __init__(self):
        super(BotPlugin, self).__init__()
        self.topgun = TopGun()

    @botcmd
    def mav(self, mess, args):
        """Alias for maverick"""
        return self.maverick(mess, args)


    def callback_message(self, conn, mess):
        """Listen for TOP GUN mentions and interject random quotes from those
        characters who were mentioned.
        """
        message = ""
        if mess.getBody().find("(mav)") != -1:
            message = "(mav) " + self.topgun.get_random("maverick")
        else:
            for character in CHARACTERS:
                if mess.getBody().find('(%s)' % character) != -1:
                    message = '(%s) ' % character + self.topgun.get_random(character)
                    break
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
