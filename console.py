#!/usr/bin/python3
"""programm that contains the entry point of the command interpreter"""
import cmd
class HBNBCommand(cmd.Cmd):
    """Our AirBnB commande line interface"""
    prompt = '(hbnb)'
    def do_quit(self,args):
        """quit the programm with command quit"""
        return True
    
    def do_EOF(self,args):
        """quit the programm with the command EOF"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
