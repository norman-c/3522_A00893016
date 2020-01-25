from item import Item


class Dvd(Item):

    def __init__(self, call_num, title, num_copies, release_date, region_code):
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._release_date = release_date
        self._region_code = region_code

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
    def release_date(self):
        return self._release_date

    @property
    def region_code(self):
        return self._region_code

    def check_availability(self):
        return super().check_availability()

    def __str__(self):
        return f"---- DVD: {self._title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
