#!/usr/bin/python3

"""define a Base Class"""
import json
import csv


class Base:
    """
    represent a Base class
    """
    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiate an object of the Base class
        :param id: object id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This static method returns a json string
        list dictionary
        :param list_dictionaries: A dictionary
        :return: A list string dictionary
        """

        if list_dictionaries is None:
            return "[]"
        return f"{json.dumps(list_dictionaries)}"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method writes the json string
        to a file
        :param list_objs: A list of objects
        :return: Returns a new file with <Class name>.json
        """
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                listing = [dic.to_dictionary() for dic in list_objs]
                file.write(Base.to_json_string(listing))

    @staticmethod
    def from_json_string(json_string):
        """
        This static method returns a json string back to
        an object
        :param json_string: JSON string
        :return: object
        """

        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """

        :param dictionary:
        :return:
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 8)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of
        JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
