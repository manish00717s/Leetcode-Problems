import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = len(self.idx_map[val]) == 0
        self.idx_map[val].add(len(self.vals))
        self.vals.append(val)
        return res

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        idx = self.idx_map[val].pop()
        last_idx = len(self.vals) - 1
        last_val = self.vals[-1]
        if idx != last_idx:
            self.vals[idx] = last_val
            self.idx_map[last_val].remove(last_idx)
            self.idx_map[last_val].add(idx)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()