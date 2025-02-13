from abc import ABC

from item import Item


class Book(Item, ABC):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, author, **kwargs):
        super().__init__(**kwargs)
        self._author = author

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"---- Book: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self.author}"
