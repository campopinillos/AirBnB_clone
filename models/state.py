#!/usr/bin/python3
"""
State Module

"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State City """
    name: ""

    def __init__(self, **kwargs):
        super().__init__()
