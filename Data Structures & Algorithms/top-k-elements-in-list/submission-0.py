class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem = {}
        for v in nums:
            elem[v] = 1 +elem.get(v,0)
        
        # print(elem.items())
        fin = sorted(elem.items(), key=lambda item: item[1], reverse=True)
        # print(fin)
        selection = fin[:k]
        # print(selection)
        res = []
        for i in selection:
            res.append(i[0])
        return res


