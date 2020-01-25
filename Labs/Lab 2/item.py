from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def get_title(self):
        """
        Returns the title of the item
        :return: a string
        """
        return self._title

    @abstractmethod
    def increment_number_of_copies(self):
        """
        Set's the number of copies of an item
        :param value: a positive integer
        """
        self._num_copies += 1

    @abstractmethod
    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an item
        :param value: a positive integer
        """
        self._num_copies -= 1

    @abstractmethod
    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific item.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num

    @abstractmethod
    def check_availability(self):
        """
        Returns True if the item is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @abstractmethod
    def __str__(self):
        pass
