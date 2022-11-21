class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        elem = nums[0]
        left = [x for x in nums if x < elem]
        mid = [x for x in nums if x == elem]
        right = [x for x in nums if x > elem]
        return self.sortArray(left) + mid + self.sortArray(right)