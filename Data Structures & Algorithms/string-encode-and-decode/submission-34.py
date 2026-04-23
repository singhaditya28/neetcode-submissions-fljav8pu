class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs=='':
            return "!/\\lk,"
        if strs==[]:
            return '[]'
        a = '!/\\lk,'.join(strs)
        print(a)
        return a
    def decode(self, s: str) -> List[str]:
        b = s.split('!/\\lk,')
        if s==['']:#len(b) ==0
            print(1)
            return [""]
        if s == '[]':
            return []

        print(type(b))
        return b