class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict_p = {}
        for i in range(0, len(names)):
            dict_p[heights[i]] = names[i]
        heights.sort(key=lambda x: -x)
        lst = []
        for item in heights:
            lst.append(dict_p[item])
        return lst