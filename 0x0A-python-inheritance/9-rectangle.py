BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Inherited from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Define a Rectangle object
    """

    def __init__(self, width, height):
        """
        Initializing a new Rectangle object
        :param width: Rectangle width
        :param height: Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Get area
        :return: The area of rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Return a string representation for the class
        :return: A string
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
