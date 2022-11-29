
# Räkna ut 100!, summera siffrorna i svatet

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_digits(n):
    # För nummret n, summera siffrorna
    # Gör till en sträng
    s = 0
    # Summera siffrorna
    for digit in str(n):
        s += int(digit)

    return s

f = (factorial(100))
print(f)

print(sum_digits(f))
