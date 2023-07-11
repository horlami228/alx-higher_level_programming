#!/usr/bin/python3
"""A class student that defines a student"""


class Student:
    """
    This class defines Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the class object
        :param first_name: First name
        :param last_name: Last name
        :param age: Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary description with simple data structure
        :return: Returns a dictionary
        """
        dic = {}
        for keys, values in self.__dict__.items():
            if isinstance(values, (int, list, dict, str, bool)):
                dic[keys] = values
        return dic
