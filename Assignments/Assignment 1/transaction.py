class Transaction:

    def __init__(self, timestamp, amount, category, store):
        self._timestamp = timestamp
        self._amount = amount
        self._category = category
        self._store = store

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def store(self):
        return self._store

    def __str__(self):
        return f"TimeStamp: {self._timestamp}\n" \
               f"Amount: ${self._amount}\n" \
               f"Category: {self._category}\n" \
               f"Store: {self._store}\n"