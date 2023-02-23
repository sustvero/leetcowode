class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # continuously reach out to neighbours
        # have a set called visited
        visited = set()
        islands = 0

         # use DFS algorithm as a helper function
        def dfs(r, c):
            if (r >= rows or r < 0 
                or c >= cols or c < 0 
                or grid[r][c] == '0'
                or (r, c) in visited
            ):
                return

            visited.add((r, c)) # add point to visited set
            # run dfs on each adjacent vertex
            dfs(r + 1, c) #below
            dfs(r - 1, c) #above
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left

        for r in range(0, rows):
            for c in range(0, cols):
                # check if current vertex has already been visited
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands

# this solution has complexity ((nm)^2)log(nm)