from collections import Counter
class Solution:
    def frequencySort(self, s):
        count = Counter(s)
        sorted_chars = sorted(count.keys(), key=lambda x: -count[x])
        result = ""
        for ch in sorted_chars:
            result += ch * count[ch]
        return result
