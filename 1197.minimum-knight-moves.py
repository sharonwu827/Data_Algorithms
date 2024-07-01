class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = ((1,2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        queue = deque([(0,0)])
        res = 0 
        seen = set()
        while queue:
            for _ in range(len(queue)):
                curX, curY = queue.popleft()
                if curX == x and curY == y:
                    return res
                seen.add((curX, curY))
                for i, j in dirs:
                    newX, newY = curX + i, curY + j
                    if (newX, newY) not in seen:
                        queue.append((newX, newY))
                        seen.add((newX, newY))
            res+=1
        return res