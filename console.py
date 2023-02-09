#!/usr/bin/python3
"""the console used to run the program in the terminal"""

import cmd
from models.basemodel import BaseModel


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
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) 
        and prints the id
        """

    def do_show(self, line):

    def do_detroy(self, line):

    def do_all(self, line):

    def do_update(self, line):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
