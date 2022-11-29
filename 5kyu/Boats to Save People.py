# https://leetcode.com/problems/boats-to-save-people/

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i


l = Solution()
print(l.numRescueBoats([1, 3, 5, 2], 3))
