class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0

        for i in range(len(s)):
            curr = romans[s[i]]
            next_val = romans[s[i+1]] if i+1 < len(s) else 0

            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result

s = "DLXXXV"
obj = Solution()
result = obj.romanToInt(s)
print("Int value: ",result)