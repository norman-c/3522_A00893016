import math


class Asteroid:

    unique_id = 0

    def __init__(self, circumference, position, velocity):
        """
        Creates the asteroid object
        :param circumference: a float
        :param position: a tuple of ints
        :param velocity: a tuple of ints
        """
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = Asteroid.get_unique_id()

    @classmethod
    def get_unique_id(cls):
        """Return the unique id of the Asteroid class"""
        cls.unique_id +=1
        return cls.unique_id

    @staticmethod
    def calc_circumference(radius):
        """Calculate the circumference"""
        return radius * 2 * math.pi

    def __str__(self):
        """Return information about the class as a string"""
        return "Id: {0} Circumference: {1} Position: {2} Velocity: {3}".format(self._id, self._circumference, self._position, self._velocity)

    def set_circumference(self, circumference):
        """Set the circumference of the asteroid
        circumference -- the circumference to set
        """
        self._circumference = circumference

    def get_circumference(self):
        """Get the circumference of the asteroid"""
        return self._circumference

    def set_position(self, new_position):
        """Set the position of the asteroid
        new_position -- the position to set
        """
        self._position = new_position

    def get_position(self):
        """Get the position of the asteroid"""
        return self._position

    def set_velocity(self, velocity):
        """Set the velocity of the asteroid
         velocity -- the velocity to set
         """
        self._velocity = velocity

    def get_velocity(self):
        """Get the velocity of the asteroid"""
        return self._velocity

    def move(self):
        """Change the position of the asteroid based on velocity"""
        return (self._position[0] + self._velocity[0], self._position[1] + self._velocity[1], self._position[2] +self._velocity[2])

