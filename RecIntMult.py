# Input: two n-digit positive integers x and y
# Output: the product x * y
# Assumption: n is a power of 2

def RecIntMult(x, y, n):
    if n == 1:
        return x * y
    
    else:
        a = int(str(x)[:n // 2])
        b = int(str(x)[n // 2:])

        c = int(str(y)[:n // 2])
        d = int(str(y)[n // 2:])

        ac = RecIntMult(a, c, n // 2)
        ad = RecIntMult(a, d, n // 2)
        bc = RecIntMult(b, c, n // 2)
        bd = RecIntMult(b, d, n // 2)


        return (10**n) * ac + ((10** (n // 2)) * (ad + bc)) + bd

print(RecIntMult(5678, 1234, 4)) # Expected: 7006652, Result: 7006652
