from budget import Budget
from transaction_gen import TransactionGen
from user import Angel
from user import Rebel
from user import TroubleMaker


class Fam:

    def __init__(self, user):
        self._user = user
        self._transaction_list = []

    def display_fam_menu(self):
        """
        Displays menu for user to interact with
        :return:
        """
        lockCounter = 0
        user_input = None
        while user_input != 5:
            if isinstance(self._user, Rebel) and self._user.locked:
                print("Account has been locked. Exiting program.")
                break
            else:
                print("\nWelcome to the F.A.M.!")
                print("-----------------------")
                print("1. View Budgets")
                print("2. Record a Transaction")
                print("3. View Transactions by Budget")
                print("4. View Bank Account Details")
                print("5. Quit")
                string_input = input("Please enter your choice (1-5)")

                # handle user pressing only enter in menu
                if string_input == '':
                    continue

                user_input = int(string_input)

                if user_input == 1:
                    self._user.display_budgets()
                    user_input = input("Press Enter to continue")
                elif user_input == 2:
                    transaction = TransactionGen.create_transaction(self._user.b_balance)
                    if transaction is None:
                        print("Transaction canceled.")
                    else:
                        amount = transaction.amount
                        budget_code = transaction.budget_code
                        if budget_code == 0:
                            if isinstance(self._user, Angel):
                                self._transaction_list.append(transaction)
                                self._user._b_balance = self._user.b_balance - amount
                                ninety = 0.1 * self._user.budgets[0].total
                                self._user.budgets[0].amount = self._user.budgets[0].amount - amount
                                if self._user.budgets[0].amount < 0:
                                    print("You have exceeded the budget for games and entertainment.")
                                elif self._user.budgets[0].amount < ninety:
                                    print("You have exceeded more than 90% of the budget for games and entertainment.")
                            elif isinstance(self._user, TroubleMaker):
                                if self._user.budgets[0].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    seventyFive = 0.25 * self._user.budgets[0].total
                                    oneTwenty = -0.20 * self._user.budgets[0].total
                                    self._user.budgets[0].amount = self._user.budgets[0].amount - amount
                                    if self._user.budgets[0].amount < oneTwenty:
                                        print(
                                            "You have exceeded more than 120% of the budget for games and "
                                            "entertainment.")
                                        print("You are now locked out of conducting transactions for games and "
                                              "entertainment.")
                                        self._user.budgets[0].locked = True
                                    elif self._user.budgets[0].amount < 0:
                                        print("You have exceeded the budget for games and entertainment.")
                                    elif self._user.budgets[0].amount < seventyFive:
                                        print(
                                            "You have exceeded more than 75% of the budget for games and entertainment.")
                            elif isinstance(self._user, Rebel):
                                if self._user.budgets[0].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    fifty = 0.50 * self._user.budgets[0].total
                                    self._user.budgets[0].amount = self._user.budgets[0].amount - amount
                                    if self._user.budgets[0].amount < self._user.budgets[0].total:
                                        print("You have exceeded the budget for games and entertainment!!!")
                                        print("You are now locked out for games and entertainment.")
                                        self._user.budgets[0].locked = True
                                        lockCounter = lockCounter + 1
                                        if lockCounter == 2:
                                            self._user.locked = True
                                    elif self._user.budgets[0].amount < fifty:
                                        print(
                                            "You have exceeded more than 50% of the budget for games and entertainment.")

                        elif budget_code == 1:
                            if isinstance(self._user, Angel):
                                self._transaction_list.append(transaction)
                                self._user._b_balance = self._user.b_balance - amount
                                ninety = 0.1 * self._user.budgets[1].total
                                self._user.budgets[1].amount = self._user.budgets[1].amount - amount
                                if self._user.budgets[1].amount < 0:
                                    print("You have exceeded the budget for clothing and accessories.")
                                elif self._user.budgets[1].amount < ninety:
                                    print("You have exceeded more than 90% of the budget for clothing and accessories.")
                            elif isinstance(self._user, TroubleMaker):
                                if self._user.budgets[1].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    seventyFive = 0.25 * self._user.budgets[1].total
                                    oneTwenty = -0.20 * self._user.budgets[1].total
                                    self._user.budgets[1].amount = self._user.budgets[1].amount - amount
                                    if self._user.budgets[1].amount < oneTwenty:
                                        print(
                                            "You have exceeded more than 120% of the budget for clothing and "
                                            "accessories.")
                                        print(
                                            "You are now locked out of conducting transactions for clothing and "
                                            "accessories.")
                                        self._user.budgets[1].locked = True
                                    elif self._user.budgets[1].amount < 0:
                                        print("You have exceeded the budget for clothing and accessories.")
                                    elif self._user.budgets[1].amount < seventyFive:
                                        print(
                                            "You have exceeded more than 75% of the budget for clothing and "
                                            "accessories.")
                            elif isinstance(self._user, Rebel):
                                if self._user.budgets[1].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    fifty = 0.50 * self._user.budgets[1].total
                                    self._user.budgets[1].amount = self._user.budgets[1].amount - amount
                                    if self._user.budgets[1].amount < self._user.budgets[1].total:
                                        print("You have exceeded the budget for clothing and accessories!!")
                                        print("You are now locked out for clothing and accessories.")
                                        self._user.budgets[1].locked = True
                                        lockCounter = lockCounter + 1
                                        if lockCounter == 2:
                                            self._user.locked = True
                                    elif self._user.budgets[1].amount < fifty:
                                        print(
                                            "You have exceeded more than 50% of the budget for clothing and "
                                            "accessories.")

                        elif budget_code == 2:
                            if isinstance(self._user, Angel):
                                self._transaction_list.append(transaction)
                                self._user._b_balance = self._user.b_balance - amount
                                ninety = 0.1 * self._user.budgets[2].total
                                self._user.budgets[2].amount = self._user.budgets[2].amount - amount
                                if self._user.budgets[2].amount < 0:
                                    print("You have exceeded the budget for eating out.")
                                elif self._user.budgets[2].amount < ninety:
                                    print("You have exceeded more than 90% of the budget for eating out.")
                            elif isinstance(self._user, TroubleMaker):
                                if self._user.budgets[2].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    seventyFive = 0.25 * self._user.budgets[2].total
                                    oneTwenty = -0.20 * self._user.budgets[2].total
                                    self._user.budgets[2].amount = self._user.budgets[2].amount - amount
                                    if self._user.budgets[2].amount < oneTwenty:
                                        print("You have exceeded more than 120% of the budget for eating out.")
                                        print("You are now locked out of conducting transactions for eating out.")
                                        self._user.budgets[2].locked = True
                                    elif self._user.budgets[2].amount < 0:
                                        print("You have exceeded the budget for eating out.")
                                    elif self._user.budgets[2].amount < seventyFive:
                                        print(
                                            "You have exceeded more than 75% of the budget for eating out.")
                            elif isinstance(self._user, Rebel):
                                if self._user.budgets[2].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    fifty = 0.50 * self._user.budgets[2].total
                                    self._user.budgets[2].amount = self._user.budgets[2].amount - amount
                                    if self._user.budgets[2].amount < self._user.budgets[2].total:
                                        print("You have exceeded the budget for eating out!!")
                                        print("You are now locked out for eating out.")
                                        self._user.budgets[2].locked = True
                                        lockCounter = lockCounter + 1
                                        if lockCounter == 2:
                                            self._user.locked = True
                                    elif self._user.budgets[2].amount < fifty:
                                        print(
                                            "You have exceeded more than 50% of the budget for eating out")

                        elif budget_code == 3:
                            if isinstance(self._user, Angel):
                                self._transaction_list.append(transaction)
                                self._user._b_balance = self._user.b_balance - amount
                                ninety = 0.1 * self._user.budgets[3].total
                                self._user.budgets[3].amount = self._user.budgets[3].amount - amount
                                if self._user.budgets[3].amount < 0:
                                    print("You have exceeded the budget for miscellaneous.")
                                elif self._user.budgets[3].amount < ninety:
                                    print("You have exceeded more than 90% of the budget for miscellaneous.")
                            elif isinstance(self._user, TroubleMaker):
                                if self._user.budgets[3].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    seventyFive = 0.25 * self._user.budgets[3].total
                                    oneTwenty = -0.20 * self._user.budgets[3].total
                                    self._user.budgets[3].amount = self._user.budgets[3].amount - amount
                                    if self._user.budgets[3].amount < oneTwenty:
                                        print(
                                            "You have exceeded more than 120% of the budget for miscellaneous.")
                                        print("You are now locked out of conducting transactions for miscellaneous.")
                                        self._user.budgets[3].locked = True
                                    elif self._user.budgets[3].amount < 0:
                                        print("You have exceeded the budget for miscellaneous.")
                                    elif self._user.budgets[3].amount < seventyFive:
                                        print(
                                            "You have exceeded more than 75% of the budget for miscellaneous.")
                            elif isinstance(self._user, Rebel):
                                if self._user.budgets[3].locked:
                                    print("Your are locked out of this category. Cannot complete transaction.")
                                else:
                                    self._transaction_list.append(transaction)
                                    self._user._b_balance = self._user.b_balance - amount
                                    fifty = 0.50 * self._user.budgets[3].total
                                    self._user.budgets[3].amount = self._user.budgets[3].amount - amount
                                    if self._user.budgets[3].amount < self._user.budgets[3].total:
                                        print("You have exceeded the budget for miscellaneous!!")
                                        print("You are now locked out for miscellaneous.")
                                        self._user.budgets[3].locked = True
                                        lockCounter = lockCounter + 1
                                        if lockCounter == 2:
                                            self._user.locked = True
                                    elif self._user.budgets[3].amount < fifty:
                                        print(
                                            "You have exceeded more than 50% of the budget for miscellaneous.")

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
        user_input = None
        while user_input != 5:
            print("Please select a budget to view.")
            print("1. Games and Entertainment")
            print("2. Clothing and Accessories")
            print("3. Eating Out")
            print("4. Miscellaneous")
            print("5. Exit")
            string_input = input("Please enter your choice (1-5)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue
            user_input = int(string_input)
            if user_input == 1 or 2 or 3 or 4:
                break
            if user_input == 5:
                print("Exiting View Transactions by Budget")
                return
        print("\nTransaction List\n")
        for transaction in self._transaction_list:
            if transaction.budget_code == user_input - 1:
                print(transaction)


def load_test_user():
    """
    Used to create Fam user for testing
    :return:
    """
    games_budget = Budget("Games and Entertainment", 100)
    clothes_budget = Budget("Clothing and Accessories", 100)
    food_budget = Budget("Eating out", 100)
    misc_budget = Budget("Miscellaneous", 100)
    budgets = [games_budget, clothes_budget, food_budget, misc_budget]
    return Rebel("Ryan", 11, 2314, "TD", 1234, budgets)


def create_user():
    """
    Ask user for input to create a user
    :return:
    """
    user_type = None
    print("\nRegistering User:")
    print("-----------------------")
    print("Enter 1 for Angel user type")
    print("Enter 2 for Trouble Maker user type")
    print("Enter 3 for Rebel user type")
    print("Enter 4 to load test user")
    print("Enter 5 to exit program")
    while user_type != 5:
        user_type = input("Please enter a number from 1-5: ")
        if user_type == '':
            continue
        user_type = int(user_type)

        if user_type == 4:
            return load_test_user()
        try:
            name = input("Please enter user's name: ")
            age = int(input("Please enter user's age (positive number): "))
            b_num = input("Please enter bank account number: ")
            b_name = input("Please enter bank name: ")
            b_balance = int(input("Please enter bank balance (positive number): "))
            b_games = int(input("Please enter a budget for games and entertainment (positive number): "))
            b_clothes = int(input("Please enter a budget for clothing and accessories (positive number): "))
            b_food = int(input("Please enter a budget for eating out (positive number): "))
            b_misc = int(input("Please enter a budget for miscellaneous (positive number): "))
        except ValueError:
            print("Invalid data entered. Now exiting.")
            exit()
        budgets = [b_games, b_clothes, b_food, b_misc]

        if user_type == 1:
            return Angel(name, age, b_num, b_name, b_balance, budgets)
        elif user_type == 2:
            return TroubleMaker(name, age, b_num, b_name, b_balance, budgets)
        elif user_type == 3:
            return Rebel(name, age, b_num, b_name, b_balance, budgets)


def main():
    my_fam = Fam(create_user())
    my_fam.display_fam_menu()


if __name__ == '__main__':
    main()
