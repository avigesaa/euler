import itertools

def list_to_int(xs):
    return reduce(lambda x,y: x*10 + y, xs)

def is_substring_divisible(xs):
    return list_to_int(xs[7:10]) % 17 == 0 and \
           list_to_int(xs[6:9])  % 13 == 0 and \
           list_to_int(xs[5:8])  % 11 == 0 and \
           list_to_int(xs[4:7])  %  7 == 0 and \
           list_to_int(xs[3:6])  %  5 == 0 and \
           list_to_int(xs[2:5])  %  3 == 0 and \
           list_to_int(xs[1:4])  %  2 == 0

print sum(list_to_int(xs) for xs in itertools.permutations(range(0,10)) if is_substring_divisible(xs))
