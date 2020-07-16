def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a<b:
        temp = b
        b = a
        a = temp
    c = b
    while True:
        if (b%c == 0) and (a%c == 0):
            break
        c-=1
    return c

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
