from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def __init__(self, call_num, title, num_copies, ):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    @property
    def title(self):
        return self._title
    #
    # @title.setter
    # def title(self, value):
    #     self.title = value

    def increment_number_of_copies(self):
        super().increment_number_of_copies()

    def decrement_number_of_copies(self):
        super().decrement_number_of_copies()

    @property
    def num_copies(self):
        return self._num_copies

    @property
    def call_number(self):
        return self._call_num
    #
    # @call_number.setter
    # def call_number(self, value):
    #     self._call_num = value

    @property
    def author(self):
        return self._author

    def check_availability(self):
        return super().check_availability()

    @abstractmethod
    def __str__(self):
        pass
