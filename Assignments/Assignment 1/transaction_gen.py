from datetime import datetime
import time

from transaction import Transaction


class TransactionGen:

    @staticmethod
    def create_transaction(b_balance):
        """
        Creates a transaction from user input
        :return: transaction object
        """
        code = 4
        timestamp = datetime.now()
        try:
            amount = int(input("Enter cost of item "
                               "(positive number): "))
        except ValueError:
            print("Invalid cost.")
            return None
        if amount > b_balance:
            print("Bank balance too low.")
            return None
        user_input = None
        while code == 4:
            print("Please select the budget category")
            print("1. Games and Entertainment")
            print("2. Clothes and Accessories")
            print("3. Eating out")
            print("4. Miscellaneous")
            string_input = input("Please enter your choice (1-4)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue
            user_input = int(string_input)
            if user_input == 1:
                code = 0
            elif user_input == 2:
                code = 1
            elif user_input == 3:
                code = 2
            elif user_input == 4:
                code = 3

        store = input("Enter store name: ")

        return Transaction(timestamp, amount, store, code)
