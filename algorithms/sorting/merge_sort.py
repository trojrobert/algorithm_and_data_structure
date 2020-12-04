

def do_merge_sort(array):

    #divide the array
    array_length = len(array)

    if array_length > 1:
        middle = array_length//2 

        left_array = array[0:middle]
        right_array =array[middle:array_length]

        do_merge_sort(left_array)
        do_merge_sort(right_array)


        i = j = k = 0

        while i < len(left_array)and j < len(right_array):

            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1

            else:
                array[k] = right_array[j]
                j += 1

            k += 1


        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):

            array[k] = right_array[j]
            j += 1
            k += 1

    return array

def print_list(array):
    print(*array, sep=',')

if __name__ == "__main__":
    array = [ 12, 11, 3, 1, 5, 9]

    print_list(array)

    sorted_array = do_merge_sort(array)

    print_list(sorted_array) 



