#!/usr/bin/python3
"""the console used to run the program in the terminal"""

import cmd


class HBNBCommand(cmd.Cmd):
    """entry point for the console"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the console"""
        return True

    def do_EOF(self, line):
        """exit the console"""
        return True

    def emptyline(self):
        """do nothing on " " + enter"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
