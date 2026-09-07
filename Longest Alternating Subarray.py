class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        length = 1
        expected = 1

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]

            if diff == expected:
                length += 1
                ans = max(ans, length)
                expected *= -1
            else:
                if diff == 1:
                    length = 2
                    ans = max(ans, length)
                    expected = -1
                else:
                    length = 1
                    expected = 1

        return ans
