#!/usr/bin/python3
"""
User Module

"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User """
    email = ""
    password: ""
    first_name: ""
    last_name: ""

    def __init__(self, **kwargs):
        super().__init__()
