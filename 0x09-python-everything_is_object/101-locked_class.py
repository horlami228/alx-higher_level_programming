#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating a new LockedClass attributes
    for anything except attributes called "first_name".
    """

    __slots__ = ["first_name"]
