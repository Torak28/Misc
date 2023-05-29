"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"
"""

from src.problems.p1603_design_parking_system import ParkingSystem


class Tests:
    """
    store TestCases
    """

    test_1 = ([1, 1, 1], 1, 2, 3, 1)
    test_2 = ([1, 1, 0], 1, 2, 3)

    def test_answer_1(self):
        """
        test case 1
        """
        park = ParkingSystem(*self.test_1[0])
        for elem in self.test_1[1:-1]:
            assert park.add_car(elem) is True
        assert park.add_car(-1) is False

    def test_answer_2(self):
        """
        test case 2
        """
        park = ParkingSystem(*self.test_2[0])
        for elem in self.test_2[1:-1]:
            assert park.add_car(elem) is True
        assert park.add_car(-1) is False
