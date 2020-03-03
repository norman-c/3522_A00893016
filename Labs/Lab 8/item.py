from abc import ABC, abstractmethod


class Item(ABC):

    @property
    def title(self):
        pass

    @title.setter
    def title(self, value):
        self._title = value

    def increment_number_of_copies(self):
        super().increment_number_of_copies()

    def decrement_number_of_copies(self):
        super().decrement_number_of_copies()

    @property
    def num_copies(self):
        pass

    @property
    def call_number(self):
        return self._call_num

    @call_number.setter
    def call_number(self, value):
        self._call_num = value

    def check_availability(self):
        return super().check_availability()

    @abstractmethod
    def __str__(self):
        pass
