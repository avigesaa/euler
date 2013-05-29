def reversed_str(n):
    return str(n)[::-1]

def is_palindromic(n):
    return str(n) == reversed_str(n)
    
def is_lychrel(n):
    for i in xrange(50):
        n = n + int(reversed_str(n))
        if is_palindromic(n):
            return False        
    return True

print len(filter(is_lychrel, xrange(0, 10000)))
