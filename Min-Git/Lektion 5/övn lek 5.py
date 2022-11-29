
# Linjär sökning (ordo N)
def linear_serch(input_list, item):
    for index, value in enumerate(input_list):
        if value == item:
            return index

    return None


# unsorted_list = [4, 5, 1, 2, 15, 7]
# print(unsorted_list)
# print(linear_serch(unsorted_list, 15))

def binary_serch(input_list, item):
    first = 0
    last = len(input_list) - 1

    # Loop?
    while first <= last:
        midpoint = (first + last) // 2

        if item == input_list[midpoint]:
            return midpoint

        elif item < input_list[midpoint]:
            last = midpoint - 1

        elif item > input_list[midpoint]:
            first = midpoint + 1

    return None


sorted_list = [1, 2, 7, 9, 12, 13, 17, 21, 22]
#              0             4               8

print(binary_serch(sorted_list, 21))

a = 2
b = 5

temp = a
a = b
b = temp
# a == 5
# b == 2
a,b = b, a
print(a, b)
