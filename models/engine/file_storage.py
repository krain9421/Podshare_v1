#!/usr/bin/python3
"""
Module that defines the FileStorage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.post import Post
from models.comment import Comment

classes = {"User": User, "Post": Post, "Comment": Comment}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __users_path = "users.json"
    __objects = {}
    __users = {}


    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None and obj.__class__ is User:
            try:
                os.makedirs("users/{}".format(obj.username))
            except:
                pass
            key = obj.__class__.__name__ + "." + obj.id
            self.__users[key] = obj
        elif obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        json_users = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        for key in self.__users:
            json_users[key] = self.__users[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects,f)
        with open(self.__users_path, 'w') as f:
            json.dump(json_users,f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo =  json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing JSON file to objects"""
        self.reload()
