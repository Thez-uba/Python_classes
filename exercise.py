# Create a python funtion to take in 2 integer and find the sum of even number between them.
a=13
b=3
def evenIntegers():
    total = 0
    for num in range(min(a,b), max(a,b)):
    # alternatively, if a > b:
    # a,b = b,a
        if num % 2 == 0:
            total += num
    print(total)
evenIntegers()

def oddIntegers(a,b):
    if a > b:
        a , b = b , a
    total = 0
    for num in range(a,b):
        if num % 2 != 0:
            total += num
    print(total)
oddIntegers(a,b)