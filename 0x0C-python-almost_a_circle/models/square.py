#!/usr/bin/python3
"""define a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square class that inherits
    from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiate a new square object
        :param size: square size
        :param x: x value
        :param y: y value
        :param id: square id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square object"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} " \
               f"- {self.size}"

    def update(self, *args, **kwargs):
        """
        This method can be used to update the attributes
        :param args: Variable optional arguments
        :return:
        """
        tab = 0
        if args and len(args) != 0:
            for arg in args:
                if tab == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if tab == 1:
                    self.size = arg
                if tab == 2:
                    self.x = arg
                if tab == 3:
                    self.y = arg
                tab += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        This method returns a dictionary representation of the object
        :return: A dictionary
        """

        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
