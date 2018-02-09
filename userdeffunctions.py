""" This module contains the car class"""


class car:
    def __init__(self, name, colour, seats):
        """ car object which has three attributes """
        self.colour = colour
        self.seats = seats
        self.name = name

    def __call__(self):
        return self.name

    def get_seats(self):
        """ Returns number of seats """
        return self.seats
