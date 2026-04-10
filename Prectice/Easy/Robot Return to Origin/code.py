class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) & 1: return False
        x, y = [0, 0]

        dist = {
            "U" : (0, 1),
            "D" : (0, -1),
            "L" : (-1, 0),
            "R" : (1, 0)
        }

        for c in moves:
            dx, dy = dist[c]
            x += dx
            y += dy
        
        return [x, y] == [0, 0]


moves = "UD"
obj = Solution()

print("Moves correct? -> ",obj.judgeCircle(moves))