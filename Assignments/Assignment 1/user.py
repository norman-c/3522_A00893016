from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name, age, b_num, b_name, b_balance, bud):
        self._name = name
        self._age = age
        self._b_name = b_name
        self._b_num = b_num
        self._b_balance = b_balance
        self._budgets = bud
        self._locked = False

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

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
    def budgets(self):
        return self._budgets

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        self._locked = value

    @abstractmethod
    def display_bank(self):
        return f"\nBank Account number: {self._b_num}\n" \
               f"Bank Name: {self._b_name}\n" \
               f"Bank Balance: ${self._b_balance}"

    @abstractmethod
    def display_budgets(self):
        for b in self._budgets:
            print(b)


class Angel(User):

    def __init__(self, name, age, b_num, b_name, b_balance, budget):
        super().__init__(name, age, b_num, b_name, b_balance, budget)

    def display_bank(self):
        return super().display_bank()

    def display_budgets(self):
        super().display_budgets()


class TroubleMaker(User):

    def __init__(self, name, age, b_num, b_name, b_balance, budget):
        super().__init__(name, age, b_num, b_name, b_balance, budget)

    def display_bank(self):
        return super().display_bank()

    def display_budgets(self):
        super().display_budgets()


class Rebel(User):

    def __init__(self, name, age, b_num, b_name, b_balance, budget):
        super().__init__(name, age, b_num, b_name, b_balance, budget)

    def display_bank(self):
        return super().display_bank()

    def display_budgets(self):
        super().display_budgets()
