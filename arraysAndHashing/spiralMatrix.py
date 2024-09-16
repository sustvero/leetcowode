class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # we need to find a stopping condition
        # count the number of spots we have passed

        x_start = 0
        x_end = len(matrix[0])
        y_start = 0
        y_end = len(matrix)

        res = []

        # define x and y coordinates
        x = 0
        y = 0
        res.append(matrix[x][y])
        count = 1
        x += 1

        total_spots = len(matrix) * len(matrix[0])
        while count < total_spots:
            # go right
            while x < x_end and count < total_spots:
                print(matrix[y][x])
                res.append(matrix[y][x])
                x += 1
                count += 1
            x = x_end - 1
            y += 1
            # go down
            while y < y_end and count < total_spots:
                res.append(matrix[y][x])
                y += 1
                count += 1
            y = y_end - 1
            # go left
            x -= 1
            while x >= x_start and count < total_spots:
                res.append(matrix[y][x])
                x -= 1
                count += 1
            x = x_start
            y -= 1
            while y > y_start and count < total_spots:
                res.append(matrix[y][x])
                y -= 1
                count += 1
            y = y_start + 1

            if count == total_spots:
                break;
            
            # change start and end points
            x_start += 1
            x_end -= 1
            y_start += 1
            y_end -= 1

            # change x position
            x = x_start
    
        return res

        # this solution has time complexity O(n)
    



        



        