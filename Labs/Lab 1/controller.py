import random
import time
import datetime
from asteroid import Asteroid



class Controller:

    asteroid_list = []

    def __init__(self):
        for i in range(1, 101):
            circumference = Asteroid.calc_circumference(random.randint(1,4))
            temp_asteroid = Asteroid(circumference, (0,0,0), (random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)))
            Controller.asteroid_list.append(temp_asteroid)

    def simulate(self, seconds):
        print("Simultation Start Time: {}".format(datetime.datetime.fromtimestamp(time.time())))
        print("\nMoving Asteroids!\n-----------------\n")
        for i in range(seconds):
            time.sleep(1)
            for x in Controller.asteroid_list:
                x.set_position(x.move())
                print(x)
            print("\n")
        print("Simultation End Time: {}".format(datetime.datetime.fromtimestamp(time.time())))


def main():
    temp = Controller()
    temp.simulate(2)

if __name__ == "__main__":
    main()
