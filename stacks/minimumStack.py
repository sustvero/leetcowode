class MinStack:

    # along with the value, note the current minimum value

    def __init__(self):
        self.val_list = []
        self.current_min = []
        

    def push(self, val: int) -> None:
        self.val_list.append(val)
        # first element or smaller than current minimum
        if len(self.current_min) == 0 or val < self.current_min[-1]:
            self.current_min.append(val)
        # greater than current minimum
        else:
            self.current_min.append(self.current_min[-1])
        

    def pop(self) -> None:
        self.current_min.pop()
        self.val_list.pop()
        

    def top(self) -> int:
        return self.val_list[-1]
        

    def getMin(self) -> int:
        return self.current_min[-1]
        
# all functions run in O(1)