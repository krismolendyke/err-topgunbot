#!/usr/bin/env python


from random import choice
import re


class TopGun(object):
    """Get random lines for various characters from TOP GUN."""
    CHARACTERS = {
        "maverick": r"MAVERICK",
        "iceman": r"ICE(MAN)?",
        "goose": r"GOOSE",
        "jester": r"JESTER",
        "viper": r"VIPER"
    }


    def __init__(self):
        super(TopGun, self).__init__()
        self.lines = {}
        for name, name_re in TopGun.CHARACTERS.iteritems():
            self.lines[name] = self.get_lines(name_re)


    def get_random(self, name):
        """Get a random line for the given character's name."""
        if name in self.lines:
            return choice(self.lines[name])
        else:
            return ("Sorry, is \"%s\" in TOP GUN?  I only know of " % name +
                    ", ".join(TopGun.CHARACTERS.keys()[:-1]) + " and " +
                    TopGun.CHARACTERS.keys()[-1] + ".")


    def get_lines(self, name):
        """Get a list of lines from the TOP GUN film script for the given
        charater's name.
        """
        BEGIN_RE = re.compile(r"^\s+%s\s+" % name)
        END_RE = re.compile(r"^\s+$")
        lines = []
        with open("topGun.txt") as f:
            in_line_block = False
            line = []
            for l in f:
                if BEGIN_RE.search(l):
                    in_line_block = True
                    line = []
                if END_RE.search(l):
                    if in_line_block and len(line):
                        lines.append(" ".join(line))
                    in_line_block = False
                if in_line_block:
                    if not BEGIN_RE.search(l):
                        sub_line = l.split(")")[-1].strip()
                        if sub_line:
                            line.append(sub_line)
        return lines


if __name__ == "__main__":
    tg = TopGun()
    print "fake: " + tg.get_random("fake")
    print "maverick: " + tg.get_random("maverick")
    print "goose: " + tg.get_random("goose")
    print "iceman: " + tg.get_random("iceman")
    print "jester: " + tg.get_random("jester")
    print "viper: " + tg.get_random("viper")
