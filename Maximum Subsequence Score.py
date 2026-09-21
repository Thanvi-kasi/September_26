class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        total = 0
        ans = 0

        for b, a in pairs:
            heapq.heappush(heap, a)
            total += a

            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * b)

        return ans
