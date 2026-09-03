class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1

        ans = 1
        length = 1
        prev_sign = 0

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                sign = 1
            elif arr[i] < arr[i - 1]:
                sign = -1
            else:
                sign = 0

            if sign == 0:
                length = 1
                prev_sign = 0
            elif sign != prev_sign:
                length += 1
                prev_sign = sign
            else:
                length = 2
                prev_sign = sign

            ans = max(ans, length)

        return ans
