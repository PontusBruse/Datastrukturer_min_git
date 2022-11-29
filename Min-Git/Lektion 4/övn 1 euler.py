def even_3_5_sum(limit):
    s = 0
    for number in range(0, limit):
        if number % 3 == 0 or number % 5 == 0:
            s += number

    return s

if __name__ == '__main__':
    print(even_3_5_sum(1000)) # ska bli 23
    # 3+5+6+9=23