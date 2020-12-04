

def selection_sort(array):

    array_length = len(array)

    for i in range(array_length - 1):

        min_index = i
        
        for j in range(i + 1, (array_length)):
    
            if (array[j] < array[min_index]):
                min_index = j
        
        #swap

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

        print(array)
    
    return array

if __name__ == "__main__":
    numbers = [4, 7, 2, 1, 6, 3]

    selection_sort(numbers)    