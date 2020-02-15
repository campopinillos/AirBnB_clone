#!/usr/bin/python3
"""
Amenity Module

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity City """
    name: ""

    def __init__(self, **kwargs):
        super().__init__()
