def sum_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop(0) + sum_list(lista)


def power(x, n):
    if n == 0:
        return 1

    else:
        return x * power(x, n-1)


def tail_rekursiv(num, product = 1):
    if num == 1:
        return product

    else:
        product *= num
        return tail_rekursiv((num-1), product)

def max_recursion(count):
    print(count)
    return max_recursion(count + 1)

if __name__ == '__main__':
    print(sum_list([5, 4, 2, 7, 1]))
    print(power(4, 6))

print(tail_rekursiv(5))
print(max_recursion(0))
