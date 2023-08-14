#!/usr/bin/python3
"""User module that inherits from a BaseModel."""
# from models.base_model import BaseModel
from models.base_model import BaseModel
from models.post import Post

class User(BaseModel):
    """
    Defines a User class that inherits from BaseModel with the following attributes.
    username (string)
    email (string)
    *password (string)
    first_name (string)
    last_name (string)
    posts (dict)
    followers (list)
    following (list)
    likes (dict)
    lists (dict)
    """

    def __init__(self, *args, **kwargs):
        """Initializes a user object"""
        super().__init__(*args, **kwargs)
        self.username = ""
        self.email = ""
        self.passwd = ""
        self.first_name = ""
        self.last_name = ""
        self.posts = {}
        self.followers = []
        self.following = []
        self.likes = {}
        self.lists = {}

    def createPost(self, caption=None):
        """Creates a PodShare post for a user"""
        new_Post = Post()
        new_Post.audioId = None
        new_Post.userId = self.id
        if caption is None:
            print("Posts must have a caption\n")
        else:
            new_Post.caption = caption

        key = "[{:s}].{:s}".format(new_Post.__class__.__name__, new_Post.id)
        value = new_Post.to_dict()
        self.posts[key] = value
