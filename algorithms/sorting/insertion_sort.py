def insertion_sort(array):
    length_array = len(array)


    for i in range(1, length_array):
        
        pointer = array[i]
        j = i - 1

        while (j >= 0 and array[j] > pointer):

            array[j + 1] = array[j]

            j -= 1
        array[j + 1] = pointer

    return array
    


if __name__ == "__main__":
    numbers = [4, 7, 2, 1, 6, 3]

    print(insertion_sort(numbers))    