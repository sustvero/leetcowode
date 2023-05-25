class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # create an adapted dfs algorithm
        # run dfs, checking each time whether the color matches the color of the source

        visited = {}
        rows = len(image)
        cols = len(image[0])

        same_color = image[sr][sc]

        def dfs(r, c):

            if (r, c) in visited or (r not in range(0, rows) or (c not in range(0, cols)) or image[r][c] != same_color):
                return
            
            # change color if needed
            if image[r][c] != color:
                image[r][c] = color
            
            
            # mark the square as visited
            visited[(r, c)] = 1
            
            # run dfs on adjacent squares
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # run dfs
        dfs(sr, sc)
        return image
        

# this solution has time complexity O(nm)
            