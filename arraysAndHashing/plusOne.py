class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        """
        example: 1 9 9 9 -> 2 0 0 0
        or: 9 9 -> 1 0 0

        """

        last_digit = digits[len(digits) - 1]
        if last_digit < 9:
            digits[len(digits) - 1] += 1

        else:

            i = len(digits) - 1
            # continue carrying the 1 until you no longer need to
            while i > -1 and (((i == len(digits) - 1) and digits[i] == 9) or (i < len(digits) - 1 and digits[i] == 10)):
                digits[i] = 0
                if i == 0:
                    digits_new = [1]
                    for i in range(len(digits)):
                        digits_new.append(digits[i])
                    digits = digits_new
                else:
                    digits[i - 1] += 1
                i -= 1
        
        return digits

        # this solution has time complexity O(n) where n is the number of digits
        # todo: simplify this solution, make more readable
            

        