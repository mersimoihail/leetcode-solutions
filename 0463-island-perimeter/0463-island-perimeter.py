from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited = set()
        count = 0

        def island(row, col):
            nonlocal count

            if (row, col) in visited:
                return

            visited.add((row, col))

            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    count += 1
                elif grid[r][c] == 0:
                    count += 1
                else:
                    island(r, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island(i, j)
                    return count