from typing import List

class Solution:
    def longestCommonPrefix(self, strs:List[str])->str:
        strs.sort()

        s1 = strs[0]
        s2 = strs[-1]

        idx = 0

        while idx < len(s1)  and idx < len(s2):
            if s1[idx] == s2[idx]:
                idx += 1
            else:
                break
        return s1[:idx]
    
strs = ["flower","flow","flight"]

obj = Solution()
result = obj.longestCommonPrefix(strs)
print("Biggest Prefix: ",result)