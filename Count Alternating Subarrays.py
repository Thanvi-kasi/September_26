class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        length = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                length += 1
            else:
                length = 1

            ans += length

        return ans
