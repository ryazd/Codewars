class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        part1 = self.sortArray(nums[0:mid])
        part2 = self.sortArray(nums[mid:])
        p = []
        i = 0
        j = 0
        while i < len(part1) and j < len(part2):
            if part1[i] < part2[j]:
                p.append(part1[i])
                i += 1
            else:
                p.append(part2[j])
                j += 1
        while i < len(part1):
            p.append(part1[i])
            i += 1
        while j < len(part2):
            p.append(part2[j])
            j += 1
        return p