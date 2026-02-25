a = 1

def simple_interest(p, r, t):
    return p * r * t

def compound_interest(p, r, t):
    return p * (1 + r) ** t

def rate_of_interest(si, t):
    return ((((1+(si/100))**t)*100)-100)/t

sis = [1,2,3,4,5, 6, 7, 8, 9, 10]

for si in sis:
    for t in range(1,11):
        print(rate_of_interest(si, t), end=" ")
    print()