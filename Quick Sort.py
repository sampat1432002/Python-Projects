
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]


    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        p = partition(start, end, array)

        # Sort elements before partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


array = [10, 7, 8, 9, 1, 5]
print("Unsorted array is:", end="\n")
print(*array)
quick_sort(0, len(array) - 1, array)
print("After applying Quick Sort array is: ", end="\n")
print(*array)