class User():

    def __init__(self, name, age, user_type, b_num, b_name, b_balance, budget):
        self._name = name
        self._age = age
        self._user_type = user_type
        self._b_num = b_num
        self._b_name = b_name
        self._b_balance = b_balance
        self._budget = budget

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def usertype(self):
        return self._user_type

    @property
    def b_num(self):
        return self.b_num

    @property
    def b_name(self):
        return self._b_name

    @property
    def b_balance(self):
        return self._b_balance

    @property
    def budget(self):
        """
        Will maybe create a budget class or as a List
        :return:
        """
        return self._budget

    def display_bank(self):
        return f"\nBank Account number: {self._b_num}\n" \
               f"Bank Name: {self._b_name}\n" \
               f"Bank Balance: ${self._b_balance}"
