#!/usr/bin/python3
""" a consol to create and update objects"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the consol class"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """handling ENTR+"""
        pass

    def do_EOF(self, args):
        """handling ctrl+D"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
