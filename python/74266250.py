def nondec(n):
    '''
    >>> nondec(113355779)
    True
    >>> nondec(44569)
    True
    >>> nondec(346234)
    False
    >>> nondec(222)
    True
    >>> nondec(789)
    True
    >>> nondec(55555)
    True
    >>> nondec(1234123)
    False
    >>> nondec(98765)
    False
    '''
    prev = 9
    while n > 0:
        lastdigit = n % 10
        if lastdigit > prev:
            return False
        prev = lastdigit
        n = int(n / 10)
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
