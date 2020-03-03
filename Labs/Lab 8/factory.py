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
        author = input("Enter Author Name: ")
        kwargs = {"call_num": call_number, "title": title, "num_copies": num_copies}
        new_book = Book(author, **kwargs)

        return new_book


class DvdFactory(ItemFactory):

    def create_item(self):
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_date = input("Enter release date: ")
        region_code = input("Enter region_code: ")
        kwargs = {"call_num": call_number, "title": title, "num_copies": num_copies}
        new_dvd = Dvd(release_date, region_code, **kwargs)

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
        kwargs = {"call_num": call_number, "title": title, "num_copies": num_copies}
        new_journal = Journal(author, issue_number, publisher, kwargs)

        return new_journal
