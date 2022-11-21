class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid
            else:
                right = mid
            if nums[mid] == target:
                return mid
        return right + 1 if target > nums[right] else right if target > nums[left] else left