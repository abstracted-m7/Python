class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        '''
        n+m-1
        str1[i] == "T" so word[i..(i+m-1)] == str2
        str[i]  == "F" so word[i..(i+m-1)] != str2
        '''
        n , m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1) #? is denote panding position

        #process 'T'
        for i, b in enumerate(str1):
            if b != 'T':
                continue
            #The substring must match t
            for j, c in enumerate(str2):
                v = ans[i + j]
                if v != '?' and v != c:
                    return ""
                ans[i + j ] = c
        
        prev_ans = ans
        ans = ['a' if c == '?' else c for c in ans] #initial default

        #process 'F'
        for i, b in enumerate(str1):
            if b != 'F':
                continue
            #substring must not equal to k
            if ''.join(ans[i: i+m]) != str2:
                continue
            #locate the last pending position to modify
            for j in range(i + m - 1, i - 1, -1):
                if prev_ans[j] == '?':
                    ans[j] = 'b'
                    break
            else:
                return ""
        return ''.join(ans)
str1 = "TFTF"
str2 = "ab"
obj = Solution()
print("The Result: ",obj.generateString(str1, str2))