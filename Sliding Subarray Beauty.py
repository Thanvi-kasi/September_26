class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        count = [0] * 50
        ans = []

        for i in range(len(nums)):
            if nums[i] < 0:
                count[nums[i] + 50] += 1

            if i >= k:
                if nums[i - k] < 0:
                    count[nums[i - k] + 50] -= 1

            if i >= k - 1:
                c = 0
                beauty = 0

                for j in range(50):
                    c += count[j]
                    if c >= x:
                        beauty = j - 50
                        break

                ans.append(beauty)

        return ans
