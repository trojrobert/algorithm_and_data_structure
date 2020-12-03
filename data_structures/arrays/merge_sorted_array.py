

def merge_sorted_array(array_1, array_2):



    if len(array_1) == 0 or len(array_2) == 0:
        return array_1 + array_2

    
    merged_array = []

    i = 0
    j = 0

    while ( i < len(array_1) and j <  len(array_2)):

        if(array_1[i] <= array_2[j]):

            merged_array.append(array_1[i]) 
            i += 1

        else:

            merged_array.append(array_2[j]) 
            j += 1
    return merged_array + array_1[i:] + array_2[j:]

if __name__ == "__main__":

    print(merge_sorted_array([0,3,4,30], [3, 8, 89, 100]))

    