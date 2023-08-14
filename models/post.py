#!/usr/bin/python3
"""Post module that inherits from a BaseModel."""
from models.base_model import BaseModel
# from base_model import BaseModel

class Post(BaseModel):
    """
    Defines a PodShare post with the following attributes.
    audioId (string)
    caption (string)
    userId (string)
    likes (list)
    numberOfPlays (int)
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Post object"""
        super().__init__(*args, **kwargs)
        self.audioId = ""
        self.caption = ""
        self.userId = ""
        self.likes = []
        self.numberOfPlays = 0

    
