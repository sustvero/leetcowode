
# plan: use arrays to store single digit numbers, teens, double digit tens, and powers of 10
# when splitting a number: work backwards?
# start from final 2 digits
# then hundreds and thousands
# concatenate thousands + hundreds + tens + ones

# O(n) where n is the number of digits in the number

# edge cases:
# 0
# numbers with teens
# numbers with zero digits (such as 101 or 3001)

# constraints on n are 0 <= n <= 9999

def numberToWord(n):

    # define dictionaries

    single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # blank left inside for easier indexing
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    double_digits = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    # zero edge case
    if n == 0:
        return "zero"
    
    # ONES

    last_digit = n % 10
    n = n // 10

    ones = single_digits[last_digit]

    if n == 0: return ones

    # TENS

    tens_digit = n % 10
    n = n // 10

    tens = ""

    if tens_digit == 1:
        ones = ""
        tens = teens[last_digit]
    
    else:
        tens = double_digits[tens_digit]

    if n == 0:
        return tens + ones
    
    # HUNDREDS
    hundreds_digit = n % 10
    n = n // 10

    hundreds = single_digits[hundreds_digit] 
    if hundreds_digit > 0:
        hundreds += " hundred "

    if n == 0:
        return hundreds + tens + ones
    
    #THOUSANDS
    thousands_digit = n % 10
    n = n // 10

    thousands = single_digits[thousands_digit] + " thousand"

    return thousands + " " + hundreds + tens + ones


print(numberToWord(0))
print(numberToWord(11))
print(numberToWord(201))
print(numberToWord(100))
print(numberToWord(9999))
print(numberToWord(4080))
print(numberToWord(4008))

    

        

    

    



