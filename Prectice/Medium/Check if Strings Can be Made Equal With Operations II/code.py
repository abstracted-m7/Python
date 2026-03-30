class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1_even = ""
        s1_odd = ""
        s2_even = ""
        s2_odd = ""

        for i in range(n):
            if i % 2 == 0:
                s1_even += s1[i]
                s2_even += s2[i]
            else:
                s1_odd += s1[i]
                s2_odd += s2[i]
        s1_even = ''.join(sorted(s1_even))
        s2_even = ''.join(sorted(s2_even))
        s1_odd = ''.join(sorted(s1_odd))
        s2_odd = ''.join(sorted(s2_odd))

        if s1_even == s2_even and s1_odd == s2_odd:
            return True

        return False

s1 = "abcdba"
s2 = "cabdab"
obj = Solution()
print("Result: ",obj.checkStrings(s1,s2))