import itertools
import operator

def fractional_digits():
    for n in itertools.count():
        for d in str(n):
            yield int(d)

def filtered_fractional_digits(digit_indices):
    max_index = max(digit_indices)
    for i, d in enumerate(fractional_digits()):
        if i in digit_indices:
            yield d
        if i >= max_index:
            break

indices = [1, 10, 100, 1000, 10000, 100000, 1000000]

print reduce(operator.mul, filtered_fractional_digits(indices)) 
        
