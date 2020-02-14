class Transaction:

    def __init__(self, timestamp, amount, store, budget_code):
        self._timestamp = timestamp
        self._amount = amount
        self._store = store
        self._budget_code = budget_code

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def amount(self):
        return self._amount

    @property
    def budget_code(self):
        return self._budget_code

    @property
    def store(self):
        return self._store

    def __str__(self):
        return f"TimeStamp: {self._timestamp}\n" \
               f"Amount: ${self._amount}\n" \
               f"Store: {self._store}\n"
