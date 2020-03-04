from abc import ABC

from item import Item


class Journal(Item, ABC):

    def __init__(self, author, issue_number, publisher, **kwargs):
        super().__init__(**kwargs)
        self._issue_number = issue_number
        self._publisher = publisher
        self._author = author

    @property
    def author(self):
        return self._author

    @property
    def publisher(self):
        return self._publisher

    @property
    def issue_number(self):
        return self._issue_number

    def __str__(self):
        return f"---- Journal: {self._title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self._author}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
