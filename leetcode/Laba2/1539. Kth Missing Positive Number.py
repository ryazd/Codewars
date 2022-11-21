class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) 
        while right - left > 0:
            mid = left + (right - left) // 2
            if arr[mid] - (mid + 1) >= k:
                right = mid
            else:
                left = mid + 1
        return left + k