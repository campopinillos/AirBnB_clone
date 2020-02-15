#!/usr/bin/python3
"""
HBNB Console

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class Console """
    prompt = '(hbnb) '
    intro = '      WELCOME!\n\
        .--. \n\
       |o_o |\n\
       |!_/ |\n\
      //   \\ \\ \n\
     (|     | ) \n\
    / \\_   _/ \\ \n\
    \\___)=(___/ \n'

    __classes = {'BaseModel': BaseModel,
                 'User': User,
                 'Place': Place,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Review': Review}

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
        if line is None or line == "":
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
        if line is None or line == "":
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

    def do_destroy(self, line):
        """Destroy command to delete a instance"""
        if line is None or line == "":
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
                del storage.all()[k]
                storage.save()

    def do_all(self, line):
        """All command prints all string representation of all instances"""
        if line != "":
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                list = [v for k, v in storage.all().items()
                        if k.split(".")[0] == line]
                print(list)
        else:
            list = [v for v in storage.all().values()]
            print(list)

    def do_update(self, line):
        """Update command load new info at the instances"""
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(' ')[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        elif len(line.split(' ')) < 3:
            print("** attribute name missing **")
        elif len(line.split(' ')) < 4:
            print("** value missing **")

    def do_all(self, line):
        """All command prints all string representation of all instances"""
        if line != "":
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                list = [str(v) for k, v in storage.all().items()
                        if k.split(".")[0] == line]
                print(list)
        else:
            list = [str(v) for v in storage.all().values()]
            print(list)

    def do_count(self, line):
        count = 0
        for k, v in storage.all().items():
            if k.split(".")[0] == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
