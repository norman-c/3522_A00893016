import random
import math
import asteroid as asteroid


class Controller:
    asteroid_list = []

    def __init__(self):
        for i in range(1, 100):
            circumference = Asteroid.calc_circumference(random.randint(1,4))
            temp_asteroid = asteroid(circumference, 0, (random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)))
