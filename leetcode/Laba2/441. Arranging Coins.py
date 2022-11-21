class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            s_r = (1 + mid) * mid / 2
            if s_r == n:
                return mid
            elif s_r > n:
                if n >= (1 + mid - 1) * (mid - 1) / 2:
                    return mid - 1
                else:
                    right = mid
            else:
                left = mid
        return right if (1 + right) * right / 2 <= n else left