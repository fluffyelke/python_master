def get_first_elem(my_list):
    return my_list[0]


def get_specific_elem(my_list, idx):
    return my_list[idx]


print(get_first_elem([1, 2, 3]))
print(get_specific_elem([10, 15, 20], 2))

# linear complexity (O(n))


def get_sum(my_list):
    total_sum = 0
    for elem in my_list:
        total_sum = total_sum + elem

    return total_sum


print(get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Quadratic time (O(n2))
def get_sum_v2(my_list):
    total_sum = 0
    for row in my_list:
        for elem in row:
            total_sum += elem

    return total_sum


print(get_sum_v2([[1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15]]))


# logarithmic (O(logN))

def search_binary(my_list, item):
    first = 0
    last = len(my_list) - 1
    found_flag = False
    while first <= last and not found_flag:
        mid = (first + last) // 2
        if my_list[mid] == item:
            found_flag = True
        else:
            if item < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found_flag


print(search_binary([8, 9, 10, 100, 1000, 2000, 3000], 10))

