def fibonacci():
    current, next = 0, 1 
    while True:
        yield current
        current, next = next, current + next

result = 0;

for x in fibonacci():
    if x > 4000000:
        break
    if (x % 2) == 0:
        result += x

print result    



