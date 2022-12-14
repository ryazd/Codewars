class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = ans = 0
        visit = {0: 1}
        for i, n in enumerate(nums):
            preSum += n
            ans += visit.get(preSum - k, 0)
            visit[preSum] = visit.get(preSum, 0) + 1
        return ans