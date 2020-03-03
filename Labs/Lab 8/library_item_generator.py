from book import Book
from dvd import Dvd
from journal import Journal
from factory import BookFactory
from factory import JournalFactory
from factory import DvdFactory


class LibraryItemGenerator:

    @staticmethod
    def generate_test_items():
        """
        Return a list of items with dummy data.
        :return: a list
        """
        kwargs1 = {"call_num": "100.200.300", "title": "Harry Potter 1", "num_copies": 2}
        kwargs2 = {"call_num": "425.63.775", "title": "Toy Story", "num_copies": 2}
        kwargs3 = {"call_num": "874.234.863", "title": "Science Journal", "num_copies": 5}
        item_list = [
            Book("J K Rowling", **kwargs1),
            Dvd("10-10-2004", "NA", **kwargs2),
            Journal("Dr. Smart", 7, "Pearsons", **kwargs3)
        ]
        return item_list

    @staticmethod
    def create_item(self):
        """
        Gets user input to create item
        :return: item
        """
        print("What item are you adding?")
        print("1. Book")
        print("2. Journal")
        print("3. Dvd")
        string_input = input("Please enter your choice (1-3)")

        user_input = int(string_input)
        if user_input == 1:
            return BookFactory.create_item(self)
        if user_input == 2:
            return JournalFactory.create_item(self)
        if user_input == 3:
            return DvdFactory.create_item(self)

    # @staticmethod
    # def __create_book():
    #     """
    #     Creates a book
    #     :return: book
    #     """
    #     call_number = input("Enter Call Number: ")
    #     title = input("Enter title: ")
    #     num_copies = int(input("Enter number of copies "
    #                            "(positive number): "))
    #     book_data = (call_number, title, num_copies)
    #     author = input("Enter Author Name: ")
    #     new_book = Book(book_data[0], book_data[1], book_data[2], author)
    #
    #     return new_book
    #
    # @staticmethod
    # def __create_journal():
    #     """
    #     Creates a journal
    #     :return: a journal
    #     """
    #     call_number = input("Enter Call Number: ")
    #     title = input("Enter title: ")
    #     num_copies = int(input("Enter number of copies "
    #                            "(positive number): "))
    #     author = input("Enter Author Name: ")
    #     issue_number = input("Enter Issue Number: ")
    #     publisher = input("Enter Publisher: ")
    #     new_journal = Journal(call_number, title, num_copies, author, issue_number, publisher)
    #
    #     return new_journal
    #
    # @staticmethod
    # def __create_dvd():
    #     """
    #     Creates a dvd
    #     :return: a dvd
    #     """
    #     call_number = input("Enter Call Number: ")
    #     title = input("Enter title: ")
    #     num_copies = int(input("Enter number of copies "
    #                            "(positive number): "))
    #     release_date = input("Enter release date: ")
    #     region_code = input("Enter region_code: ")
    #     new_dvd = Dvd(call_number, title, num_copies, release_date, region_code)
    #
    #     return new_dvd
