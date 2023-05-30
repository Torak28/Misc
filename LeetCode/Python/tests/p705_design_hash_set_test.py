"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"
"""

from src.problems.p705_design_hash_set import MyHashSet


class Tests:
    """
    store TestCases
    """

    def test_answer_1(self):
        """
        test case 1
        """
        my_set = MyHashSet()
        my_set.add(1)
        my_set.add(2)
        assert my_set.contains(1) is True
        assert my_set.contains(3) is False
        my_set.add(2)
        assert my_set.contains(2) is True
        my_set.remove(2)
        assert my_set.contains(2) is False
