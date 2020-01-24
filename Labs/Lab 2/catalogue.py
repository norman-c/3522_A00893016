import difflib
from book import Book
from library_item_generator import LibraryItemGenerator

class Catalogue:

    def __init__(self, item_list):
        self._item_list = item_list

    def add_item(self):
        self._item_list.append(LibraryItemGenerator.create_item())

    def add_book(self):
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        book_data = (call_number, title, num_copies)
        author = input("Enter Author Name: ")
        new_book = Book(book_data[0], book_data[1], book_data[2], author)

        found_book = self._retrieve_book_by_call_number(
            new_book.call_number)
        if found_book:
            print(f"Could not add book with call number "
                  f"{new_book.call_number}. It already exists. ")
        else:
            self._book_list.append(new_book)
            print("book added successfully! book details:")
            print(new_book)

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
