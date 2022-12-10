class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            w = tuple(sorted(s))
            if w in res:
                res[w].append(s)
            else:
                res[w] = [s]
        return res.values()