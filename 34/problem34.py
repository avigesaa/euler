from math import factorial

def factorial_digit_sum(n):
    return factorial(n % 10) + factorial_digit_sum(n // 10) if n > 0 else 0

print sum(x for x in xrange(10, 9999999) if x == factorial_digit_sum(x))
