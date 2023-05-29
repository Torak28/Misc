"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"

Link: https://leetcode.com/problems/design-parking-system/

Design a parking system for a parking lot. The parking lot has
three kinds of parking spaces: big, medium, and small, with a
fixed number of slots for each size.
"""


class ParkingSystem:
    """
    Parking System
    """

    def __init__(self, big: int, medium: int, small: int):
        """
        Init with list `spots` describing empty spaces.

        Args:
            big (int): num of spaces for big cars,
            medium (int): num of spaces for medium cars
            small (int): num of spaces for small cars
        """
        self.spots = [big, medium, small]

    def add_car(self, car_type: int) -> bool:
        """
        Be smart and use car_type as list index to know what car
        needs to be added

        Args:
            car_type (int): car type. 1 for big, 2 for medium and
                           3 for small

        Returns:
            bool: `True` if car can park, `False` is can't
        """
        car_type_allign = car_type - 1

        if self.spots[car_type_allign] > 0:
            self.spots[car_type_allign] -= 1
            return True
        return False
