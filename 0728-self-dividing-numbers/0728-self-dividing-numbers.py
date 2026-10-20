class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True
        result = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                result.append(num)
        return result
