#!/usr/bin/python3
"""Comment module that inherits from a BaseModel."""
from models.base_model import BaseModel
from models.post import Post

# from base_model import BaseModel
# from post import Post


class Comment(Post):
    """
    Defines a PodShare comment with the following attributes.
    audioId (string)
    caption (string)
    userId (string)
    likes (list)
    numberOfPlays (int)
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Comment object"""
        super().__init__(*args, **kwargs)
