from collections import defaultdict
import bisect
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))
    def get(self, key, timestamp):
        arr = self.store[key]
        idx = bisect.bisect_right(arr, (timestamp, chr(127))) - 1
        if idx >= 0:
            return arr[idx][1]
        return ""
