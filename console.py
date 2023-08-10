import cmd
from models import *
from models.engines import FileStorage

class HBNBCommand(cmd.Cmd):
    print("implementation")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
