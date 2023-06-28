#!/usr/bin/python3
"""
    defines a square class
"""


class Square:
    """
        Represent a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """initialize with a private instance size
        and an optional argument

        Args:
            size(int): The size of new square
        Returns:
            The return value. true for success, false for otherwise
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Retrieve the value
        :return: Returns the correct output
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        set the correct input
        :param value: object size instance value
        :return: return true for success. 0 for otherwise
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the value
        :return: Returns the correct output
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
            set the correct input
            :param value: object size instance value
            :return: return true for success. 0 for otherwise
        """

        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculate the area of the square
        :return: returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints to standard output the square as chr #
        :return: true if success. 0 for otherwise
        """
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
