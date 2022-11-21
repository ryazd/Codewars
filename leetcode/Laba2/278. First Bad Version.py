class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        if n == 1:
            return 1
        while right - left >= 1:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return right