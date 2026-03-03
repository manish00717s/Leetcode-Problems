class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        div_sum = m * k * (k + 1) // 2
        return total - 2 * div_sum