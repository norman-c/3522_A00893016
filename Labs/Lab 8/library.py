""" This module houses the library"""
from book import Book
import difflib

from catalogue import Catalogue
from dvd import Dvd


class Library:
    """
    The Library consists of a catalogue and an
    interface for users to check out, return and find books.
    """

    def __init__(self, catalogue):
        """
        Intialize the library with a catalogue
        :param catalogue: catalogue object
        """
        self._catalogue = catalogue

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove aa item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if (string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._catalogue.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self._catalogue.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self._catalogue.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self._catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    lib_catalogue = Catalogue()
    my_epic_library = Library(lib_catalogue)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
