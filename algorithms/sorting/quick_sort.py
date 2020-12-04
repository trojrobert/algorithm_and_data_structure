
def partition(array, low, high):

    i = (low -1)
    pivot = array[high]


    for j in range(low, high):

        if array[j] <= pivot:
            i = i+1

            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    return (i+1)


def quicksort(array, low, high):

    if len(array) == 1:
        return array

    if low < high: 

        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index-1)
        quicksort(array, partition_index+1, high)

    return array


if __name__ == "__main__":
    array = [ 5, 1, 7, 2, 4]
    print(*array, sep=",")

    array_length = len(array)
    sorted_array = quicksort(array, 0 , array_length-1)

    print(*sorted_array, sep=",")

