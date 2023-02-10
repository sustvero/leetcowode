class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # this solution will use binary searching
        # first search vertically to find the correct row (range of values)
        # next, search horizontally to find the target value

        m = len(matrix)
        n = len(matrix[0])

        # vertical search
        low = 0
        high = m - 1
        mid = 0
        row = -1

        while (low <= high):
            mid = (low + high) // 2
            print(mid)
            if (matrix[mid][0] <= target and matrix[mid][-1] >= target): # found correct range
                row = mid
                break
            elif (matrix[mid][0] < target and matrix[mid][-1] <= target): # right half
                low = mid + 1
            else: # left half
                high = mid - 1
        
        
        if (row == -1):
            return False
        

        # horizontal search
        column = 0
        low = 0
        high = n - 1
        mid = 0

        while (low <= high):
            mid = (low + high) // 2
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] < target):
                low = mid + 1
            else:
                high = mid - 1
                
        
        return False

# this solution has runtime O(log(m) + log(n))
