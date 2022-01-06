INT_MAX = 2147483647

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n, Q = len(rooms), len(rooms[0]), deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: Q.append((i, j, 0))
        while Q:
            x, y, step = Q.popleft()
            for i, j in [(x+1, y), (x-1,y), (x,y+1),(x,y-1)]:
                if 0 <= i < m and 0 <= j < n and rooms[i][j] == INT_MAX:
                    rooms[i][j] = step + 1
                    Q.append((i, j, step+1))
