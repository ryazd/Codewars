class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while right >= left:
            r_v = nums[right] ** 2
            l_v = nums[left] ** 2
            if r_v >= l_v:
                result.append(r_v)
                right -= 1
            else:
                result.append(l_v)
                left += 1
        return result[::-1]