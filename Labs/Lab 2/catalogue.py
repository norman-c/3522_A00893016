import difflib
from book import Book
from library_item_generator import LibraryItemGenerator

class Catalogue:

    def __init__(self):
        self._item_list = LibraryItemGenerator.generate_test_items()

    def add_item(self):
        self._item_list.append(LibraryItemGenerator.create_item())

    def find_books(self, title):
        title_list = []
        for library_book in self._book_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def remove_book(self, call_number):
        found_book = self._retrieve_book_by_call_number(call_number)
        if found_book:
            self._book_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def reduce_book_count(self, call_number):
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_book_count(self, call_number):

        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        else:
            return False

    def display_available_books(self):
        """
        Display all the books in the library.
        """
        print("Books List")
        print("--------------", end="\n\n")
        for item in self._item_list:
            print(item)
