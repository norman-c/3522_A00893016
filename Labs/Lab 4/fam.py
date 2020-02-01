from user import User


class Fam:

    def __init__(self, user):
        self._transaction_list
        self._user = user

    def display_transaction_menu(self):
        user_input = None
        while user_input != 5:
            print("\nWelcome to the F.A.M.!")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5)")

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
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using the F.A.M.")

    def main():
        """
        Creates a library with dummy data and prompts the user for input.
        """
        new_user = User("Ryan",11,"good",2314,"TD", 1234 , budget)
        my_fam = Fam(new_user)
        my_fam.display_transaction_menu()

    if __name__ == '__main__':
        main()
