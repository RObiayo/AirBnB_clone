#!/usr/bin/python3
"""Describes the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Rep a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""
