

def bubble_sort(unsorted_list):

    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)- 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                # swap
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list




unsorted_list = [5, 3, 4, 7, 2]

print(bubble_sort(unsorted_list))


def bubble_sort2(unsorted_list):
    lst = unsorted_list.copy()
    swapped = False
    compared_count = 0
    for i in range(0, len(lst)-1):

        for j in range(0, len(lst) - i -1):
            compared_count += 1  ########################
            if lst[j] > lst[j+1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True


        if not swapped:
            break
    print("Compare count:", compared_count)
    return unsorted_list


unsorted_list = [5, 3, 4, 7, 2]

print(bubble_sort(unsorted_list))

print(bubble_sort2(unsorted_list))
