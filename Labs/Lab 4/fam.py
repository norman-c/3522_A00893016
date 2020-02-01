from budget import Budget
from transaction_gen import TransactionGen
from user import User


class Fam:

    def __init__(self, user):
        self._user = user
        self._transaction_list = []

    def display_transaction_menu(self):
        """
        Displays menu for user to interact with
        :return:
        """
        user_input = None
        while user_input != 5:
            print("\nWelcome to the F.A.M.!")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions")
            print("4. View Bank Account Details")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5)")

            # handle user pressing only enter in menu
            if (string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                print(self._user.budget)
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                self._transaction_list.append(TransactionGen.create_transaction())
            elif user_input == 3:
                self._display_transactions()
            elif user_input == 4:
                print(self._user.display_bank())
                user_input = input("Press Enter to continue")

            elif user_input == 5:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using the F.A.M.")

    def _display_transactions(self):
        """
        Displays the transactions in the list
        :return:
        """
        print("\nTransaction List\n")
        for transaction in self._transaction_list:
            print(transaction)


def load_test_user():
    """
    Used to create Fam user for testing 
    :return:
    """
    budget = Budget(100, 100, 100, 100)
    return User("Ryan", 11, "good", 2314, "TD", 1234, budget)


def main():
    my_fam = Fam(load_test_user())
    my_fam.display_transaction_menu()


if __name__ == '__main__':
    main()
