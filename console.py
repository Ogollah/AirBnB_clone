#!/usr/bin/env python3
import cmd
"""
HBNBCommand class.
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter using Ctrl-D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
