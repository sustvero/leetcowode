class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = set()

        # use dfs as a helper function
        def dfs(r, c):
            if (r not in range(0, m)
                or c not in range(0, n)
                or grid[r][c] == 0 # CAREFUL: ARRAY CONTAINED INTEGERS INSTEAD OF STRINGS
                or (r, c) in visited
            ):
                return 0
            
            visited.add((r, c))
            
            # run dfs on adjacent vertices
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        maxArea = 0
        for r in range(0, m):
            for c in range(0, n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curArea = 0
                    curArea = dfs(r, c)
                    if curArea > maxArea:
                        maxArea = curArea
        
        return maxArea

# this solution has time complexity O(nm*nmlognm)