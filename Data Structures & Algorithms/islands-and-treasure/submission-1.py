class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        visited = set()
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (
                    r < 0 or r >= ROWS or 
                    c < 0 or c >= COLS or
                    (r, c) in visited or
                    grid[r][c] == -1
                ):
                    continue
                
                
                grid[r][c] = distance
                visited.add((r,c))

                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

            distance += 1

            
