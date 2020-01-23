from item import Item


class Dvd(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._release_date = release_date
        self._region_code = region_code

    def get_title(self):
        pass

    def increment_number_of_copies(self):
        pass

    def decrement_number_of_copies(self):
        pass

    def get_num_copies(self):
        pass

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

    @property
    def release_date(self):
        return self._release_date

    @property
    def region_code(self):
        return self._region_code

    # @call_number.setter
    # def call_number(self, value):
    #     """
    #     This is the decorator way to create a SET property. This would
    #     allow us to invoke this method by simply saying
    #     my_book.call_number = "102.345.992". I've commented this out
    #     since call numbers should not need a setter.
    #     :param value: a string
    #     :precondition value: a unique call number identifier
    #     """
    #     self._call_num = value

    def check_availability(self):
        pass

    def __str__(self):
        return f"---- DVD: {self._title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
