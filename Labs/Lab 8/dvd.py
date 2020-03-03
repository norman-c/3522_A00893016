from item import Item


class Dvd(Item):

    def __init__(self, call_num, title, num_copies, release_date, region_code):
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code


    @property
    def release_date(self):
        return self._release_date

    @property
    def region_code(self):
        return self._region_code


    def __str__(self):
        return f"---- DVD: {self._title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
