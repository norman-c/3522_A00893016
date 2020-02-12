class Budget:

    def __init__(self, games, clothes, food, misc):
        self._games = games
        self._clothes = clothes
        self._food = food
        self._misc = misc

    @property
    def games(self):
        return self._games

    @property
    def clothes(self):
        return self._clothes

    @property
    def food(self):
        return self._food

    @property
    def misc(self):
        return self._misc

    def __str__(self):
        return f"---- Budgets:----\n" \
               f"Games and Entertainment: ${self._games}\n" \
               f"Clothing and Accessories: ${self._clothes}\n" \
               f"Eating out: ${self._food}\n" \
               f"Miscellaneous: ${self._misc}"
