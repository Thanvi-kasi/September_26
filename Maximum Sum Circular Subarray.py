class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_ending = 0
        max_sum = nums[0]
        min_ending = 0
        min_sum = nums[0]

        for num in nums:
            max_ending = max(num, max_ending + num)
            max_sum = max(max_sum, max_ending)

            min_ending = min(num, min_ending + num)
            min_sum = min(min_sum, min_ending)

            total += num

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
