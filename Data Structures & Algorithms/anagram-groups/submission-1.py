class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        if not strs: return [[""]]
        for i in strs:
            counter = [0]*26
            for char in i:
                counter[ord(char)-ord('a')]+=1
            res[tuple(counter)].append(i)
            # print(counter)
        a = list(res.values())
        print(a)
        return a
            

