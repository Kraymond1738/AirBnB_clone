#!/usr/bin/python3
"""programm that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.city import City
from models import storage
import shlex


Class = {"BaseModel", "Amenity", "Place", "State", "User", "Review", "City"}

Class_dict = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "Place": Place,
        "State": State,
        "User": User,
        "Review": Review,
        "City": City}


class HBNBCommand(cmd.Cmd):
    """Our AirBnB commande line interface"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """quit the programm with command quit"""
        return True

    def do_EOF(self, args):
        """quit the programm with the command EOF"""
        return True

    def emptyline(self):
        """anything to do if it is a line is Empty"""
        pass

    def do_create(self, args):
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in Class:
            print("** class doesn't exist **")
            return
        for key, value in Class_dict.items():
            if args[0] == key:
                instance = value()
                print(instance.id)
                instance.save()

    def do_show(self, args):
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in Class:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        answer = "{}.{}".format(args[0], args[1])
        if answer not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[answer])

    def do_destroy(self, args):
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in Class:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        answer = "{}.{}".format(args[0], args[1])
        storage.all().pop(answer)
        storage.save()

    def do_all(self, args):
        args = shlex.split(args)
        all_element = storage.all()
        if len(args) == 0:
            for key in all_element:
                element = all_elemnt[key].__str__
                print(element)
        elif args[0] in Class:
            for key in all_element:
                if all_element[key].__class__.__name__ == args[0]:
                    element = all_element[key].__str__
                    print(element)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
