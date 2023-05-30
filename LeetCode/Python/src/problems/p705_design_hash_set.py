"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"

Link: https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.
"""


class MyHashSet:
    """
    Simple HashTable
    """

    def __init__(self):
        """
        Init with `hash_set` to store data
        """
        self.hash_set = set()

    def add(self, key: int) -> None:
        """
        Add to HashSet

        Args:
            key (int): elem to add
        """
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        """
        Remove from HashSet

        Args:
            key (int): elem to remove
        """
        self.hash_set.discard(key)

    def contains(self, key: int) -> bool:
        """Check if `key` is a elem of `hash_set`

        Args:
            key (int): elem to check

        Returns:
            bool: True if exists, False if not
        """
        if key in self.hash_set:
            return True
        return False
