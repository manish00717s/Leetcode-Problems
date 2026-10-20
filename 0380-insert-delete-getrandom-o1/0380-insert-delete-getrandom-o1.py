import random
class RandomizedSet(object):
    def __init__(self):
        self.vals = []
        self.idx_map = {}
    def insert(self, val):
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.vals)
        self.vals.append(val)
        return True
    def remove(self, val):
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val
        self.idx_map[last_val] = idx
        self.vals.pop()
        del self.idx_map[val]
        return True
    def getRandom(self):
        return random.choice(self.vals)
