#!/usr/bin/python3

"""define a Mylist class"""


class MyList(list):
    """
    This class inherits from the list class
    """

    def print_sorted(self):
        list_copy = self.copy()
        """
        This function prints out a sorted list
        :return: Sorted list
        """
        for num in self:
            if not isinstance(num, int):
                raise TypeError("list should be only integers")
        list_copy.sort()
        print(list_copy)
