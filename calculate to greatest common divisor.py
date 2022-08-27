def gcd(x, y):
    i = 1
    result = 1
    while i <= x and i <= y:
        if not (x % i) and not (y % i):
            result = i
        i += 1
    return result


a = int(input("enter two number\n"))
b = int(input())
print("greatest common divisor:", gcd(a, b))
