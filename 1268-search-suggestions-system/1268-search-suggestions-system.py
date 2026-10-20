from bisect import bisect_left
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)
            suggestions = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            res.append(suggestions)
        return res
