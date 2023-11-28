import random

class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            index = self.random_set[val]
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.random_set[self.list[index]] = index
            self.list.pop()
            del self.random_set[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)