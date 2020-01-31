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
