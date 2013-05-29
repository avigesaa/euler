def reverse_str(n):
    return str(n)[::-1]

def is_palindromic(n):
    return str(n) == reverse_str(n)
    
def is_lychrel(n):
    for i in xrange(0,50):
        n = n + int(reverse_str(n))
        if is_palindromic(n):
            return False        
    return True

print len(filter(is_lychrel, xrange(0, 10000)))





