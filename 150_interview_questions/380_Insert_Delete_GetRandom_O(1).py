# 380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
from random import randint


class RandomizedSet:
    def __init__(self):
        self.random_set  = set()

    def insert(self, value):
        self.random_set.add(value)
    def remove(self, value):
        self.random_set.remove(value)
    def getRandom(self):
        list_of_elements = list(self.random_set)
        return list_of_elements[randint(0,len(list_of_elements)-1)]


random_set = RandomizedSet()
random_set.insert(2)
random_set.insert(3)
print(random_set.random_set)
random_set.getRandom()

