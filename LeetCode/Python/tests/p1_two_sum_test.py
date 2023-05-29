"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"
"""

from src.problems.p1_two_sum import Solution


class Tests:
    """
    store TestCases
    """

    sol = Solution()
    test_1 = ([2, 7, 11, 15], 9)
    test_2 = ([3, 2, 4], 6)
    test_3 = ([3, 3], 6)

    def test_answer_1(self):
        """
        test case 1
        """
        assert self.sol.two_sum_1(*self.test_1) == [0, 1]

    def test_answer_2(self):
        """
        test case 2
        """
        assert self.sol.two_sum_1(*self.test_2) == [1, 2]

    def test_answer_3(self):
        """
        test case 3
        """
        assert self.sol.two_sum_1(*self.test_3) == [0, 1]

    def test_answer_4(self):
        """
        test case 4
        """
        assert self.sol.two_sum_2(*self.test_1) == [0, 1]

    def test_answer_5(self):
        """
        test case 5
        """
        assert self.sol.two_sum_2(*self.test_2) == [1, 2]

    def test_answer_6(self):
        """
        test case 6
        """
        assert self.sol.two_sum_2(*self.test_3) == [0, 1]
