import math


class Asteroid:

    unique_id = 0

    def __init__(self, circumference, position, velocity):
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = Asteroid.get_unique_id()

    @classmethod
    def get_unique_id(cls):
        cls.unique_id +=1
        return cls.unique_id

    @staticmethod
    def calc_circumference(radius):
        return radius * 2 * math.pi

    def __str__(self):
        return "Id: {0} Circumference: {1} Position: {2} Velocity: {3}".format(self._id, self._circumference, self._position, self._velocity)

    def set_circumference(self, circumference):
        self._circumference = circumference

    def get_circumference(self):
        return self._circumference

    def set_position(self, new_position):
        self._position = new_position

    def get_position(self):
        return self._position

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity

    def move(self):
        return (self._position[0] + self._velocity[0], self._position[1] + self._velocity[1], self._position[2] +self._velocity[2])
