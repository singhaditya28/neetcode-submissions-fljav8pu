class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs: return ""
        prefix = strs[0]
        
        for i in range(1,len(strs)):
            counter =0
            
            for j in range(min(len(strs[i]),len(prefix))):
                if strs[i][j]==prefix[j]:
                    counter+=1
                # elif prefix== "":
                #     return ""
                else:
                    break
            prefix = prefix[:counter]
        return prefix