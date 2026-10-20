class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_map = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k
            if remainder < 0:
                remainder += k
            if remainder in remainder_map:
                count += remainder_map[remainder]
            remainder_map[remainder] = remainder_map.get(remainder, 0) + 1
        return count
