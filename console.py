#!/usr/bin/python3
"""
HBNB Console

"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '
    intro = "Welcome!"
    __classes = {'BaseModel': BaseModel}

    def emptyline(self):
        """Empty line execution"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create command new instance"""
        if line is None:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.__classes[line]()
            obj.save()
            print(obj.id)
            storage.save()

    def do_show(self, line):
        """Show command display info of the id instance"""
        if line is None:
            print("** class name missing **")
        elif line.split(' ')[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(line.split(' ')[0], line.split(' ')[1])
            if k not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[k])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
