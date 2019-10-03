# Author: Jessica Strait
# This project recursively finds the solution of an integer to the power of another integer. 

def power(x, n):
    # Write your code here
    # First I will check to see if both inputs are integers. If they are not, I'll return error.
    if type(x) is not int:
        return 'error'
    elif type(n) is not int:
        return 'error'
    else:
        # If n is negative, we will also return error.
        if n < 0:
            return 'error'
        # If n is exactly zero, we will return one.
        if n == 0:
            return 1
        # If n is exactly one, we return x.
        if n == 1:
            return x
        # Otherwise, we will use a recursive call to multiply x times the power function of x to the next smaller power.
        else:
            return x * power(x, n-1)
