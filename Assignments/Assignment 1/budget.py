class Budget:

    def __init__(self, name, amount):
        self._name = name
        self._total = amount
        self._amount = amount
        self._locked = False

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def total(self):
        return self._total

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        self._locked = value

    def __str__(self):
        return f"Category: {self._name}\n" \
               f"Locked: {self._locked}\n" \
               f"Amount spent: {self._amount}\n" \
               f"Amount left: {(self._total - self._amount)}\n" \
               f"Total budget: {self._total}\n" \
