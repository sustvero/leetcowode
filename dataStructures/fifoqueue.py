class MyQueue:
    # first in, first out
    # 2 stacks
    # 1 2 3 4 5
    stack1 = []
    reset = []

    def __init__(self):
        self.stack1 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        # remove first element and return
        # reset queue
        temp = self.stack1[0]
        self.stack1 = self.stack1[1:]
        return temp
        

    def peek(self) -> int:
        # returns element at front of queue
        return self.stack1[0]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()