class Solution:
    def lenLongestFibSubarray(self, nums):
        ans = 2
        cur = 2

        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                cur += 1
            else:
                cur = 2
            ans = max(ans, cur)

        return ans
