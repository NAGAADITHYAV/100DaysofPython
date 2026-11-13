import cmath
def average(a,b):
    return (a+b)/2

def square_root(n):
    '''
    lets start with g = 1
    then n/g == g then return g else take g = average of g, n/g
    '''
    real = True
    if n < 0:
        n = abs(n)
        real = False
    g = 1
    while(abs((n/g)-g) > 0.000000000000001):
        g = average(n/g, g)
    if real:
        return g
    else:
        return complex(0,g)

print(square_root(1.5))
print(square_root(-1))