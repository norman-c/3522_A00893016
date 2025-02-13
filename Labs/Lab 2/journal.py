from item import Item


class Journal(Item):

    def __init__(self, call_num, title, num_copies, author, issue_number, publisher):
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._author = author
        self._issue_number = issue_number
        self._publisher = publisher

    def get_title(self):
        return super().get_title()

    def increment_number_of_copies(self):
        super().increment_number_of_copies()

    def decrement_number_of_copies(self):
        super().decrement_number_of_copies()

    def get_num_copies(self):
        pass

    @property
    def call_number(self):
        return self._call_num

    @property
    def author(self):
        return self._author

    @property
    def publisher(self):
        return self._publisher

    @property
    def issue_number(self):
        return self._issue_number

    def check_availability(self):
        return super().check_availability()

    def __str__(self):
        return f"---- Journal: {self._title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
