#!/usr/bin/python3
""" a consol to create and update objects"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the console class"""
    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    prompt = "(hbnb) "

    def readline(self):
        return input(self.prompt)

    def default(self, lines):
        """the cmds's default method to manipulate
        commands with this form <class_name>.<method>"""
        line = lines.split('.')
        all_count = {
            "all()": self.do_all,
            "count()": self.do_count
        }

        if line[0] in self.class_mapping:
            if line[1] in all_count:
                all_count[line[1]](f"{line[0]} {line[1]}")
            elif line[1].startswith("show"):
                show_id = line[1].split('"')[1]
                self.do_show(f"{line[0]} {show_id}")
            elif line[1].startswith("destroy"):
                destr_id = line[1].split('"')[1]
                self.do_destroy(f"{line[0]} {destr_id}")
            elif line[1].startswith("update"):
                update_args = line[1].split('"')
                update_class = line[0]
                update_id = update_args[1]
                update_attr = update_args[3]
                update_value = update_args[5]
                self.do_update(f"{update_class} {update_id}"
                               f"{update_attr} {update_value}")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """handling ENTER"""
        pass

    def do_EOF(self, arg):
        """handling ctrl+D"""
        return True

    def do_create(self, arg):
        """creates a new instance of a specified class and prints its ID"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]

        if class_name in HBNBCommand.class_mapping:
            obj = HBNBCommand.class_mapping[class_name]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = arg.split()
        if not args:
            objects = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in self.class_mapping:
                print("** class doesn't exist **")
                return
            objects = [obj for obj in storage.all().values()
                       if obj.__class__.__name__ == class_name]
        formatted_objects = []
        for obj in objects:
            formatted_objects.append(f"[{str(obj)} {obj.to_dict()}]")
        for formatted_obj in formatted_objects:
            print(formatted_obj)

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        Usage: <class name>.count()
        Example: User.count()
        """
        count = len([val for key, val in storage.all().items() if
                     key.startswith(arg[0])])
        print(count)

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating an attribute
        (save the change into the JSON file).
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        instance = storage.all()[key]

        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]

        if attribute_name in ["id", "created_at", "updated_at"]:
            return
        try:
            attr = getattr(instance, attribute_name, None)
        except Exception:
            pass

        value = str(value)
        value = value.strip('"')
        if attr is not None:
            if isinstance(attr, int):
                value = int(value)
            if isinstance(attr, float):
                value = float(value)
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        setattr(instance, attribute_name, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
