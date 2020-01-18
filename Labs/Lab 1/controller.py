import random
import time
import datetime
from asteroid import Asteroid


def simulate(seconds):
    """
    Simulates movement of the asteroids and displays the simulation
    :param seconds: an int for how many seconds to simulate
    :return:
    """
    delta = datetime.datetime.now() + datetime.timedelta(seconds=1)
    time.sleep(1 - (delta.microsecond / 1000000))
    print("Simultation Start Time: {}".format(datetime.datetime.fromtimestamp(time.time())))

    print("\nMoving Asteroids!\n-----------------\n")
    for i in range(seconds):
        time.sleep(1)
        for x in Controller.asteroid_list:
            x.set_position(x.move())
            print(x)
        print("\n")
    print("Simultation End Time: {}".format(datetime.datetime.fromtimestamp(time.time())))


class Controller:
    asteroid_list = []
    starting_position = (0, 0, 0)

    def __init__(self):
        """
        Creates 100 asteroids and stores them into a list
        """
        for i in range(1, 101):
            circumference = Asteroid.calc_circumference(random.randint(1, 4))
            temp_asteroid = Asteroid(circumference, Controller.starting_position,
                                     (random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)))
            Controller.asteroid_list.append(temp_asteroid)


def main():
    temp = Controller()
    simulate(2)


if __name__ == "__main__":
    main()
