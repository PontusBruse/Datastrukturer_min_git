
# Fakultet (factorial)

def factorial(n):
    # Basfall
    if n == 1:
        return 1
    # Rekusivt fall
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    print(factorial(1)) # 1!
    print(factorial(2)) # 2!
    print(factorial(3)) # 3!
    print(factorial(10)) # 10 * 9 * 8 ... * 2 * 1