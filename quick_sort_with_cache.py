def quicksort(n_list):
    if len(n_list) <= 1:
        return n_list

    pivot_list = [
        n_list[0],
        n_list[(len(n_list)-1) // 2],
        n_list[len(n_list)-1]
    ]
    pivot = sum(pivot_list) - max(pivot_list) - min(pivot_list)

    less_list = []
    more_list = []
    equal_list = []

    for n in n_list:
        if n < pivot:
            less_list.append(n)
        elif n > pivot:
            more_list.append(n)
        else:
            equal_list.append(n)

    print(f"less: {less_list}, equal: {equal_list}, more: {more_list}")

    return quicksort(less_list) + equal_list + quicksort(more_list)

l = [1,2,3,4,5,6,7]

print(quicksort(l))

# print(l)