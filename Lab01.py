"""Required questions for lab 1"""

## Boolean Operators ##

# Q4
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x > 0 and y > 0


## while Loops ##

# Q7
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    x = n
    while x > 0:
    	if(n%x == 0):
    		print(x)
    	x = x - 1
	
#Q8
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
    	return n
    else:
    	return fib(n-1) + fib(n-2)

#Extra Credit Work

def is_factor(x,y):
	# Will Return true if x is not zero
	# and the remainder of y/x == 0
	return x != 0 and y%x == 0

def gets_discount(x,y):
	# Discount for grandparents(65+) accompanying
	# grandchildren (12-)
	return (x >= 65 and y <=12) or (y >= 65 and x <= 12)

def falling_fact(n,k):
	# Calculates falling factorial of n to depth k
	total = 1
	while k > 0:
		total = total * n
		n -= 1
		k -= 1
	return total
