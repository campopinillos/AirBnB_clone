#!/usr/bin/python3
"""
City Module

"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City """
    state_id = ""
    name: ""

    def __init__(self, **kwargs):
        super().__init__()
