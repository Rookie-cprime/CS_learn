
def fact(n):
    """
    Input:n is a number you want to factorial
    when you input an n it will return the factorial of it self

    """
    if n == 1:
        return n
    else:
        return n*fact(n-1)
    fact()