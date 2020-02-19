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
        print()
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
        else:
            k = "{}.{}".format(line.split(' ')[0], line.split(' ')[1])
            if k not in storage.all():
                print("** no instance found **")
            else:
                """if type(getattr(storage.all()[k], attr)) is int"""
                attr = line.split()[2]
                v = line.split()[3]
                setattr(storage.all()[k], attr, v)
                storage.save()

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
        """Count command counts the instances of a class"""
        count = 0
        for k, v in storage.all().items():
            if k.split(".")[0] == line:
                count += 1
        print(count)

    def default(self, line):
        """Default command"""
        if len(line.split('.')) == 2:
            lines = line.split('.')
            if lines[1] == "all()":
                self.do_all(lines[0])
            elif lines[1] == "count()":
                self.do_count(lines[0])
            elif lines[1][0:5] == "show(" and lines[1][-1:] == ")":
                self.do_show(lines[0] + " " + lines[1][5:-1])
            elif lines[1][0:8] == "destroy(" and lines[1][-1:] == ")":
                self.do_destroy(lines[0] + " " + lines[1][8:-1])
            elif lines[1][0:7] == "update(" and lines[1][-1:] == ")":
                l_attr = lines[1][7:-1].split(", ")
                s_attr = str(lines[0])
                if l_attr[1][:1] == "{":
                    l_attr = lines[1][7:-2].split(", {")
                    print(l_attr[0])
                    print(l_attr[1])
                    d_attr = eval("{" + l_attr[1])
                    print(d_attr)
                    for k, v in d_attr.items():
                        s_attr = s_attr + " " + k + " " + str(v)
                        self.do_update(s_attr)
                else:
                    for i in l_attr:
                        s_attr = s_attr + " " + i
                    self.do_update(s_attr)

        else:
            return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
