from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        k %= n  # (reduce k<n)
        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row , left shift
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # odd row , right shift
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
        
        return True

mat = [[1,2,3],[4,5,6],[7,8,9]] #false
k = 4
obj = Solution()
result = obj.areSimilar(mat,k)  
print("Result: ",result)

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]  #true
k = 2
obj = Solution()
result = obj.areSimilar(mat,k)  
print("Result: ",result)