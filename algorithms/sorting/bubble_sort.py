
def bubble_sort(array):
    length_array = len(array)

    for i in range(length_array -1):
        for j in range(length_array -1):

            if (array[j] > array[j+1]):
                #Swap number 
                temp = array[j]
                array[j] = array[j+1]
                array[j+1]= temp
    return array

if __name__ == "__main__":
    numbers = [4, 7, 2, 1, 6, 3]

    print(bubble_sort(numbers))