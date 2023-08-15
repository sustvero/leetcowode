class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # alternate between right, down, left, up
        # matrix elements will always be between 1 and 10 inclusive, mark with -1 to show it is visited?

        res = []

        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols

        x = 0
        y = 0

        dir = "right"

        while True:
            # add current matrix element
            res.append(matrix[y][x])
            # set current matrix element to visited
            matrix[y][x] = -101
            # see if we are done
            if len(res) == size:
                break

            # otherwise, figure out where to go next
            if (dir == "right"):
                # try to keep going right
                if (x + 1) < cols and matrix[y][x + 1] != -101:
                    x = x + 1
                else:
                    # if we can't, go down
                    y = y + 1
                    dir = "down"
            
            elif dir == "down":
                # try to keep going down
                if (y + 1) < rows and matrix[y + 1][x] != -101:
                    y += 1
                else:
                    # if we can't, go left
                    x -= 1
                    dir = "left"
                
            elif dir == "left":
                # try to keep going left
                if (x - 1) >= 0 and matrix[y][x - 1] != -101:
                    x -= 1
                else:
                    # if we can't, go up
                    y -= 1
                    dir = "up"

            elif dir == "up":
                # try to keep going up
                if (y - 1) >= 0 and matrix[y - 1][x] != -101:
                    y -= 1
                else:
                    # if we can't, go right
                    x += 1
                    dir = "right"
        
        return res


