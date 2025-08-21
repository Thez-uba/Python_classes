def multiplier(number):
    return lambda a: number * a
y= multiplier(18)
print(y(3))