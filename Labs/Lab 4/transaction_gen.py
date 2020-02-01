from transaction import Transaction


class TransactionGen:

    @staticmethod
    def create_transaction():
        category = None
        timestamp = "Timestamp"
        amount = int(input("Enter cost of item "
                           "(positive number): "))
        user_input = None
        while category is None:
            print("Please select the budget category")
            print("1. Games and Entertainment")
            print("2. Clothes and Accessories")
            print("3. Eating out")
            print("4. Miscellaneous")
            string_input = input("Please enter your choice (1-4)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue
            if user_input == 1:
                category = "Games and Entertainment"
            elif user_input == 2:
                category = "Clothes and Accessories"
            elif user_input == 3:
                category = "Eating out"
            else:
                category = "Miscellaneous"


        store = input("Enter store name: ")

        return Transaction(timestamp, amount, category, store)
