class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = []
        for i in s:
            seen.append(i)
        for j in t:
            try: 
                seen.remove(j)
            except:
                return False
        return True