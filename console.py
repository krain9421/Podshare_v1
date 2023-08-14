#!/usr/bin/python3
"""Console module that is entry point of command
    interpreter
"""
import cmd
import sys
import inspect
import shlex
import re
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.post import Post
from models.comment import Comment

classes = {"BaseModel": BaseModel, "User": User, "Post": Post,
            "Comment": Comment}

class PodShareCommand(cmd.Cmd):
    """ PodShare console """
    prompt = '(podshare) '

    def do_EOF(self, arg):
        """ Exits the console """
        return True

    def emptyline(self):
        """ overwrites the emptyline method """
        return False

    def do_quit(self, arg):
        """ Exits the console """
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves it to the JSON file and prints
            the id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            new_dict = self._key_value_parser(args[1:])
            print(f'new_dict {new_dict}')
            new_instance = classes[args[0]](**new_dict)
            print(new_instance.id)

    def do_createUser(self, arg):
        """Creates a User instance with a username and password"""
        args = arg.split()
        if len(args) == 0:
            print("** username missing **")
            return False
        if not re.match(r'[A-Za-z0-9]+', args[0]):
            print("** username must contain only characters and numbers ! **")
            return False
        if not args[1]:
            print("** password missing **")
            return False
        else:
            new_instance = User()
            new_instance.username = args[0]
            new_instance.passwd = args[1]
            print(new_instance.id)
            new_instance.save()

if __name__ == '__main__':
    PodShareCommand().cmdloop()
