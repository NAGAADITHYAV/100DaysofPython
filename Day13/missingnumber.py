def missing_number(s):
    k = 1
    while(str(k) in s):
        k += 1
    return k
print(missing_number('109875432'))