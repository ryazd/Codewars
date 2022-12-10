class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 in nums_set:
                continue
            length = 0
            while num in nums_set:
                num += 1
                length += 1
            ans = max(ans, length)
        return ans