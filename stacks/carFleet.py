class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """

        condition for a car not to catch up to the car ahead:
        both greater position and greater speed

        if this condition is not true, the question is whether the 
        catch-up happens before the destination is reached
        compare the number of steps needed to reach the destination?
        if it is less than or equal the two cars become a fleet

        method:
        sort the cars by closest to destination to furthest from destination
        figure out the number of steps needed to reach the destination
        store this in a stack
        if a car requires less or equal steps than the car in front of it,
        pop its steps off the stack

        the length of the stack after iterating will be the final result
        """

        # create pairs: location, speed
        cars = []
        for i in range(len(position)):
            pair = [position[i], speed[i]]
            cars.append(pair)
        
        # sort by closest to furthest from destination
        cars.sort(key=lambda x: x[0], reverse=True)

        # iterate through cars and keep a stack of steps
        stack = []
        for car in cars:
            steps = (target - car[0]) / car[1]
            stack.append(steps)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            # else do nothing (car will catch up to the one in front of it)
        
        return len(stack)

# the time complexity of this problem is O(nlogn)
                


