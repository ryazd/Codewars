class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lst = set([x for x in range(0, len(nums) + 1)])
        return list(lst - set(nums))[0]