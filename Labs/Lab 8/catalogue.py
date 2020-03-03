import difflib

from library_item_generator import LibraryItemGenerator


class Catalogue:
    """
    Holds a list of items
    """
    def __init__(self):
        self._item_list = LibraryItemGenerator.generate_test_items()

    def add_item(self):
        """
        Add an item to the item list
        """
        self._item_list.append(LibraryItemGenerator.create_item())

    def return_item(self, call_number):
        """
        Returns an item to the list
        :param call_number: The call_number of the item to be returned
        """
        status = self._increment_item_count(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for item in self._item_list:
            if item.call_number == call_number:
                found_item = item
                break
        return found_item

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._retrieve_item_by_call_number(call_number)

        if library_item is None:
            print(f"Could not find item with call number {call_number}"
                  f". Checkout failed.")
            return
        if library_item.check_availability():

            status = self._reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def find_items(self, title):
        """
        Find an item in the list
        :param title: A string
        :return: The results if the item is in the list
        """
        title_list = []
        for library_item in self._item_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def remove_item(self, call_number):
        """
        Removes an item from the list
        :param call_number: a string
        :return: Print confirmation
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    def _reduce_item_count(self, call_number):
        """
        Reduce count of item in the list
        :param call_number: a string
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def _increment_item_count(self, call_number):
        """
        increase count of item in the list
        :param call_number: a string
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for item in self._item_list:
            print(item)
