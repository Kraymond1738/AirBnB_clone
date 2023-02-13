#!/usr/bin/python3
"""the console used to run the program in the terminal"""

import cmd
from models.basemodel import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        pass

    def do_show(self, line):
        pass

    def do_detroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
