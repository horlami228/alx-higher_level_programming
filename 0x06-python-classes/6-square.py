#!/usr/bin/python3
"""define a square class"""


class Square:
    """creates a square instance"""

    def __init__(self, size=0, position=(0, 0)):

        """ Initialize a square instance
        Args:
            size(int): size of the square
            position(int, int): width position
        Returns:
            returns value. true for sucess. false for otherwise
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """to retrieve the value"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve postion value"""

        return self.__position

    @position.setter
    def position(self, value):
        if(not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """print to stdout the square with #"""

        if self.__size == 0:
            print()

        for i in range(0, self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
