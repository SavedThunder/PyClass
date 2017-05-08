# CS2021 Lab 02
# Q4
def f_to_c(fahrenheit):
    """Converts Fahrenheit to Celsius

    >>> f_to_c(14)
    -10.0
    >>> f_to_c(68)
    20.0
    >>> f_to_c(-31)
    -35.0
    """
    "*** YOUR CODE HERE ***"
    return (fahrenheit - 32) * (5/9)


def c_to_f(celsius):
    """Converts Celsius to Fahrenheit

    >>> c_to_f(0)
    32.0
    >>> c_to_f(5)
    41.0
    >>> c_to_f(-25)
    -13.0
    """
    "*** YOUR CODE HERE ***"
    return celsius * (9/5) + 32

#Q5
def dispatch_function(option1, f1, option2, f2):
    """Takes in two options and two functions. Returns a function that takes in
    an option and value and calls either f1 or f2 depending on the given option.

    >>> func_d = dispatch_function('c to f', c_to_f, 'f to c', f_to_c)
    >>> func_d('c to f', 0)
    32.0
    >>> func_d('f to c', 68)
    20.0
    >>> func_d('blabl', 2)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    "*** YOUR CODE HERE ***"
    def function(option, value):
    	assert option == option1 or option == option2
    	if(option == option1):
    		return f1(value)
    	if(option == option2):
    		return f2(value)
    return function


# Q6
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    def printing(value):
    	num = 0
    	while(num < value):
    		if(num%n == 0):
    			print("Buzz!")
    		else:
    			print(num)
    		num += 1
    return printing

#  Q7
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
    	f = sub
    else:
    	f = add
    return f(a, b)

#  Q8
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return (a*a + b*b + c*c) - (min(a,b,c)*min(a,b,c))


###  Q9
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    "*** YOUR CODE HERE ***"
    i = 2
    factor = 0;
    while i < n:
    	if n % i == 0:
    		factor = i
    	i+=1
    return factor


###  Q10
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

   >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

        
#   Q11
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    assert n > 0
    print(n)
    while n != 1:
        if n > 1:
            if n%2 == 0:
                n = n // 2
                print(n)
                count += 1
            else:
                n = n * 3 + 1
                print(n)
                count += 1
    return count