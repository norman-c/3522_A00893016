import abc
from abc import ABC

from book import Book
from dvd import Dvd
from journal import Journal


class ItemFactory(ABC):

    @abc.abstractmethod
    def create_item(self):
        pass


class BookFactory(ItemFactory):

    def create_item(self):
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        book_data = (call_number, title, num_copies)
        author = input("Enter Author Name: ")
        new_book = Book(book_data[0], book_data[1], book_data[2], author)

        return new_book


class DvdFactory(ItemFactory):

    def create_item(self):
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_date = input("Enter release date: ")
        region_code = input("Enter region_code: ")
        new_dvd = Dvd(call_number, title, num_copies, release_date, region_code)

        return new_dvd


class JournalFactory(ItemFactory):

    def create_item(self):
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter Author Name: ")
        issue_number = input("Enter Issue Number: ")
        publisher = input("Enter Publisher: ")
        new_journal = Journal(call_number, title, num_copies, author, issue_number, publisher)

        return new_journal
