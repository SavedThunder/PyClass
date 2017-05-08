# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    assert n > 0
    if n <= 1:
        return n
    return n + skip_add(n-2)


#Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        return (gcd(b,a))
    while a > b and not (a % b == 0):
        a, b = b , a%b
    return b

        


# Q7
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n//2)
    if n % 2 != 0:
        return  1 + hailstone(n*3 + 1)


# Q8
def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if(m==1 | n==1):
        return 1
    num_paths = 0
    if(m > 1):
        num_paths += paths(m-1,n)
    if(n > 1):
        num_paths += paths(m,n-1)
    return num_paths

#Q10
def count_vals(nlist):
    if type(nlist) == list:
        return sum(count_vals(i) for i in nlist)
    else:
        return 1

